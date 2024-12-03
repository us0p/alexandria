# Nest.js
Is a framework for building efficient, scalable Node.js server-side 
applications.
It combines elements of OOP, FP, and FRP (Functional Reactive Programming).
Under the hood, Nest makes use of robust HTTP server frameworks like 
Express (default) and optionally can be configured to use Fastify as well.
Nest provides a level of abstraction above these common Node.js frameworks,
but also exposes their API directly to the developer.

## Philosophy
While plenty of superb libraries, helpers, and tools exist for Node, none 
of them effectively solve the main problem of `Architecture`.
Nest provides an out-of-the-box application architecture which allows 
developers and teams to create highly testable, scalable, loosely coupled, 
and easily maintainable applications. The architecture is heavily inspired 
by Angular.

## Installation - NestCLI
```bash
npm i -g @nestjs/cli
nest new <project-name>
```

This command should create a folder with `<project-name` with the following
files

```plaintext
src
|-app.controller.spect.ts
|-app.controller.ts
|-app.module.ts
|-app.service.ts
|-main.ts
```

Here's a brief overview of those core files:
- `app.controller.ts`: A basic controller with a single route.
- `app.controller.spec.ts`: The unit tests for the controller.
- `app.module.ts`: The root module of the application.
- `app.service.ts`: A basic service with a single method.
- `main.ts`: The entry file of the application which uses the core function
  `NestFactory` to create a Nest application instance.

`main.ts` defines an async function, which will bootstrap the application.
`NestFactory` exposes a few static methods that allow creating an 
application instance. The `create()` method returns an application object, 
which fulfills the `INestApplication` interface.

Note that a project scaffolded with the NestCLI creates an initial project 
structure that encourages developers to follow the convention of keeping 
each module in its own dedicated directory.

> By default, if any error happens while creating the application your app 
will exit with the code 1. If you want to make it throw an error instead 
disable the option `abortOnError`.

## Platform
Nest aims to be a platform-agnostic framework. Technically, Nest is able to
work with an Node HTTP framework once an apdapter is created. The platforms
supported out-of-the-box are:
- Expess
- Fastfy
Whichever platform is used, it exposes its own application interface. These
are seen respectively as `NestExpressApplication` and 
`NestFastifyApplication`.
When you pass a type to `NestFactory.create()` method, as in the example 
below, the returned object will have methods available exclusively for that
specific platform. Note, however, you don't need to specify a type unless 
you actually want to access the underlying platform API.
```typescript
const app = await NestFactory.create<NestExpressApplication>(AppModule);
```

> To speed up the development process (x20 times faster builds), you can 
use the SWC builder by passing the `-b swc` (require package `@swc/cli` 
installed as a development dependency) flag to the `start` script, as 
follows `npm start -- -b swc`.

> In order to take advantage of `express` typing, install `@types/express` 
package.

To watch for changes in your files, you can run the following command to 
start the application:
```bash
npm run start:dev
```

## Linting and formatting
A generated Nest project comes with both a code linter and formatter preinstalled,
`eslint` and `prettier`.
For headless environments where an IDE is not relevant (Continuous Integration, Git hooks, etc.) a Nest project comes with ready-to-use `npm` scripts.
```bash
# Lint and autofix with eslint
npm run list

# Format with prettier
npm run format
```
