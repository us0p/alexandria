# Controllers
A controller's purpose is to receive specific requests for the application.
Frequently, each controller has more than one route, and different routes 
can perform different actions.

In order to create a basic controller, we use classes and decorators. 
Decorators associate classes with required metadata and enable Nest to 
create a routing map.

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

Note that even if you use classes, the type will not enforce a scheme on the
payload, you still need to perform validation.

## Getting up and running
Controllers always belong to a module, which is why we include the 
`controllers` array within the `@Module()` decorator.
