# Networking
Container networking refers to the ability for containers to connect to and
communicate with each other, or to non-Docker workloads.

Containers have networking enabled by default, and they can make outgoing 
connections. A container has no information about what kind of network it's 
attached to, or whether their peers are also Docker workloads or not. A 
container only sees a network interface with an IP address, a gateway, a 
routing table, DNS services, and other networking details. That is, unless 
the container uses the `none` network driver.

You can create custom, user-defined networks, and connect multiple 
containers to the same network. Once connected to a user-defined network, 
containers can communicate with each other using container IP addresses or 
container names.

## Drivers
|Driver  |Description                                                               |
|--------|--------------------------------------------------------------------------|
|bridge  |The default network driver                                                |
|host    |Remove network isolation between the container and the Docker host        |
|none    |Completely isolate a container from the host and other containers         |
|overlay |Overlay networks connect multiple Docker daemons together                 |
|ipvlan  |IPvlan networks provide full control over both IPv4 and IPv6 addressing   |
|macvlan |Assign a MAC address to a container                                       |

## Published ports
By default, when you create or run a container using `docker create` or 
`docker run`, containers on bridge networks don't expose any ports to the 
outside world. This creates a firewall rule in the host, mapping a 
container port to a port on the Docker host to the outside world.

Publishing container ports is insecure by default. Meaning, when you 
publish a container's ports it becomes available not only to the Docker 
host, but to the outside world as well.

If you want to make a container accessible to other containers, it isn't 
necessary to publish the container's ports. You can enable inter-container 
communication by connecting the containers to the same network, usually a 
bridge network.

## IP address and hostname
By default, the container gets an IP address for every Docker network it 
attaches to. A container receives an IP address out of the IP subnet of the
network. The Docker daemon performs dynamic subnetting and IP address 
allocation for containers. Each network also has a default subnet mask and 
gateway.

In the same way, a container's hostname defaults to be the container's ID 
in Docker.
