Log Aggregation

Problem
The application consists of multiple services and service instances that 
are running on multiple machines. Requests often span multiple service 
instances.
Each service instance generates writes information about what it is doing 
to a log file in a standardized format. The log file contains errors, 
warnings, information and debug messages.
How to understand the behavior of an application and troubleshoot problems?

Solution
Use a centralized logging service that aggregates logs from each service 
instance. The users can search and analyze the logs. They can configure 
alerts that are triggered when certain messages appear in the logs.
An example is AWS Cloud Watch.

Issues
- handling a large volume of logs requires substantial infrastructure.
