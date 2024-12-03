# Controllers
Are responsible for handling incoming requests and returning responses to 
the client.
A controller's purpose is to receive specific requests for the application.
Frequentlyy, each controller has more than one route, and different routes 
can perform different actions.

In order to create a basic controller, we use classes and decorators. 
Decorators associate classes with required metadata and enable Nest to 
create a routing map.

> For quikly creating a CRUD controller with the validation built-in, you 
may use the CLI's CRUD generator: `nest g resource [name]`

## Routing
The `@Controller()` decorator is required to define a basic controller and 
it accepts an optional route path prefix as first parameter. Using a path 
prefix in a `@Controller()` decorator allows us to easily group a set of 
related routes.

```typescript
@Controller('route-these-nuts`)
class CatController {
    @Get()
    findAll(): string {
        return "All cats in the whole world"
    }
}
```

The `@Get()` HTTP request method decorator tells Nest to create a handler 
for a specific endpoint for HTTP requests. The endpoint corresponds to the 
HTTP request method and the route path. The route path of a handler is 
determined by concatenating the optional prefix declared for the 
controller, and any path specified in the method's decorator.

Nest eploys two different options for manipulating responses:
- Standard (recommended): Using this built-in method, when a request 
  handler returns a JavaScript object or array, it will automatically be 
  serialized to JSON. When it returns a JavaScript primitive type, however,
  Nest will send just the value without attempting to serialize it. This 
  makes response handling simple. Furthermore, the response's status code 
  is always 200 by default, except for POST requests which use 201.
- Library-specific: It's alwo possible to use the library-specific 
  (e.g. Express) response object, which can be injected using the `@Res()` 
  decorator in the method handler signature. Whith this approach, you have 
  the ability to use the native resposne handling methods exposed by that 
  object.

> Nest detects when the handler is using either `@Res()` or `@Next()`, 
indicating you have chosen the library-specific option. If both approaches 
are used at the same time, the Standard approach is automatically disabled 
for this single route and will no longer work as expected. To use both 
approaches at the same time (for example, by injecting the response object 
to only set cookies/headers but still leave the rest to the framework), you
must set the `passthrough` option to `true` in the 
`@Res({ passthrough: true })` decorator. 

## Request object
Handlers often need access to the client request details. Nest provides 
access to the request object of the underlying platform. We can access the 
request object by instructing Nest to inject it by adding the `@Req()` 
decorator to the handler's signature.

```typescript
...
@Get()
findAll(@Req() request: Request): string {
    ...
}
...
```

We can also use dedicated decorators intead, such as `@Body()` or `@Query`,
which are available out of the box.
Below is a list of the provided decorators and the plain platform-specific 
objects they represent.

| Decoratos              | Objects                         |
|------------------------|---------------------------------|
| @Request(), @Req()     | req                             |
| @Response(), @Res() *  | res                             |
| @Next()                | next                            |
| @Session()             | req.session                     |
| @Param(key?: string)   | req.params / req.params[key]    |
| @Body(key?: string)    | req.body / req.body[key]        |
| @Query(key? string)    | req.query / req.query[key]      | 
| @Headers(name? string) | req.headers / req.headers[name] |
| @Ip()                  | req.ip                          |
| @HostParam()           | req.hosts                       |

*For compatibilty with typings across underlying HTTP platforms, Nest 
provides `@Res()` and `@Response()` decorators. `@Res()` is simply an alias
for `@Response()`.
When using them, you should also import the typing for the underlying 
library.
Note that when you inject either `@Res()` or `@Response()` in a method 
handler, you put Nest into library-specific mode for that handler, and you 
become responsible for managing the response. When doing so, you must issue
some kind of response by making a call on the `response` object, or the 
HTTP server will hang.

## Resources
