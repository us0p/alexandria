## Nodes
A node is an instance of the Docker engine participating in the swarm. You 
can also think of this as a Docker node. You can run one or more nodes on a
single physical computer or cloud server, but production swarm deployments 
typically include Docker nodes distributed across multiple physical cloud 
machines.

## Manager nodes
Manager nodes perform the orchestration and cluster management functions 
required to maintain the desired state of the swarm, schedule services 
execution between workers and serve the swarm mode HTTP API endpoints.

To deploy your application to a swarm, you submit a service definition to a
manager node. The manager node dispatches units of work called `tasks` to 
worker nodes.

By default manager nodes also run services as worker nodes, but you can 
configure them to run manager tasks exclusively and be manager-only nodes. 

Manager nodes select a single leader to conduct orchestration tasks.

If the manager in a single-manager swarm fails, your services continue to 
run, but you need to create a new cluster to recover.

An odd number `N` of manager nodes in the cluster tolerates the loss of at 
most `(N-1)/2` managers.

Docker recommends a maximum of seven manager nodes for a swarm. Adding more
managers does NOT mean increased scalability or higher performance. In 
general, the opposite is true.

The reason why Swarm mode is using a consensus algorithm is to make sure 
that all the manager nodes that are in charge of managing and scheduling 
tasks in the cluster are storing the same consistent state.
Having the same consistent state across the cluster means that in case of a
failure, any Manager node can pick up the tasks and restore the services to
a stable state.

Raft tolerates up to (N-1)/2 failures and requires a majority or quorum of 
(N/2)+1 members to agree on values proposed to the cluster. This means that
in a cluster of 5 Managers running Raft, if 3 nodes are unavailable, the 
system cannot process any more requests to schedule additional tasks. The 
existing tasks keep running but the scheduler cannot rebalance tasks to 
cope with failures if the manager set is not healthy.

## Worker nodes
Worker nodes receive and execute tasks dispatched from manager nodes.
Worker nodes are also instances of Docker Engine whose sole purpose is to 
execute containers.

You cannot have a worker node without at least one manager node.
By default, all managers are also workers.
You can promote a worker node to be a manager.
An agent runs on each worker node and reports on the tasks assigned to it. 
The worker node notifies the manager node of the current state of its 
assigned tasks so that the manager can maintain the desired state of each 
worker.

- Adding worker nodes increase capacity. When you add workers to your 
  swarm, you increase the scale of the swarm to handle tasks without 
  affecting the manager raft consensus.
- Manager nodes increase fault-tolerance. Among manager noed, a single 
  leader node conducts orchestration tasks. If a leader node goes down, the
  remaining manager node elect a new leader and resume orchestration and 
  maintenance of the swarm state.

!["manager vs worker nodes"](https://docs.docker.com/engine/swarm/images/swarm-diagram.webp)


## Add or remove label metadata
Node labels provide a flexible method of node organization. You can also 
use node labels in service constraints. Apply constraints when you create a
service to limit the nodes where the scheduler assigns tasks for the 
service.

## Node availability
- Active: Swarm manager can assign tasks to any `Active` node.
- Drain: Prevents a node from receiving new tasks from the swarm manager. 
  It also means the manager stops tasks running on the node and launches 
  replica tasks on a node with `Active` availability.
  A node's status, including Drain, only affects the node's ability to 
  schedule swarm service workloads.
  Setting a node to `Drain` does not remove standalone containers from that
  node.

Swarm manager nodes use the Raft Consensus Algorithm to manage the swarm 
state. 
There is no limit on the number of manager nodes. The decision about how 
many manager nodes to implement is a trade-off between performance and 
fault-tolerance. Adding manager nodes to a swarm makes the swarm more 
fault-tolerant. However, additional manager nodes reduce write performance 
because more nodes must acknowledge proposals to update the swarm state.
Raft requires a majority of managers, also called the quorum, to agree on 
proposed updates to the swarm, such as node additions or removals. 
Membership operations are subject to the same constraints as state 
replication.
If the swarm loses the quorum of managers, the swarm cannot perform 
management tasks. If your swarm has multiple managers, always have more 
than two. To maintain quorum, a majority of managers must be available. An 
odd number of managers is recommended, because the next even number does 
not make the quorum easier to keep. For instance, whether you have 3 or 4 
managers, you can still only lose 1 manager and maintain the quorum. If you
have 5 or 6 managers, you can still only lose two.
Even if a swarm loses the quorum of managers, swarm tasks on existing 
worker nodes continue to run. However, swarm nodes cannot be added, 
updated, or removed, and new or existing tasks cannot be started, stopped, 
moved, or updated.
Because manager nodes are meant to be a stable component of the 
infrastructure, you should use a fixed IP address for the advertise address
to prevent the swarm from becoming unstable on machine reboot.

If the whole swarm restarts and every manager node subsequently gets a new 
IP address, there is no way for any node to contact an existing manager. 
Therefore the swarm is hung while nodes try to contact one another at their
old IP addresses.

Dynamic IP addresses are OK for worker nodes.

Distribute manager nodes

In addition to maintaining an odd number of manager nodes, pay attention to
datacenter topology when placing managers. For optimal fault-tolerance, 
distribute manager nodes across a minimum of 3 availability-zones to 
support failures of an entire set of machines or common maintenance 
scenarios.

Run manager-only nodes
By default manager nodes also act as a worker nodes. This means the 
scheduler can assign tasks to a manager node. For small and non-critical 
swarms assigning tasks to managers is relatively low-risk as long as you 
schedule services using resource constraints for cpu and memory.

However, because manager nodes use the Raft consensus algorithm to 
replicate data in a consistent way, they are sensitive to resource 
starvation. You should isolate managers in your swarm from processes that 
might block swarm operations like swarm heartbeat or leader elections.
To avoid interference with manager node operation, you can drain manager 
nodes to make them unavailable as worker nodes

An unreachable health status means that this particular manager node is 
unreachable from other manager nodes. In this case you need to take action 
to restore the unreachable manager:
- Restart the daemon and see if the manager comes back as reachable.
- Reboot the machine.
- If neither restarting nor rebooting works, you should add another manager
  node or promote a worker to be a manager node. You also need to cleanly 
  remove the failed node entry from the manager set with docker node demote
  <NODE> and docker node rm <id-node>.

You should never restart a manager node by copying the raft directory from 
another node. The data directory is unique to a node ID. A node can only 
use a node ID once to join the swarm. The node ID space should be globally 
unique.
