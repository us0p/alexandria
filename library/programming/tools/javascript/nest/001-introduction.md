# Nest.js
Is a framework for building efficient, scalable Node.js server-side 
applications.
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

## Platform
Nest aims to be a platform-agnostic framework. Technically, Nest is able to
work with any Node HTTP framework once an apdapter is created. The 
platforms supported out-of-the-box are:
- Expess
- Fastfy
