from flask import Flask, request, json
app = Flask(__name__)

listOfPets = []

@app.route('/hello')
def hello():
    return 'Hello there!\n'

@app.route('/pets', methods=['GET', 'POST'])
def storePets():
	if request.method == "GET":
		return json.dumps(listOfPets)
	elif request.method == "POST":
		result = request.args.to_dict()
		print(result)
		if ('name' in result.keys()) & ('age' in result.keys()) & ('species' in result.keys()):
			listOfPets.append(result)
			return json.dumps(result)
		else:
			return 'HTTP 400 Error: Bad Request -- Please provide name, age, and species in query string.'


if __name__ == '__main__':
    app.run()