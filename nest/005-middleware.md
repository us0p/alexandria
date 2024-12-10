# Middlware
Is a function which is called before the route handler. Middleware 
functions have access to the `request` and `response` objects, and the 
`next` middleware function in the application's request-response 
cycle. The next middleware function is commonly denoted by a variable named
`next`
Nest middlware are, by default, equivalent to `express` middleware.

You implement custom Nest middleware in either a function, or in a class 
with an `@Injectable()` decorator. The class should implement the 
`NestMiddleware` interface, while the function does not have any special 
requirements.

```typescript
import { Injectable, NestMiddleware } from "@nestjs/common";
import { Request, Response, NextFunction } from "express";

@Injectable()
export class LoggerMiddleware implements NestMiddleware {
    use(req: Reqeust, res: Response, next: NextFunction) {
        console.log("Request...");
        next();
    }
}
```

> Nest middleware fully supports Dependency Injection.

## Applying middleware
Middlewares are set ussing the `configure()` method of the module class.
Modules that include middleware have to implement the `NestModule` 
interface.

```typescript
import { Module, NestModule, MiddlewareConsumer } from "@nestjs/common";
import { LoggerMiddleware } from "./common/middleware/logger.middleware";
import { CatsModule } from "./cats/cats.module";

@Module({
    imports: [CatsModule],
})
export class AppModule implements NestModule {
    configure(consumer: MiddlewareConsumer) {
        consumer.apply(LoggerMiddleware).forRoutes("cats")
    }
}
```

We have set up the middleware for the `/cats` route handlers that were 
previously defined. We may also further restrict a middleware to a 
particular request method by passing an object containing the route `path` 
and request `method` to the `forRoutes()` method when configuring the 
middleware.

```typescript
import { Module, NestModule, RequestMethod, MiddlewareConsumer } from "@nestjs/common";
import { LoggerMiddleware } from "./common/middleware/logger.middleware";
import { CatsModule } from "./cats/cats.module";

@Module({
    imports: [CatsModule]
})
export class AppModule implements NestModule {
    configure(consumer: MiddlewareConsumer) {
        consumer.apply(LoggerMiddleware).forRoutes({
            path: 'cats',
            method: RequestMethod.GET
        })
    }
}
```

> The `configure()` method can be asynchronous.

> When using the `express` adapter, Nest will register `json` and 
`urlencoded` from the package `body-parser` by default. This means if you 
want to customize that middleware via the `MiddlewareConsumer`, you need to
turn off the global middleware by setting the `bodyParser` flag to `false` 
when creating the application with `NestFactory.create()`.

## Route wildcards
Pattern based routes are supported as well.

> The `fastfy` package uses the latest version of the `path-to-regexp` 
package, which no longer supports wildcard asterisks. Instead you must use 
parameters (e.g., `(.*)`, `:splat*`).

## Middleware consumer
It's a helper class. It provides several built-in methods to manage 
middleware. All of them can be simply chained in the `fluent style`. The 
`forRoutes()` method can take a single string, multiple string, a 
`RouteInfo` object, a controller class and even multiple controller 
classes.
The `apply()` method may either take a single middleware, or multiple 
arguments to specify `multiple middlewares`

```typescript
import { Module, NestModule, MiddlewareConsumer } from '@nestjs/common';
import { LoggerMiddleware } from './common/middleware/logger.middleware';
import { CatsModule } from './cats/cats.module';
import { CatsController } from './cats/cats.controller';

@Module({
  imports: [CatsModule],
})
export class AppModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    consumer
      .apply(LoggerMiddleware)
      .forRoutes(CatsController);
  }
}

```

## Excluding routes
We can easily exclude certain routes with the `exclude()` method. It can 
take a single string, multiple strings, or a `RouteInfo` object identifying
routes to be excluded.
It also supports the wildcard parameters using the `path-to-regexp` 
package.

```typescript
consumer
    .apply(LoggerMiddleware)
    .exclude(
        {path: 'cats', method: RequestMethod.GET},
        {path: 'cats', method: RequestMethod.POST},
        'cats/(.*)'
    )
    .forRoutes(CatsController);
```

`LoggerMiddleware` will be bound to all routes defined inside 
`CatsController` except the three passed to the `exclude()` method.

## Functional Middleware

```typescript
import { Request, Response, NextFunction } from 'express';

export function logger(req: Request, res: Response, next: NextFunction) {
    console.log('Request...');
    next();
}

// in the module file:

consumer
    .apply(logger)
    .forRoutes(CatsController);
```

> Consider using the simpler functional alternative any time your 
middleware doesn't need any dependencies.

You can also provide multiple middleware that are executed sequentially, 
simply by providing a comma separated list inside the `apply()` method.

## Global middleware
If we want to bind middleware to every registered route at once, we can use
the `use()` method that is supplied by the `INestApplication` instance:

```typescript
// main.ts
const app = await NestFactoryyy.create(AppModule);
app.use(logger);
await app.listen(process.env.PORT ?? 3000);
```

> Accessing the DI container in a global middleware is not possible. You 
can use a functional middleware instead when using `app.use()`. 
Alternatively, you can use a class middleware and consume it with 
`.forRoutes('*')` within the `AppModule` (or any other module).
