from flask import Flask, request
app = Flask(__name__)

listOfPets = []

@app.route('/hello')
def hello():
    return 'Hello there!\n'

@app.route('/pets', methods = ['GET', 'POST'])
def storePets():
	if request.method == "GET":
		return listOfPets
	elif request.method == "POST":
		# for each elem in the json blob, add it to teh list 

		return "POST"

if __name__ == '__main__':
    app.run()