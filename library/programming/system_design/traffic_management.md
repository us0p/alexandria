There are 3 main web components that are used to manage traffic and load in web applications:
- [Reverse Proxies](reverse_proxy.md)
- [Load Balancers](load_balancer.md)
- [API Gateways](api_gateway.md)

Those components can be used together to build web applications.

## AWS Microservice Example
Employs API Gateways and Load Balancers together.

API Gateway provide a unified front for client applications sending traffics based on routes to different backed services.

Each of each is fronted by an load balancer, which allows for individual service scaling.

![[Pasted image 20250702165626.png]]
## Load Balancer + Reverse Proxy
Typically a reverse proxy works well for single services or services with little work load but when you need to scale you'll want to use a reverse proxy with a load balancer depending on the use case and requirements you'll need to fulfill.

Usually you'll have a load balancer that splits the load among two or more reverse proxy + servers replicas while the reverse proxy takes care of headers, session and service routing.

```plaintext
               +----------------------+
               |    Load Balancer     |
               +----------------------+
                  |                 |
         +--------+------+     +----+----------+
         | ReverseProxy1 |     | ReverseProxy2 |
         +--------+------+     +----+----------+
              |  |                  |       |
       +------+  +------+    +------+       +------+
       | App1 |  | App2 |    | App1 |       | App2 |
       +------+  +------+    +------+       +------+

```