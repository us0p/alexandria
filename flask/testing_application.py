# A Flask() instance has two methods used while testing your application:
# test_client() -> Extends Werkzeug's client and it's used to make
#                  requests to your application without having to start
#                  the server.
# test_cli_runner() -> Creates a runner that can call the Click commands
#                      registered with the application.

# Tips to test Flask applications
# The factory yielded by Flask() doesn't have much to test, but it's
# configurations.
# To test authentication you can create a class that will receive the
# client and have methods to login and logout the user, you can then
# use this class inside your tests to avoid writing login and logout
# requests in every test.

# The test client:
# When you perform a request with the client produced by app.test_client()
# it returns a TestResponse object which represents the Response object
# send back to the client in normal requests.
# In this object you can:
# 1. assert its status code with: response.status_code.
# 2. assert headers with: response.headers (it's a dict).
# 3. get the response data as bytes in: response.data, values expected to
#    render on the page should be here, if you want to get the value of 
#    this field as text instead of bytes you should use 
#    response.get_data(as_text=True).
# 4. using client in a with block allows accessing context variables such
#    as session after the response is returned.
