Health Check API

Problem
Sometimes a service instance can be incapable of handling requests yet 
still be running. For example, it might have ran out of database 
connections. When this occurs, the monitoring system should generate a 
alert. Also, the load balancer or service registry should not route 
requests to the failed service instance.
How to detect that a running service instance is unable to handle requests?

Aditional considerations
- An alert should be generated when a service instance fails.
- Requests should be routed to working service instances.

Solution
A service has an health check API endpoint (e.g. HTTP /health) that returns
the health of the service. The API endpoint handler performs various 
checks, such as:
- the status of the connections to the infrastructure services used by the 
  service instance.
- the status of the host, e.g. disk space.
- application specific logic.

A health check client - a monitoring service, service registry or load 
balancer - periodically invokes the endpoint to check the health of the 
service instance.

Benefits
- The health check endpoint enables the health of a service instance to be 
  periodically tested.

Drawbacks
- The health check might not be sufficiently comprehensive or the service 
  instance might fail between health checks and so requests might still be 
  routed to a failed service instance.
