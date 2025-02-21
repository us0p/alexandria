Exception Tracking

Problem
The application consists of multiple services and service instances that 
are running on multiple machines. Errors sometimes occur when handling 
requests. When an error occurs, a service instance throws an exception, 
which contains an error message and a stack trace.
How to understand the behavior of an application and troubleshoot problems?

Aditional considerations
Exceptions must be de-duplicated, recorded, investigated by developers and 
the underlying issue resolved.

Solution
Report all exceptions to a centralized exception tracking service that 
aggregates and tracks exceptions and notifies developers.

Benefits
- It is easier to view exceptions and track their resolution.

Drawbacks
- The exception tracking service is additional infrastructure.
