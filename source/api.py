import json
from flask import Flask, request
import jobs

app = Flask(__name__)

def get_data():
    with open("unemployment_rates.json", "r") as json_file:
        user_data = json.load(json_file)
    return user_data

@app.route('/jobs', methods=['POST'])
def jobs_api():
    try:
        job = request.get_json(force=True)
    except Exception as e:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    return json.dumps(jobs.add_job(job['start'], job['end']))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
