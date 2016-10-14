from flask import Flask, request, json
app = Flask(__name__)

listOfPets = []

@app.route('/hello')
def hello():
    return 'Hello there!\n'

@app.route('/pets', methods=['POST'])
def storePets():
	result = request.args.to_dict()
	listOfPets.append(result)
	return json.dumps(result)
	

if __name__ == '__main__':
    app.run()