# Modules
A module is a class annotated with a `@Module()` decorator. It provides 
metadata that Nest makes use of to organize the application structure.

Each application has at least one module, a root module. The root module is
the starting point Nest uses to build the application graph - The internal 
data structure Nest uses to resolve module and provider relationships and 
dependencies.
Modules are **strongly** recommended as an effective way to organize your 
components. Thus, for most applications, the resulting architecture will 
employ multiple modules, each encapsulating a closely related set of 
capabillities.

The `@Module()` decorator takes a single object whose properties describe 
the module:

- providers: Will be instantiated by the Nest injector and may be shared at
  least across this module.
- controllers: Set of controllers defined in this module which have to be 
  instantiated.
- imports: List of modules that export the providers which are required in 
  this module.
- exports: Subset of `providers` that are provided by this module and 
  should be available in other modules which import this module. You can 
  use either the provider itself or just its token (`provide` value).

The module encapsulates providers by default. This means that it's 
impossible to inject providers that are neither directly part of the 
current module nor exported from the imported modules. Thus, you may 
consider the exported providers from a module as the module's public 
interface, or API.

## Feature module
It simply organizes code relevant for a specific feature, keeping code 
organized and establishing clear boundaries.
For example, the Cat related classes of the previous examples shold be 
moved to its own module, and that module would be responsible for all cat 
related features.

## Shared modules
Modules are singletons by default, and thus you can share the same instance
of any providers between multiple modules effortlessly.
Every module is automatically a shared module. Once created it can be 
reused by any module.
If you want to share an instance of your providers between several other 
modules you need first to export the providers by adding it to the module's
`exports` array.

Now any module that imports this updated module will have access to that 
provider and will share the same instance with all other modules that 
import it as well.

## Module re-exporting
Module can export their internal providers. In addition, they can re-export
modules that they import, thus, making it available for other modules which
import this one.

```typescript
@Module({
    imports: [CommonModule],
    exports: [CommonModule]
})

export class CoreModule{}
```

## Dependency Injection
Module classes can inject providers as well.

```typescript
import { Module } from '@nestjs/common';
import { CatsController } from './cats.controller';
import { CatsService } from "./cats.service";

@Module({
    controllers: [CatsController],
    providers: [CatsService]
})
export class CatsModule {
    constructor(private catsService: CatsService) {}
}
```

However, module classes themselves cannot be injected as providers due to 
`circular dependency`

## Global modules
Nest encapsulates providers inside the modules scope. You aren't able to 
use a module's providers elsewhere without first import the encapsulating 
module.
When you want to provide a set of providers which should be available 
everywhere out-of-the-box, make the module global with the `@Global()` 
decorator.

```typescript
import { Module, Global } from "@nestjs/common";
import { CatsController } from "./cats.controller";
import { CatsService } from "./cats.service";

@Global()
@Module({
    controllers: [CatsController],
    providers: [CatsService],
    exports: [CatsService],
})

export class CatsModule{}
```

The `@Global()` decorator makes the module global-scoped. Global modules 
should be registered only once, generally by the root or core module. In 
the above example, the `CatsService` provider will be ubiquitous, and 
modules that wich to inject the service will not need to import the 
`CatsModule` in their imports array.

## Dynamic modules
It enables you to easily create customizable modules that can register and 
configure providers dynamically.
Following is an example of a dynamic module definition for a 
`DatabaseModule`

```typescript
import { Module, DynamicModule } from '@nestjs/common';
import { createDatabaseProviders } from "./database.providers";
import { Connection } from "./connection.provider";

@Module({
    providers: [Connection],
    exports: [Connection],
})
export class DatabaseModule {
    // this method can be sync or async.,
    static forRoot(entities = [], options?): DynamicModule {
        const providers = createDatabaseProviders(options, entities);
        return {
            module: DatabaseModule,
            providers: providers,
            exports: providers,
            global: true // optional, register the dynamic module to global scope
        }
    }
}
```

This module defines the `Connection` provider by default, but 
additionally - depending on the `entities` and `options` objects passed 
into the `forRoot()` method - exposes a collection of providers. Note that 
the properties returned by the dynamic module extend (rather than override)
the base module metadata defined in the `@Module()` decorator.

The `DatabaseModule` can be imported and configured in the following manner:

```typescript
import { Module } from "@nestjs/common";
import { DatabaseModule } from "./database/database.module";
import { User } from "./users/entities/user.entity";

@Module({
    imports: [DatabaseModule.forRoot([User])],
    exports: [DatabaseModule], // forRoot() isn't required for exporting
})
export class AppModule{}
```

