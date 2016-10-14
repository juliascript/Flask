# API Services Flask Challenges 

## :zero: 
Install Flask web server framework with `pip install Flask`. Test that it’s installed with `python -c "import flask"`.
## :one: 
Create a simple Flask web server that receives GET requests to the route `/hello` and responds with a friendly message. Test this route in your web browser and using Curl, Postman, or another tool to make HTTP requests.
## :two: 
Add a new handler that receives POST requests to the route `/pets` with JSON data in the body and returns that JSON data unmodified in the response body. Test the `/pets` route using Curl, Postman, or another tool to make HTTP POST requests to ensure it responds correctly with the same data given in the request.
## :three: 
Modify the `/pets` handler to parse the JSON data, validate that it has *all* of these fields: `name`, `age`, `species`. If it passes validation, store the parsed dictionary in a simple list variable (this will serve as a temporary in-memory database so these pets will be saved for the lifetime of the web server). If not, respond with a HTTP 400 error and a helpful error message in JSON. Test the `/pets` route to ensure it responds correctly to *both* valid and invalid POST requests.
## :four: 
Add a new handler that receives GET requests to the route `/pets` and responds with a JSON representation of the list of *all* pets. Test that the `/pets` route responds correctly to GET requests.
## :five: 
Add a new handler that receives GET requests to the route `/pets/<name>` and checks if a pet with that name exists. If so, return a JSON representation of the pet. If not, respond with a HTTP 404 error and a helpful JSON error message. Test that the `/pets/<name>` route responds correctly to GET requests with a name that exists and another that doesn’t.