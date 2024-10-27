from flask import Flask, request, url_for, redirect, session

# the instance of this class is an WSGI application.
# must be initiated with the module or package's name.
app = Flask(__name__)

# specifies whitch url will trigget this function.
@app.route("/")
def hello_world():
    # HTML is the default response type in Flask.
    return "<p>Hello, World!</p>"

# create a route with a variable section <id>
# the function receives the argument as a keyword argument.
@app.route("/user/<user>")
def index(user):
    return user

# it's also possible to convert the variable value to one
# of the following values:
# - string: (default) accepts any text without a slash.
# - int: accepts positive integers.
# - float: accepts positive floating point values.
# - path: like string but also accepts slashes.
# - uuid: accepts UUID strings.
# the form is: <converter:variable_name>.
@app.route("/user-id/<user>/<int:id>")
def user_id (user, id):
    return f"<p>User: {user}, ID: {id}</p>"

# if a route is defined with a trailing slash, accessing the route without
# the trailing slash will redirect to the same path with the trailing
# slash.
# if it is defined without a trailing slash, acessing the route with the
# trailing slash will produce a 404 error.

# It's also possible to build the url of a specific function with
# url_for().
# It accepts the name of the function as its first argument and any number
# of keyword arguments, each corresponding to a variable part of the URL
# rule. Unknown variable parts are appended to the URL as query 
# parameters.
# to generate url for static files use the special "static" endpoint name:

# url_for("static", filename="some_image.png")
# the file has to be stored on the filesystem as static/some_image.png

with app.test_request_context():
    # prints: /user/lopes
    print(url_for('index', user="lopes"))
    # prints /user-id/lopes/1?query_param=qp
    print(url_for(
        'user_id',
        user="lopes",
        id=1,
        query_param="qp"
    ))

# by default, a route only answers to GET requests.
# a route can answer to many methods.
# to access the method of the current request, use flask.request.method.
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        return "<p>Sign up form</p>"
    else:
        return "<p>Sign in form</p>"

# the above implementation is good if you want to share some variables
# between the two methods. But it's also possible to define them
# apart:
@app.get("/request")
def request_get():
    return "<p>This request was a get</p>"

@app.post("/request")
def request_post():
    return "<p>This request was a post</p>"

# note that:
# 1. if GET is present, Flask automatically adds support for the 
#    HEAD method and handles HEAD requests according to the HTTP RFC. 
#    Likewise, OPTIONS is automatically implemented for you.
# 2. you can also decorate a route with @app.delete() or @app.put(), etc.

# To serve static files just create a folder called static in your package
# or next to your module and it'll be available at /static on the
# application.

# Context Locals
# Some objects in Flask, like the request object, looks like global
# objects, but in reallity they are proxies to objects that are local
# to a specific context.
# Imagine the context being the handling thread. A request comes in and the
# web server decides to spawn a new thread.
# When Flask starts its internal request handling it figures out that the 
# current thread is the active context and binds the current application 
# and the WSGI environments to that context. It does that in a way so that 
# one application can invoke another application without breaking.

# Thats why you need the context manager app.test_request_context() while 
# unit testing.
# During unit tests you dont have a WSGI environment running thus Flask 
# isn't capable of binding the application and the WSGI environment 
# togheter in the current context.
# Another option is to use app.request_context(environ) which expects
# environ to be a complete WSGI environment.

# The request object
# 1. The current request method is available by using request.method.
# 2. To access form data you can use request.form. If the key doesn't 
#    exist a special KeyError is raised. If you don't catch it, a 400 Bad 
#    Request error page is shown.
# 3. To access query params you can use request.args dictionary.
# 4. You can access files sent in a request by using request.files. It's
#    a dictionary. Each file behaves like a standard file object with the
#    addition of a save() method that allows you to store that file on the
#    server's filesystem.
# 5. To access request cookies you can use request.cookies dictionary.
#    You should use the get() method to avoid a KeyError and the
#    set_coockie(cookie, value) method. Note that cookies are set on
#    response objects.

@app.get("/redirect")
def redirect_to():
    return redirect(url_for("hello_world"))

# About responses
# The return value from a view function is automatically converted into a
# response object.
# The logic that Flask applies to converting return values into response 
# objects is as follows:
# 
# 1. If a response object of the correct type is returned it’s directly 
#    returned from the view.
# 2. If it’s a string, it’s converted into a response object with the 
#    string as response body, a 200 OK status code and a text/html 
#    mimetype.
# 3. If it’s an iterator or generator returning strings or bytes, it is 
#    treated as a streaming response.
# 4. If it’s a dict or list, a response object is created using jsonify().
# 5. If a tuple is returned the items in the tuple can provide extra 
#    information. Such tuples have to be in the form (response, status),
#    (response, headers), or (response, status, headers). The status value
#    will override the status code and headers can be a list or dictionary 
#    of additional header values.
# 6. If none of that works, Flask will assume the return value is a valid
#    WSGI application and convert that into a response object.

# If you want to get hold of the resulting response object inside the view 
# you can use the make_response() function. You can wrap the return 
# expression with make_response() and get the response object to modify it,
# then return it from the view.

# Sessions
# In addition to the request object there is also a second object called 
# session which allows you to store information specific to a user from 
# one request to the next. This is implemented on top of cookies for you 
# and signs the cookies cryptographically.

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def is_logged():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# A note on cookie-based sessions: Flask will take the values you put into 
# the session object and serialize them into a cookie. If you are finding 
# some values do not persist across requests, check if cookies are indeed 
# enabled, and you are not getting a clear error message, check the size 
# of the cookie in your page responses compared to the size supported by 
# web browsers.
