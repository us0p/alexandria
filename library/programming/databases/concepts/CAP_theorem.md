# CAP Theorem - (Consistency, Availability, Partition tolerance)
According to the CAP theorem, any distributed system can only guarantee two
of the three properties at any time. You can't guarantee all three 
properties at once.
In the theorem, partition tolerance is a must. The assumption is that the 
system operates on a distributed data store so the system, by nature, 
operates with network partitions. Network failures will happen, so to offer
any kind of reliable service, partition tolerance is necessary.
Consistency in CAP is different than that of ACID. Consistency in CAP means 
having the most up-to-date information.Also note that availability as 
defined in CAP theorem is different from high availability in software 
architecture.

- Consistency: All clients see the same data at the same time, no matter 
  which node they connect to. For this to happen, whenever data is written 
  to one node, it must be instantly forwarded or replicated to all the 
  other nodes in the system before the write is deemed ‘successful.’
- Availability: Any client making a request for data gets a response, even 
  if one or more nodes are down. Another way to state this — all working 
  nodes in the distributed system return a valid response for any request, 
  without exception.
- Partition tolerance: A partition is a communication break within a 
  distributed system — a lost or temporarily delayed connection between two
  nodes. Partition tolerance means that the cluster must continue to work 
  despite any number of communication breakdowns between nodes in the 
  system.

NoSQL databases are ideal for distributed network applications. Unlike 
their vertically scalable SQL (relational) counterparts, NoSQL databases 
are horizontally scalable and distributed by design—they can rapidly scale 
across a growing network consisting of multiple interconnected nodes.

> The modern CAP goal should be to maximize combinations of consistency and 
availability that make sense for the specific application. Such an approach 
incorporates plans for operation during a partition and for recovery 
afterward.
Eric Brewer - Initial positor of the CAP Theorem.

## Proof of the theorem
Assume for contradiction that there does exist a system that is consistent,
available, and partition tolerant. The first thing we do is partition our 
system. It looks like this.

!["alpha 0"](https://mwhittaker.github.io/blog/an_illustrated_proof_of_the_cap_theorem/assets/cap21.svg)

Next, we have our client request that v1 be written to G1. Since our system
is available, G1 must respond. Since the network is partitioned, however, 
G1 cannot replicate its data to G2. Gilbert and Lynch call this phase of 
execution α1.

!["alpha 10"](https://mwhittaker.github.io/blog/an_illustrated_proof_of_the_cap_theorem/assets/cap22.svg)
!["alpha 11"](https://mwhittaker.github.io/blog/an_illustrated_proof_of_the_cap_theorem/assets/cap23.svg)
!["alpha 12"](https://mwhittaker.github.io/blog/an_illustrated_proof_of_the_cap_theorem/assets/cap24.svg)

Next, we have our client issue a read request to G2. Again, since our 
system is available, G2 must respond. And since the network is partitioned,
G2 cannot update its value from G1. It returns v0. Gilbert and Lynch call 
this phase of execution α2.

!["alpha 20"](https://mwhittaker.github.io/blog/an_illustrated_proof_of_the_cap_theorem/assets/cap25.svg)
!["alpha 21"](https://mwhittaker.github.io/blog/an_illustrated_proof_of_the_cap_theorem/assets/cap26.svg)

G2 returns v0 to our client after the client had already written v1 to G1. 
This is inconsistent. We assumed a consistent, available, partition 
tolerant system existed, but we just showed that there exists an execution 
for any such system in which the system acts inconsistently. Thus, no such 
system exists.
