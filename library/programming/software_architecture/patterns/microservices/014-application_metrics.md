Application Metrics

Problem
How to understand the behavior of an application and troubleshoot problems?

Solution
Instrument a service to gather statistics about individual operations. 
Aggregate metrics in centralized metrics service, which provides reporting 
and alerting. There are two models for aggregating metrics:
- push - the service pushes metrics to the metrics service.
- pull - the metrics services pulls metrics from the service>

Some example of tools that provide this implementation are:
- Prometheus.
- AWS Cloud Watch.

Benefits
- It provides deep insight into application behavior.

Drawbacks
- Metrics code is intertwined with business logic making it more 
  complicated.
- Aggregating metrics can require significant infrastructure.
