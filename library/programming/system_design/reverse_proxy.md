# Reverse Proxy (Web Server)
Is a web server that centralizes internal services and provides unified interfaces to the public.

Requests from clients are forwarded to a server that can fulfill it before the reverse proxy returns the server's response to the client.

## Additional benefits
- **Increased security** - Hide information about backend servers, blacklist IPs, limit number of connections per client
- **Increased scalability and flexibility** - Clients only see the reverse proxy's IP, allowing you to scale servers or change their configuration
- **SSL termination** - Decrypt incoming requests and encrypt server responses so backend servers do not have to perform these potentially expensive operations
    - Removes the need to install X.509 certificates on each server
- **Compression** - Compress server responses
- **Caching** - Return the response for cached requests
- **Static content** - Serve static content directly
    - HTML/CSS/JS
    - Photos
    - Videos
    - Etc
### Disadvantage(s): reverse proxy
- Introducing a reverse proxy results in increased complexity.
- A single reverse proxy is a single point of failure, configuring multiple reverse proxies (ie a [failover](availability-patterns.md##Fail-Over)) further increases complexity.