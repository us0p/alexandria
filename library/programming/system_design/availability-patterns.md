# Availability Patterns
## Fail-Over
Heartbeats are sent between the active and the passive server on standby.
### Active-Passive
 If the heartbeat is interrupted, the passive server takes over the active's IP address and resumes service.

The length of downtime is determined by whether the passive server is already running in 'hot' standby or whether it needs to start up from 'cold' standby. Only the active server handles traffic.

Can also be referred to as **master-slave** fail-over.
### Active-Active
Both servers are managing traffic, spreading the load between them.

If the servers are public-facing, the DNS would need to know about the public IPs of both servers. If the servers are internal-facing, application logic would need to know about both servers.

Active-active fail-over can also be referred to as master-master fail-over.
### Disadvantages
- Adds more hardware and additional complexity.
- Potential for data loss if the active system fails before any newly written data can be replicated to the passive.
## Replication
### Master-Slave 
The master serves reads and writes, replicating writes to one or more slaves, which serve only reads. Slaves can also replicate to additional slaves in a tree-like fashion. If the master goes offline, the system can continue to operate in read-only mode until a slave is promoted to a master or a new master is provisioned.
#### Disadvantages: Master-Slave replication
- Additional logic is needed to promote a slave to a master.
### Master-Master
Both masters serve reads and writes and coordinate with each other on writes. If either master goes down, the system can continue to operate with both reads and writes.
#### Disadvantages: Master-Master replication
- You'll need a load balancer or you'll need to make changes to your application logic to determine where to write.
- Most master-master systems are either loosely consistent (violating ACID) or have increased write latency due to synchronization.
- Conflict resolution comes more into play as more write nodes are added and as latency increases.
### Disadvantages: replication
- There is a potential for loss of data if the master fails before any newly written data can be replicated to other nodes.
- Writes are replayed to the read replicas. If there are a lot of writes, the read replicas can get bogged down with replaying writes and can't do as many reads.
- The more read slaves, the more you have to replicate, which leads to greater replication lag.
- On some systems, writing to the master can spawn multiple threads to write in parallel, whereas read replicas only support writing sequentially with a single thread.
- Replication adds more hardware and additional complexity.

## Availability in numbers
Availability is often quantified by uptime (or downtime) as a percentage of time the service is available. Availability is generally measured in number of 9s--a service with 99.99% availability is described as having four 9s.
### Availability in parallel vs in sequence
If a service consists of multiple components prone to failure, the service's overall availability depends on whether the components are in sequence or in parallel.
### In Sequence
Overall availability **decreases** when two components with availability < 100% are in sequence.
If two services, both with 99.9% of availability are together in sequence, their both availability would be 99.8%.
### In Parallel
Overall availability **increases** when two components with availability < 100% are in parallel.
If two services, both with 99.9% of availability are together in parallel, their both availability would be 99.9999%.

You can see a table with the number of availability and how to calculate the total availability for services in sequence and in parallel in [here](https://github.com/donnemartin/system-design-primer?tab=readme-ov-file#availability-in-numbers)