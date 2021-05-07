from jobs import q, update_job_status
import matplotlib.pyplot as plt
import numpy as np
import redis

rd = redis.StrictRedis(host='172.17.0.1', port=6379, db=0)

@q.worker
def execute_job(jid):
    jobs.update_job_status(jid, 'in progress')
   
    X = np.arange(10)
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    plt.xlabel('Years')
    plt.ylabel('Unemployment Rates')
    ax.bar(X + 0.00, data[0], color = 'b', width = 0.25)
    ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)
    ax.bar(X + 0.50, data[2], color = 'y', width = 0.25)
    ax.bar(X + 0.75, data[3], color = 'r', width = 0.25)
    
    plt.show()
    plt.savefig('my_fig.png')

   """ years =
    regions =
    unemployment_rates ="""


    # read the raw file bytes into a python object
    file_bytes = open('/tmp/my_fig.png', 'rb').read()

    # set the file bytes as a key in Redis
    rd.set('key', file_bytes)


    jobs.update_job_status(jid, 'complete')

execute_job()
