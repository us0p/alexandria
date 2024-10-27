# Error handler
# An error handler is a function that returns a response when a type of 
# error is raised.
# The handler receives an instance of the error being handled, which is 
# most likely a HTTPException.
# The status code of the response will not be set to the handler’s code. 
# Make sure to provide the appropriate HTTP status code when returning a 
# response from a handler.

# A handler can be registered by decorating a function with errorhandler().
# Or using register_error_handler() to bind the function later.
from flask import Flask
from werkzeug.exceptions import HTTPException, BadRequest

app = Flask(__name__)

@app.errorhandler(BadRequest)
def handle_bad_request(bad_request_error_instance):
    return 'bad request!', bad_request_error_instance.code

# or app.register_error_handler(400, handle_bad_request)

@app.get("/")
def index():
    raise BadRequest

# Handlers can be registered for any exception class, not just 
# HTTPException subclasses or HTTP status codes. Handlers can be registered
# for a specific class, or for all subclasses of a parent class.

# If some part of your code breaks while handling a request (and you have 
# no error handlers registered), a “500 Internal Server Error” will be 
# returned by default. Similarly, “404 Not Found” error will occur if a 
# request is sent to an unregistered route. If a route receives an 
# unallowed request method, a “405 Method Not Allowed” will be raised. 
# These are all subclasses of HTTPException and are provided by default in 
# Flask.

# When Flask catches an exception while handling a request, it is first 
# looked up by code. If no handler is registered for the code, Flask looks 
# up the error by its class hierarchy; the most specific handler is chosen.
# If no handler is registered, HTTPException subclasses show a generic 
# message about their code, while other exceptions are converted to a 
# generic “500 Internal Server Error”.

# Handlers registered on the blueprint take precedence over those 
# registered globally on the application, assuming a blueprint is handling 
# the request that raises the exception. However, the blueprint cannot 
# handle 404 routing errors because the 404 occurs at the routing level 
# before the blueprint can be determined.

# It is possible to register error handlers for very generic base classes 
# such as HTTPException or even Exception.
# However, this handler will trigger for exceptions raised outside of your
# view, such as 404 and 405 errors during routing. Be sure to craft your 
# handler carefully so you don’t lose information about the HTTP error.
from flask import json

@app.errorhandler(HTTPException)
def handle_generic_exception(e):
    # start with the correct header and status code from the error
    response = e.get_response()
    # replace body with JSON.
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description
    })
    response.content_type = "application/json"
    return response

# This route exception will be handle by our generic error handler.
@app.get("/e1")
def handle_generic_error():
    raise Exception

# This route exception will be handled by our specific error handler.
@app.get("/e2")
def handle_bad_request_error():
    raise BadRequest

# Since HTTPException instances are valid WSGI responses, you could also 
# return them as responses.
