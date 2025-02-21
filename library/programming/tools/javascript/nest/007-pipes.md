# Pipes
A pipe is a class annotated with the `@Injectable()` decorator, which 
implements the `PipeTransform` interface.

Pipes have two typical use cases:
- transformation: transform input data to the desired form (e.g., from 
  string to integer) 
- validation: evaluate input data and if valid, simply pass it through 
  unchanged; otherwise, throw an exception

In both cases, pipes operate on the arguments being processed by a 
controller route handler. Nest interposes a pipe just before a method is 
invoked, and the pipe receives the arguments destined for the method and 
operates on them. Any transformation or validation operation takes place at
that time, after which the route handler is invoked with any (potentially) 
transformed arguments.

Pipes run inside the exceptions zone. This means that when a Pipe throws an
exception it is handled by the exceptions layer.

Nest comes with some pipes available out-of-the-box, they're exported from 
the `@nestjs/common` package.

## Binding pipes
To use a pipe, we need to bind an instance of the pipe class to the 
appropriate context. 
Pipes can be:
- parameter-scoped: validation logic concerns only one specified parameter.
- method-scoped: validation logic concerns to all parameters of the method.
- controller-scoped: validation logic applies to all methods in the 
  controller
- global-scoped: validation logic applies to all controllers in the 
  application.

## Providing defaults
Parse pipes expect a parameter's value to be defined. They throw an 
exception upon receiving `null` or `undefined` values. To allow an endpoint
to handle missing querystring parameter values, we have to provide a 
default value to be injected before the parse pipes operate on these values.
The `DefaultValuePipe` serves that purpose by simply instantiating it 
before the relevant parse pipe.
