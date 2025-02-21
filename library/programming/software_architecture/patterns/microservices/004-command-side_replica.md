Command-Side Replica
You have applied the Microservices architecture pattern and the Database 
per service pattern. As a result, a service that implements a system 
command often needs to query other services.

Problem
How can a service that implements a command retrieve data from another 
service?

Solution
The solution consists of the following elements:
- Command service: the service that implements the command.
- Provider service: the service that owns the data that the command service
  needs.
- Replica database: a read-only replica of the data from the provider 
  service. The command service keeps the replica up to date by subscribing 
  to Domain events published by the provider service.

Benefits
- Support multiple technology stacks: the replica database can use a 
  technology stack that’s more optimized to support the command.
- Segregate by characteristics: the provider service is no longer invoked 
  by the command and so might need to be as performant or available.
- Simple interactions: the command is simpler since it no longer needs to 
  interact with the provider service.
- Efficient interactions: the command is more efficient since it no longer 
  needs to interact with the provider service.
- Prefer ACID over BASE: the replica is potentially stale.
- Minimize runtime coupling: runtime coupling is reduced since the the 
  command no longer needs to interact with the provider service.

Drawbacks
- Simple components: makes the command service more complicated since it 
  needs to maintain the replica. It also complicates the provider service 
  since it must publish the events.
- Team autonomy: the provider service’s team might need to coordinate more 
  frequently with command service team due to increased design-time 
  coupling (see below).
- Fast deployment pipeline: the command service’s deployment pipeline might
  be slower since it needs test the replica.
- Segregate by characteristics: potentially increased since, for example, 
  if the replica database contains regulated data (e.g. PII) then the 
  command service might be more complicated.
- Simple interactions: potentially more complicated since the provider 
  service’s commands must publish events.
- Efficient interactions: potentially less efficient since the provider 
  service might publish a large volume of events.
- Minimize design-time coupling: risk of tight design-time coupling between
  services, since the command service needs to know about the structure of 
  the data that is replicated and potentially its lifecycle events.
