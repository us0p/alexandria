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

| Decoratos               | Objects                         |
|-------------------------|---------------------------------|
| @Request(), @Req()      | req                             |
| @Response(), @Res() *   | res                             |
| @Next()                 | next                            |
| @Session()              | req.session                     |
| @Param(key?: string)    | req.params / req.params[key]    |
| @Body(key?: string)     | req.body / req.body[key]        |
| @Query(key? string)     | req.query / req.query[key]      | 
| @Headers(name? string)  | req.headers / req.headers[name] |
| @Ip()                   | req.ip                          |
| @HostParam(key? string) | req.hosts                       |

*For compatibilty with typings across underlying HTTP platforms, Nest 
provides `@Res()` and `@Response()` decorators. `@Res()` is simply an alias
for `@Response()`.
When using them, you should also import the typing for the underlying 
library (like in the example above).
Note that when you inject either `@Res()` or `@Response()` in a method 
handler, you put Nest into library-specific mode for that handler, and you 
become responsible for managing the response. When doing so, you must issue
some kind of response by making a call on the `response` object, or the 
HTTP server will hang.

## Resources
Nest provides decorators for all of the standard HTTP methods:
- `@Get()`
- `@Post()`
- `@Put()`
- `@Delete()`
- `@Patch()`
- `@Options()`
- `@Head()`

In addition, `@All()` defines an endpoint that handles all of them.

## Route wildcards
Pattern based routes are supported as well. For instance, the asterisk is 
used as a wildcard, and will match any combination of characters.

```typescript
@Get('ab*cd')
findAll() {
    return 'This route uses a wildcard';
}
```

The characters `?`, `+`, `*`, and `()` may be used in a route path, and are
subsets of their regular expression counterparts. The hyphen `-` and the 
dot `.` are interpreted literally by string-based paths.

> Wildcard in the middle of the route is only supported by express.

## Status Code
We can change the status code returned by the handle by adding the 
`@HttpCode()` decorator at a handler level.

```typescript
import {HttpCode, Post} from '@nestjs/common'

@Post()
@HttpCode(204)
create() {
    return 'This action adds a new cat';
}
```

If you need to provide a dynamic status code, you can use a 
library-specific response object (inject using `@Res()`) (or, in case of an
error, throw an exception).

## Headers
To specify a custom response header, you can either use a `@Header()` 
decorator or a library-specific response object.

```typescript
import {Post, Header} from '@nestjs/common'

@Post()
@Header('Cache-Control', 'no-store')
create() {
    return 'This action adds a new cat';
}
```

## Redirection
To redirect a response to a specific URL, you can either use a 
`@Redirect()` decorator or a library-specific response object.
`@Redirect()` takes two arguments, `url`, and `statusCode`, both are 
optional. The default value of `statusCode` is `302`.

```typescript
import {Get, Redirect} from '@nestjs/common';

@Get()
@Redirect('https://nestjs.com', 301)
```

> Sometimes you may want to determine the HTTP status code or the redirect 
URL dynamically. Do this by returning an object following the 
`HttpRedirectResponse` interface from `@nestjs/common`.

Returned values will override any arguments passed to the `@Redirect()` 
decorator

```typescript
import {Get, Redirect} from '@nestjs/common';

@Get('docs')
@Redirect('https://docs.nestjs.com', 302)
getDocs(@Query('version') version) {
    if (version && version === '5') {
        return {url: 'https://docs.nestjs.com/v5/'};
    }
}
```

## Route parameters
In order to define routes with parameters, we can add route parameter 
tokens in the path of the route to capture the dynamic value at that 
position in the request URL. The route parameter token in the `@Get()` 
decorator example below demonstrates this usage. Route parameters declared 
in this way can be accessed using the `@Param()` decorator, which should be
added to the method signature.

> Routes with parameters should be declared after any static paths. This 
prevents the parameterized paths from intercepting traffic destined for the
static paths.

```typescript
@Get(':id')
findOne(@Param() params: any): string {
    console.log(params.id);
    return `This action returns a #${params.id} car`;
}
```

## Sub-Domain Routing
The `@Controller` decorator can take a `host` option to require that the 
HTTP host of the incoming request matches some specific value.

> Since Fastfy lacks support for nested routers, when using sub-domain 
routing, the Express adapter should be used instead.

```typescript
import {Controller, Get} from '@nesjs/common';

@Controller({host: 'admin.example.com'})
export class AdminController {
    @Get()
    index(): string {
        return 'Admin page';
    }
}
```

Similar to a route `path`, the `hosts` option can use tokens to capture the
dynamic value at that position in the host name. Host parameters declared 
in this way can be accessed using the `@HostParam()` decorator:

```typescript
@Controller({ host: `:account.example.com` })
export class AccountController {
    @Get()
    getInfo(@HostParam('account') account: string) {
        return account;
    }
}
```

## Asynchronicity
Nest is able to resolve promises by itself:

```typescript
import {Get} from '@nestjs/common'

@Get()
async findAll(): Promise<any[]> {
    return [];
}
```

Nest route handlers are able to return RxJS observable streams. Nest will 
automatically subscribe to the source underneath and take the last emitted 
value (once the stream is completed).

```typescript
import {Get} from '@nestjs/common';

@Get()
findAll(): Observable<any[]> {
    return of([]);
}
```

## Request Payloads
The expected payload of a request must have a predefined schema which is 
usually a `DTO`. We could determine the DTO by using Typescrit interfaces, 
or by simple classes. The recommended way in Nest is by using classes, 
because they are part of the JS ES6 standard, and therefore they are 
preserved as real entities in the compiled JS. Typescript interface are 
removed durint the transpilation, Nest can't refer to them at runtime. This
is important because features such as Pipes enable additional possibilities
when they have access to the metatype of the variable at runtime.

```typescript
import {Post, Body} from '@nestjs/common';

class CreateCatDto {
    name: string;
    age: number;
    breed: string;
}

@Post()
async create(@Body() createCatDto: CreateCatDto) {
    return 'This action adds a new cat';
}
```

Note that even if you use classes, the type will not enforce a schme on the
payload, you still need to perform validation.

## Getting up and running
Controllers always belong to a module, which is why we include the 
`controllers` array within the `@Module()` decorator. If you scaffolded 
your project with NestCLI, your project should have one module, 
`AppModule` defined in `app.module.ts`.

```typescript
import {Module} from '@nestjs/common';
import {CatsController} from "./cats/cats.controller';

@Module({
        controllers: [CatsController],
})
export class AppModule {}
```

By doing this we attached the metadata to the module class using the 
`@Module()` decorator.

## Library-specific approach
Note that when in this mode your handlers lose compatibility with Nest 
features that depend on Nest standard response handling, such as 
interceptors and `@HttpCode()` / `@Header()` decorators, To fix this, you 
can set the `passthrough` option.
