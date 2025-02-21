## Swarm service networks
A docker swarm generates two different kinds of traffic:
- Control and management plane traffic: This includes swarm management 
  messages, such as requests to join or leave the swarm. This traffic is 
  always encrypted.
- Application data plane traffic: This includes container traffic and 
  traffic to and from external clients.

## Key network concepts
- Overlay networks manage communications among the Docker daemons 
  participating in the swarm.
- The ingress network is a special overlay network that facilitates load 
  balancing among a service's nodes. When any swarm node receives a request
  on a published port, it hands that request off to a module called IPVS. 
  IPVS keeps track of all the IP addresses participating in that service, 
  selects one of them, and routes the request to it, over the ingress 
  network.
- The docker_gwbridge is a bridge network that connects the overlay 
  networks (including the ingress network) to an individual Docker daemon's
  physical network. By default, each container a service is running is 
  connected to its local Docker daemon host's docker_gwbridge network.

## Firewall considerations
Docker daemons participating in a swarm need the ability to communicate 
with each other over the following ports:
- Port 7946 TCP/UDP for container network discovery.
- Port 4789 UDP (configurable) for the overlay network (including ingress) 
  data path.
When setting up networking in a Swarm, special care should be taken.

Swarm services connected to the same overlay network effectively expose all
ports to each other. For a port to be accessible outside of the service, 
that port must be published.

## Overlay networking
When you initialize a swarm or join a Docker host to an existing swarm, two
new networks are created on that Docker host:
- An overlay network called `ingress`, which handles the control and data 
  traffic related to swarm services.
- A bridge network called `docker_gwbridge`, which connects the individual 
  Docker daemon to other daemons participating in the swarm.

## Routing mesh
All nodes participate in an ingress routing mesh. The routing mesh enables 
each node in the swarm to accept connections on published ports for any 
service running in the swarm, even if there's no task running on the node. 
The routing mesh routes all incoming requests to published ports on 
available nodes to an active container.
You must also open the published port between the swarm nodes and any 
external resources, such as an external load balancer, that require access 
to the port.
Effectively, Docker acts as a load balancer for your swarm services.
You can also bypass the routing mesh for a given service.

You can configure an external load balancer for swarm services, either in 
combination with the routing mesh or without using the routing mesh at all.

The routing mesh listens on the published port for any IP address assigned 
to the node. For externally routable IP addresses, the port is available 
from outside the host. For all other IP addresses the access is only 
available from within the host.

!["Routing mesh explanation"](https://docs.docker.com/engine/swarm/images/ingress-routing-mesh.webp)

## Publish ports
When you create a swarm service, you can publish that service's ports to 
hosts outside the swarm in two ways:
- You can rely on the routing mesh. When you publish a service port, the 
  swarm makes the service accessible at the target port on every node, 
  regardless of whether there is a task for the service running on that 
  node or not. This is less complex and is the right choice for many types 
  of services.
- You can publish a service task's port directly on the swarm node where 
  that service is running. This bypasses the routing mesh and provides the 
  maximum flexibility, including the ability for you to develop your own 
  routing framework. However, you are responsible for keeping track of 
  where each task is running and routing requests to the tasks, and 
  load-balancing across the nodes.

## Connect the service to an overlay network
You can use overlay networks to connect one or more services within the 
swarm.
After you create an overlay network in swarm mode, all manager nodes have 
access to the network.
You can create a new service and pass the `--network` flag to attach the 
service to the overlay network.
The swarm extends the overlay network to each node running the service.

## Load Balancing
The swarm manager uses ingress load balancing to expose the services you 
want to make available externally to the swarm. The swarm manager can 
automatically assign the service a published port or you can configure a 
published port for the service. You can specify any unused port. If you do 
not specify a port, the swarm manager assigns the service a port in the 
30000-32767 range.

External components, such as cloud load balancers, can access the service 
on the published port of any node in the cluster whether or not the node is
currently running the task for the service. All nodes in the swarm route 
ingress connections to a running task instance.

Swarm mode has an internal DNS component that automatically assigns each 
service in the swarm a DNS entry. The swarm manager uses internal load 
balancing to distribute requests among services within the cluster based 
upon the DNS name of the service.

