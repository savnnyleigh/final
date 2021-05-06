import uuid
from hotqueue import HotQueue
from redis import StrictRedis
import os

q = HotQueue("queue", host='172.17.0.1', port=6379, db=1)
rd = StrictRedis(host='172.17.0.1', port=6379, db=0)

def _generate_jid():
    return str(uuid.uuid4())

def _generate_job_key(jid):
    if type(jid) == bytes:
	jid = jid.decode('utf-8')
    return 'job.{}'.format(jid)

#changes based on job
def _instantiate_job(jid, status, start, end):
    if type(jid) == str:
        return {'id': jid,
                'status': status,
                'start': start,
                'end': end
        }
    return {'id': jid.decode('utf-8'),
            'status': status.decode('utf-8'),
            'start': start.decode('utf-8'),
            'end': end.decode('utf-8')
    }

def _save_job(job_key, job_dict):
    """Save a job object in the Redis database."""
    rd.hmset(job_key, job_dict)

def _queue_job(jid):
    """Add a job to the redis queue."""
    q.put(jid)

#job_dict changes based on job
def add_job(start, end, status="submitted"):
    """Add a job to the redis queue."""
    jid = _generate_jid()
    job_dict = _instantiate_job(jid, status, start, end)
    save_job(_generate_job_key(jid), job_dict)
    queue_job(jid)
    return job_dict

#changes based on job
def update_job_status(jid, new_status):
    """Update the status of job with job id `jid` to status `status`."""
    jid, status, start, end = rd.hmget(generate_job_key(jid), 'id', 'status', 'start', 'end')
    job = _instantiate_job(jid, status, start, end)

    if(new_status == 'in progress'):
        worker_IP = os.environ.get('WORKER_IP')
        print(worker_IP)
        rd.hset(_generate_job_key(jid), 'worker', worker_IP)

    if job:
        job['status'] = new_status
        _save_job(_generate_job_key(jid), job)
 
   else:
        raise Exception()
