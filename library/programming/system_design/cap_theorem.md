# CAP Theorem
In a distributed computer system, you can only support two of the following guarantees:
- **Consistency** - Every read receives the most recent write or an error
- **Availability** - Every request receives a response, without guarantee that it contains the most recent version of the information
- **Partition Tolerance** - The system continues to operate despite arbitrary partitioning due to network failures
_Networks aren't reliable, so you'll need to support partition tolerance. You'll need to make a software tradeoff between consistency and availability._
## CP - consistency and partition tolerance
Wait for a response from the partitioned node which could result in a timeout error. The system can also choose to return an error, depending on the scenario you desire. This is going to happen on write operations and it happens to enforce consistency by avoid potential inconsistent data. Choose Consistency over Availability when your business requirements dictate atomic reads and writes.
![[Pasted image 20250622151404.png]]
## AP - availability and partition tolerance
Responses return the most readily available version of the data available on any node, which might not be the latest. Writes might take some time to propagate when the partition is resolved.

AP is a good choice if the business needs to allow for eventual consistency or when the system needs to continue working despite external errors.
![[Pasted image 20250622151529.png]]