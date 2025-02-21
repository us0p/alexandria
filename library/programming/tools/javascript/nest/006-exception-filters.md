# Exception Filters
Nest comes with a built-in exceptions layer which is responsible for 
processing all unhandled exceptions across an application. When an 
exception is not handled by your application code, it is caught by this 
layer, which then automatically sends an appropriate user-friendly 
response.
Out of the box, this action is performed by a built-in global exception 
filter, which handles exceptions of type HttpException. When an exception 
is unrecognized, the built-in exception filter generates the following 
default JSON response:

```json
{
  "statusCode": 500,
  "message": "Internal server error"
}
```

## Throwing standard exceptions#
Nest provides a built-in HttpException class, exposed from the 
`@nestjs/common` package.

## Exception Filters
While the base (built-in) exception filter can automatically handle many 
cases for you, you may want full control over the exceptions layer.
Exception filters are designed for exactly this purpose. They let you 
control the exact flow of control and the content of the response sent back
to the client.
