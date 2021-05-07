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
    c_year = decimal.Decimal(input('Enter Year'))
    c_area = input('Enter updated area')
    c_employment = decimal.Decimal(input('Enter updated number employed'))
    c_Civ = decimal.Decimal(input('Enter updated civilian labor force'))
    c_unem = decimal.Decimal(input('Enter updated number unemployed'))
    c_rate = c_unem/c_Civ

    new_data = {
	    'Year': c_year
	    'Area': = c_area
	    'Employment': c_employment
	    'Civilian Labor Force': c_Civ
	    'Unemployment': c_unem
	    'Unemployment Rate': c_rate    
    }

    test = get_data()
    
    test.push(JSON.stringify(new_data)) 
  
    return 'Data point has been created'

#read
@app.route('/query/<year>', methods = ['GET'])
def get_years(year):
	test = get_data()
	data_r = data['Unemployment Rates']
	list1 = []
	start = datetime.strptime(year, '%Y')
	for rate in data_r:
		date = datetime.strptime(rate['Year'], '%Y')
		if ((date == year)):
			list1.append(rate)
	return jsonify({'Data in range': list1})

#update
@app.route('/update/<year>/<area>', methods = ['PUT'])
def mod_animals_uuid(year,area):
	test = get_data()
	data_m = data['Unemployment rates']
	for rate in data_m:
                if ((rate['Year'] == year) and (rate['Area'] == area)):
			n_year = decimal.Decimal(input('Enter Year'))
			n_area = input('Enter updated area')
			n_employment = decimal.Decimal(input('Enter updated number employed'))
			n_Civ = decimal.Decimal(input('Enter updated civilian labor force'))
			n_unem = decimal.Decimal(input('Enter updated number unemployed'))
			n_rate = n_unem/n_Civ
			rate['Year'] = n_year
   			rate['Area'] =n_area
   			rate['Employment'] = n_employment
   			rate['Civilian Labor Force'] = n_Civ
   			rate['Unemployment'] = n_unem
   			rate['Unemployment Rate'] = n_rate
                        return jsonify ({'Updated data' : rate})
        	else :
                	return 'Data point does not exist, add new entry instead'

#delete
@app.route('/delete/<year>/<area>', methods = ['GET'])
def del_animals(year,area):
	test = get_data()
	data_d = data['Unemployment rates']
	list2 = test
        start = datetime.strptime(year, '%Y')
	for rate in data_d:
            date = datetime.strptime(rate['Year'], '%Y')
            if ((date == start) and (rate['Area'] == area)):
                list2.remove(rate)


	 with open("unemployment_rates.json", "r") as json_file:
    	    json.dump(list2, json_file)
    


        return ('Data points have been deleted')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
