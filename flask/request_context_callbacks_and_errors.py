# The request context keeps track of the request-level data during a 
# request. Rather than passing the request object to each function that 
# runs during a request, the request and session proxies are accessed 
# instead.

# When the Flask application handles a request, it creates a Request object 
# based on the environment it received from the WSGI server. Because a 
# worker (thread, process, or coroutine depending on the server) handles 
# only one request at a time, the request data can be considered global to 
# that worker during that request. Flask uses the term context local for 
# this.
# Flask automatically pushes a request context when handling a request. 
# View functions, error handlers, and other functions that run during a 
# request will have access to the request proxy, which points to the 
# request object for the current request.

# The Flask.wsgi_app() method is called to handle each request. It manages 
# the contexts during the request. Internally, the request and application 
# contexts work like stacks. When contexts are pushed, the proxies that 
# depend on them are available and point at information from the top item.
# When the request starts, a RequestContext is created and pushed, which 
# creates and pushes an AppContext first if a context for that application 
# is not already the top context. While these contexts are pushed, the 
# current_app, g, request, and session proxies are available to the 
# original thread handling the request.
# After the request is dispatched and a response is generated and sent, 
# the request context is popped, which then pops the application context.
# Immediately before they are popped, the teardown_request() and 
# teardown_appcontext() functions are executed. These execute even if an 
# unhandled exception occurred during dispatch.

# Flask dispatches a request in multiple stages which can affect the 
# request, response, and how errors are handled. The contexts are active 
# during all of these stages.

# 1. Before each request, before_request() callbacks are called. If one of 
#    these functions return a value, the other functions are skipped. The 
#    return value is treated as the response and the view function is not 
#    called.
# 2. If the before_request() callbacks did not return a response, the view 
#    function for the matched route is called and returns a response.
# 3. The return value of the view is converted into an actual response 
#    object and passed to the after_request() callbacks. Each function 
#    returns a modified or new response object.
# 4. After the response is returned, the contexts are popped, which calls 
#    the teardown_request() and teardown_appcontext() callbacks. These 
#    functions are called even if an unhandled exception was raised at any 
#    point above.

# If an exception is raised before the teardown functions, Flask tries to 
# match it with an errorhandler() function to handle the exception and 
# return a response. The teardown functions are still called, and are 
# passed the exception object.

# The teardown callbacks are independent of the request dispatch, and are 
# instead called by the contexts when they are popped. The teardown 
# functions are called even if there is an unhandled exception during 
# dispatch, and for manually pushed contexts. This means there is no 
# guarantee that any other parts of the request dispatch callbacks where 
# executed. Be sure to write teardown callbacks in a way that does not 
# depend on other callbacks and will not fail.

# The following signals are sent:
# 1. request_started is sent before the before_request() functions are 
#    called.
# 2. request_finished is sent after the after_request() functions are 
#    called.
# 3. got_request_exception is sent when an exception begins to be handled,
#    but before an errorhandler() is looked up or called.
# 4. request_tearing_down is sent after the teardown_request() functions 
#    are called.
from flask import Flask

app = Flask(__name__)

@app.before_request
def before():
    print("before")

@app.after_request
def after(response):
    print("after")
    return response

@app.teardown_request
def teardown(exception):
    print("teardown", f'exception {exception}')

@app.get("/")
def index():
    print("inside")
    return "<p>Hello world!</p>"
