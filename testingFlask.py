from flask import Flask, request, json
app = Flask(__name__)

listOfPets = []
namesOfPets = []

# / route
@app.route('/')
def default():
    return 'Welcome to teh pet store bruh\n'

# /hello route
@app.route('/hello')
def hello():
    return 'Hello there!\n'

# /pets route
@app.route('/pets', methods=['GET', 'POST'])
def pets():
	# If a GET request comes in on the /pets route
	if request.method == "GET":
		# Return all pets in the listOfPets list
		return json.dumps(listOfPets)
	# If a POST request comes in on the /pets route
	elif request.method == "POST":
		# Parse the request arguments into a dictionary
		result = request.args.to_dict()
		# If the required arguments (name, age, and species) are in the dictionary, proceed
		if ('name' in result.keys()) & ('age' in result.keys()) & ('species' in result.keys()):
			nameOfPet = result['name']
			# If the name of new pet not already in the namesOfPets list, proceed
			if nameOfPet not in namesOfPets:
				# Add the pet to the listOfPets list
				listOfPets.append(result)
				# Add the name of the pet to the namesOfPets list (the name is currently being used as a unique id)
				namesOfPets.append(nameOfPet)
				return 'Pet added to store\n'
			# If the name of the new pet is already in the namesOfPets list, return 409 error
			else: 
				return 'HTTP 409 Error: Conflict -- Pet already exists in store.\n', 409
		# If the required arguments (name, age, and species) are not in the dictionary, return 400 error
		else:
			return 'HTTP 400 Error: Bad Request -- Please provide name, age, and species in query string.\n', 400

# /pets/<name>
@app.route('/pets/<path:name>')
def petPath(name):
	# Iterate over all pets stored in listOfPets
	for pet in listOfPets:
		# If the name of the pet is equal to the name specified in the path, proceed
		if pet['name'] == name:
			# Return that pet
			return json.dumps(pet)
	# Otherwise, return a 404 error
	return 'HTTP 404 Error: Page Not Found -- Pet does not exist in store\n', 404

if __name__ == '__main__':
    app.run()