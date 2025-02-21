Distributed Tracing

Problem
You have applied the Microservice architecture pattern. Requests often span
multiple services. Each service handles a request by performing one or more
operations, e.g. database queries, publishes messages, etc.
How to understand the behavior of an application and troubleshoot problems?

Aditional considerations
- External monitoring only tells you the overall response time and number 
  of invocations - no insight into the individual operations.
- Any solution should have minimal runtime overhead.
- Log entries for a request are scattered across numerous logs.

Solution
Instrument services with code that:
- Assigns each external request a unique external request id.
- Passes the external request id to all services that are involved in 
  handling the request.
- Includes the external request id in all log messages.
- Records information (e.g. start time, end time) about the requests and 
  operations performed when handling a external request in a centralized 
  service.

Benefits
- It provides useful insight into the behavior of the system including the 
  sources of latency.
- It enables developers to see how an individual request is handled by 
  searching across aggregated logs for its external request id.

Drawbacks
- Aggregating and storing traces can require significant infrastructure.
