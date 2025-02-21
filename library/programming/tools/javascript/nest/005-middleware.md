# Middlware
Is a function which is called before the route handler. Middleware 
functions have access to the `request` and `response` objects, and the 
`next` middleware function in the application's request-response 
cycle. The next middleware function is commonly denoted by a variable named
`next`
Nest middlware are, by default, equivalent to `express` middleware.

It's not possible to create generic middleware which can be used across all
contexts across the whole application. This is because middleware is 
unaware of the execution context, including the handler that will be called
an any of its parameters.
