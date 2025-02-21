# Swarm
Is an advanced feature for managing a cluster of Docker daemons.
Current versions of Docker include Swarm mode for natively managing a 
cluster of Docker Engines called a swarm.
Use the Docker CLI to create a swarm, deploy application services to a 
swarm, and manage swarm behavior.

The cluster management and orchestration features embedded in Docker Engine
are built using `swarmkit`. Swarmkit is a separate project which implements
Docker's orchestration layer and is used directly within Docker.

> Docker Swarm mode isn't the same as the Docker Classic Swarm which is no 
  longer actively developed.

A swarm consists of multiple Docker hosts which run in Swarm mode.

A host can be a manager, and manage membership and delegation of tasks.
A worker, which run swarm services tasks.

A given Docker host can be a manager, a worker, or perform both roles.

When you create a service, you define its optimal state - number of 
replicas, network and storage resources available to it, ports 
the service exposes to the outside world, and more.

A task is a running container which is part of a swarm service and is 
managed by a swarm manager, as opposed to a standalone container.

When Docker is running in Swarm mode, you can still run standalone 
containers on any of the Docker hosts participating in the swarm, as well 
as swarm services.

A key difference between standalone containers and swarm services is that 
only swarm managers can manage a swarm, while standalone containers can be 
started on any daemon. 

In the same way that you can use Docker Compose to define and run 
containers, you can define and run Swarm service stacks.

## Wiring up swarm nodes
If you want to deploy more than one node, they need to be accessible by 
network.

The IP address of the manager node must be assigned to a network interface 
available to the host operating system in the manager node. All nodes in 
the swarm need to connect to the manager at the IP address.

Because other nodes contact the manager node on its IP address, you should 
use a fixed IP address.

The following ports must be available. On some systems, these ports are 
open by default.
- Port `2377` TCP for communication with and between manager nodes
- Port `7946` TCP/UDP for overlay network node discovery
- Port `4789` UDP (configurable) for overlay network traffic. Also known as
  VXLAN port.

Port 4789 is the default value for the Swarm data path port. It is 
important to prevent any untrusted traffic from reaching this port, as 
VXLAN does not provide authentication. This port should only be opened to a
trusted network, and never at a perimeter firewall.

To add services to the swarm, the service image needs to be available at a 
public or private repository, it's not possible to use local images.

Once you have deployed a service to a swarm, you are ready to use the 
Docker CLI to scale the number of containers in the service. Containers 
running in a service are called tasks.
