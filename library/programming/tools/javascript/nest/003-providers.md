# Providers
Controllers should handle HTTP requests and delegate more complex tasks to 
providers.
Providers are plain JavaScript classes that are declared as `providers` in 
a NestJS module.

To create a provider we define the `@Injectable()` decorator at the class 
level.

The `@Injectable()` decorator attaches metadata, which declares that 
the given class can be managed by the Nest `IoC` container.
Nest has a built-in inversion of control (IoC) container that resolves 
relationships between providers.

Providers are injected through the class constructor. The use of the
`private` syntax is a shorthand that allow us to both declare and 
initialize the provider class member immediately in the same location.

```typescript
import { Controller, Get } from '@nestjs/common';

@Controller()
export class ControllerClass {
  constructor(private provider: ProviderClass) {}

  @Get()
  async findAll(): Promise<any[]> {
    return this.provider.findAll();
  }
}
```

## Property-based injection
The technique we've used is called constructor-based injection, as 
providers are injected via the constructor method.
In some very specific cases, property-based injection might be useful.
For instance, if your top-level class depends on either one or multiple 
providers, passing them all the way up by calling `super()` in sub-classes 
from the constructor can be very tedious, In order to avoid this, you can 
use the `@Inject()` decorator at the property level.

```typescript
import { Injectable, Inject } from "@nestjs/common";

@Injectable()
export class HttpService<T> {
    @Inject('HTTP_OPTIONS')
    private readonly httpClient: T;
}
```

> If your class doesn't extend another class, you should always prefer 
using constructor-based injection.

## Provider registration
It's done by editing the module file and adding the service to the 
`providers` array of the `@Module()` decorator.
