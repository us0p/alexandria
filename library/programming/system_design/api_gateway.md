# API Gateway
Is a server that acts as an intermediary between clients (such as web or mobile apps) and backend services (like microservices). It receives API requests, routes them to the appropriate service, aggregates responses if needed, and sends the final response back to the client.
## Capabilities
- **Request routing**: Directs requests to appropriate microservices.
- **Load balancing**: Distributes traffic evenly across services.
- **Authentication & authorization**: Verifies identity and access rights.
- **Rate limiting & throttling**: Controls traffic to prevent overload.
- **Response transformation**: Modifies responses before returning to clients.
- **Logging & monitoring**: Captures data for observability and debugging.
## Benefits
- **Centralized Access Control**: Security (e.g., OAuth2, JWT) is managed in one place, not duplicated across services.
- **Simplified Client Interface**: Clients interact with one endpoint rather than multiple service endpoints.
- **Reduced Client Complexity**: The gateway can aggregate responses from multiple services into one, saving clients from managing that logic.
- **Improved Security**: Hides internal service details and protects against common attacks (e.g., DoS, SQL injection) with features like WAF (Web Application Firewall).
- **Load Management**: Supports rate limiting, caching, and throttling to improve performance and availability.
- **Monitoring and Analytics**: Act's as a single point of entry for a collection of services.
## Drawbacks
- **Single Point of Failure**: If the gateway goes down, all communication between clients and services can fail. Requires high availability setup.
- **Increased Latency**: Adds an extra hop in the request chain, which may slightly slow down response times.
- **Complexity**: Adds infrastructure that needs to be maintained, configured, and scaled.
- **Tight Coupling**: If not properly designed, it may create a bottleneck or tightly couple services and clients to the gateway logic.
- **Deployment Overhead**: Requires careful versioning and deployment strategies to manage changes in APIs across different services.
## Common Solutions
- [Kong](https://konghq.com/)
- [AWS API Gateway](https://aws.amazon.com/pt/api-gateway/)

![[Pasted image 20250702164751.png]]