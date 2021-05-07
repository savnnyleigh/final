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

#create
@app.route('/generate', methods=['GET'])
def generate():
    unemployment_data = {}
    unemployment_data['Year'] = 
    unemployment_data['Area'] = 
    unemployment_data['Employment'] = 
    unemployment_data['Civilian Labor Force'] = 
    unemployment_data['Unemployment'] = 
    unemployment_data['Unemployment Rate'] = 
 
    rd.hmset(str(uuid.uuid4()), this_animal)
  
    return '20 animals have been generated'

#read
@app.route('/animals/created_on/<string:s_date>/<string:e_date>', methods = ['GET'])
def get_animals(s_date,e_date):
	test = get_data()
	animals_r = data['animals']
	list1 = []
	start = datetime.strptime(s_date, '%Y-%m-%d')
	end = datetime.strptime(e_date, '%Y-%m-%d')
	for animal in animals:
		date = datetime.strptime(animal['created_on'], '%Y-%m-%d')
		if ((date>=start) and (date<=end)):
			list1.append(animal)
	return jsonify({'animals in range': list1})

#update
@app.route('/animals/mod/<string:sel_uid>', methods = ['PUT'])
def mod_animals_uuid(sel_uid):
	test = get_data()
	animals_m = data['animals']
	for animal in animals_m:
                if (animal['uid'] == sel_uid):
			tail = animal['tail']
			animal['tail'] = tail + 2
                        return jsonify ({'modified animal':animal})
        	else :
                	return jsonify ({'animal': 'animal does not exist'})
#delete
@app.route('/delete/<string:s_date>/<string:e_date>', methods = ['GET'])
def del_animals(s_date,e_date):
	test = get_data()
	unemployment_data_d = data['unemployment_data']
	list2 = []
        start = datetime.strptime(s_date, '%Y-%m-%d')
        end = datetime.strptime(e_date, '%Y-%m-%d')
	for animal in animals_d:
                date = datetime.strptime(animal['created_on'], '%Y-%m-%d')
                if ((date<start) or (date>end)):
                        list2.append(animal)
        return jsonify({'Unemployment data without data in range': list2})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
