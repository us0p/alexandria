# Reverse Proxy vs Load Balancer
[Reverse Proxies](reverse_proxy.md) and [Load Balancers](load_balancer.md) are very similar technologies.

Reverse proxies can often perform the same work of Load Balancers, so what's the need of the latest?

Although they might use the same technology and perform similar tasks, the distinction between both is in their **roles**.
## Reverse Proxies
Acts like a **receptionist** to **one or more** backend services by routing, transforming and protecting the traffic. Often sits at the **edge** of your infrastructure.
- **Main Goal**: Route or manipulate traffic to backend(s).
- **Use Case**: Protect, optimize, or rewrite traffic.
- **Backends**: One or more.
- **Decision-making**: Based on URL, headers, auth, etc.
## Load Balancers
Acts like a **call center router** to **spread load** across many instance of the **same service** and keeping services available. Handles **heath checks** and **failover**.
- **Main Goal**: Distribute traffic evenly across servers.
- **Use Case**: Scale and ensure availability.
- **Backends**: Always multiple.
- **Decision-making**: Based on load, health, connection count, etc.
## Analogy
Imagine a receptionist at a company:
- **Reverse Proxy** is like the **receptionist**: decides **who you talk to** based on your purpose (sales, support, HR).
- **Load Balancer** is like a **call center router**: sends your call to the **next available agent** in the same department.
Same person (or tool) can do both jobs — but they are fundamentally different **functions**.