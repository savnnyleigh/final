import json
from flask import Flask, request
import jobs
import redis

app = Flask(__name__)

def get_data():
    with open("unemployment_rates.json", "r") as json_file:
        user_data = json.load(json_file)
    return user_data

rd = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route('/jobs', methods=['POST'])
def jobs_api():
    try:
        job = request.get_json(force=True)
    except Exception as e:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    return json.dumps(jobs.add_job(job['start'], job['end']))

@app.route('/', methods = ['GET'])
def get_animals():
	return json.dumps(get_data())

@app.route('/animals/arms/<arm_num>', methods = ['GET'])
def get_animals_arms(arm_num):
	test = get_data()
	return json.dumps([x for x in test if x['arms'] == arm_num])

@app.route('/animals/head/<head>', methods = ['GET'])
def get_animals_head(head):
	test = get_data()
	return json.dumps([x for x in test if x['head'] == head])



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
