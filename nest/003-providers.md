# Providers
Are a fundamental concepts in Nest. Many of the basic Nest classes may be 
treated as a provider. The main idea of a provider is that it can be 
injected as a dependency; this means objects can create various 
relationships with each other, and the function of "wiring up" these 
objects largely be delegated to the Nest runtime system.

!["providers"](https://docs.nestjs.com/assets/Components_1.png)

Controllers should handle HTTP requests and delegate more complex tasks to 
providers.
Providers are plain JavaScript classes that are declared as `providers` in 
a NestJS module.

To create a provider we define the `@Injectable()` decorator at the class 
level.

```typescript
//cats.service.ts
import { Injectable } from "@nestjs/common";
import { Cat } from "./interfaces/cat.interface";

export type Cat = {
    name: string;
    age: number;
    breed: string;
}

@Injectable()
export class CatsService {
    private readonly cats: Cat[] = [];

    create(cat: Cat) {
        this.cats.push(cat);
    }

    findAll(): Cat[] {
        return this.cats;
    }
}
```

The `@Injectable()` decorator attaches metadata, which declares that 
`CatsService` is a class that can be managed by the Nest `IoC` container.
Nest has a built-in inversion of control (IoC) container that resolves 
relationships between providers.

```typescript
//cats.controller.ts
import { Controller, Get, Post, Body } from '@nestjs/common';
import { CreateCatDto } from './dto/create-cat.dto';
import { CatsService } from './cats.service';
import { Cat } from './interfaces/cat.interface';

@Controller('cats')
export class CatsController {
  constructor(private catsService: CatsService) {}

  @Post()
  async create(@Body() createCatDto: CreateCatDto) {
    this.catsService.create(createCatDto);
  }

  @Get()
  async findAll(): Promise<Cat[]> {
    return this.catsService.findAll();
  }
}

```

The `CatsService` is injected through the class constructor. The use of the
`private` syntax is a shorthand that allow us to both declare and 
initialize the `catsService` member immediately in the same location.
In the example above, Nest will resolve the `catsService` by creating and 
returning an instance of `CatsService` (or, in the normal case of a 
singleton, returning the existing instance if it has already been requested
elsewhere). This dependency is resolved and passed to your controller's 
constructor (or assigned to the indicated property).

## Optional providers
Occasionally, you might have dependencies which do not necessarily have to 
be resolved.
To indicate a provider is optional, use the `@Optional()` decorator in the 
constructor's signature.

```typescript
import { Injectable, Optional, Inject } from '@nestjs/common';

@Injectable()
export class HttpService<T> {
  constructor(@Optional() @Inject('HTTP_OPTIONS') private httpClient: T) {}
}

```

In the example above we are using a custom provider, which is the reason we
include the `HTTP_OPTIONS` custom token.

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

```typescript
import { Module } from "@nestjs/common";
import { CatsController } from "./cats/cats.controller";
import { CatsService } from "./cats/cats.service";

@Module({
    controllers: [CatsController],
    providers: [CatsService],
})
export class AppModule{}
```

Nest will now be able to resolve the dependencies of the `CatsController` 
class.
