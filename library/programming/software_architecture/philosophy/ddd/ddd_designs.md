## Strategic Design
Overview of the domain on a higher level.

Usually the first step in ddd, used to understand what are the business needs

Encompasses the problem space, it's used to define what is the problem the application is trying to solve. Thus we're only talking about the problems and not about the solutions.

Has responsibility over:
- Knowledge discovery using approaches like Event Storming or Event Modeling.
- Ubiquitous Language
- Domain Analysis, definition of core subdomains, supporting subdomain and generic subdomains.

The goal is to define a common ground were everyone involved understand the problem you're trying to resolve, uses the same language in discussions and in the code and have a clear understanding of the core domains of your application.
## Tactical Design
Overview of the domain on a lower level. It's close to the code.

It lives in the solution space, it's used to define how we're going to solve the problem we highlighted during the Strategic Design.

For that, it uses concepts like:
- Bounded Context
- Entity
- Aggregates
- Value Objects
- Domain Events
- Domain & Application Services