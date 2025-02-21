API Composition
You have applied the Microservices architecture pattern and the Database 
per service pattern. As a result, it is no longer straightforward to 
implement queries that join data from multiple services.

Problem
How to implement queries in a microservice architecture?

Solution
Implement a query by defining an API Composer, which invoking the services 
that own the data and performs an in-memory join of the results.

Benefits
- It a simple way to query data in a microservice architecture.

Drawbacks
- Some queries would result in inefficient, in-memory joins of large 
  datasets.
