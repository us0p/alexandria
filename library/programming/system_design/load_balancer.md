# Load Balancer
Load balancers distribute incoming client requests to a group of computing resources such as application servers (same services replicated horizontally) and databases.

![[Pasted image 20250702165003.png]]

In each case, the load balancer returns the response from the computing resource to the appropriate client. Load balancers are effective at:
- Preventing requests from going to unhealthy servers
- Preventing overloading resources
- Helping to eliminate a single point of failure

Load balancers can be implemented with hardware (expensive) or with software such as HAProxy.
Load balancers can route traffic based on various metrics, including:

- Random
- Least loaded
- Session/cookies
- [Round robin or weighted round robin](https://www.g33kinfo.com/info/round-robin-vs-weighted-round-robin-lb)
- [Layer 4](https://github.com/donnemartin/system-design-primer?tab=readme-ov-file#layer-4-load-balancing)
- [Layer 7](https://github.com/donnemartin/system-design-primer?tab=readme-ov-file#layer-7-load-balancing)

>To protect against failures, it's common to set up multiple load balancers, either in [active-passive](availability-patterns.md###Active-Passive) or [active-active](availability-patterns.md###Active-Active) mode.
## Additional benefits
- **Automatic Scaling**: In cloud environments, load balancing solutions can provide automatic scaling by dynamically adding or removing services as requests volume fluctuates.
- **SSL termination** - Decrypt incoming requests and encrypt server responses so backend servers do not have to perform these potentially expensive operations
    - Removes the need to install X.509 certificates on each server
- **Session persistence** - Issue cookies and route a specific client's requests to same instance if the web apps do not keep track of sessions
### Disadvantage(s): load balancer
- The load balancer can become a performance bottleneck if it does not have enough resources or if it is not configured properly.
- Introducing a load balancer to help eliminate a single point of failure results in increased complexity.
- A single load balancer is a single point of failure, configuring multiple load balancers further increases complexity.