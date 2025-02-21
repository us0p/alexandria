# Microservices Architecture
Is an application as a set of independently deployable, loosely coupled, 
components, a.k.a. services. Each service consists of one or more 
subdomains and is owned by the team (or teams) that owns the subdomains.
In order to be independently deployable each service typically has its own 
source code repository and its own deployment pipeline, which builds, tests
and deploys the service.
Some system operations will be local (implemented by a single service), 
while others will be distributed across multiple services. A distributed 
operation is implemented using either synchronously using a protocol such 
as HTTP/REST or asynchronously using a message broker.

Benefits
- Simple services - each service consists of a small number of subdomains,
  possibly just one - and so is easier to understand and maintain.
- Team autonomy - a team can develop, test and deploy their service 
  independently of other teams.
- Fast deployment pipeline - each service is fast to test since it’s 
  relatively small, and can be deployed independently.
- Support multiple technology stacks - different services can use different
  technology stacks and can be upgraded independently.
- Segregate subdomains by their characteristics - subdomains can be 
  segregated by their characteristics into separate services in order to 
  improve scalability, availability, security etc.

Drawbacks
- Some distributed operations might be complex, and difficult to understand
  and troubleshoot.
- Some distributed operations might be potentially inefficient.
- Some operations might need to be implemented using complex, eventually 
  consistent (non-ACID) transaction management since loose coupling 
  requires each service to have its own database.
- Some distributed operations might involve tight runtime coupling between 
  services, which reduces their availability.
- Risk of tight design-time coupling between services, which requires time 
  consuming lockstep changes.

When to use
There are two key issues that you must address. The first issue is whether 
to use the monolithic or microservice architecture. And then, if you choose
to use the microservice architecture, the next key challenge is to define a
good service architecture. You must avoid (or at least minimize) the 
potential drawbacks: complex, inefficient interactions; complex eventually 
consistent transactions; and tight runtime coupling.

Assemblage, is an architecture definition process that uses the dark energy
and dark matter forces to group the subdomains in a way that results in 
good microservice architecture.

