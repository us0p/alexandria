# Availability vs Consistency
In distributed systems, you can only support two of the following guarantees:
- **Consistency**: Every read receives the most recent write or an error.
- **Availability**: Every request receives a response, without guarantee that it contains the most recent version of the information.
- **Partition Tolerance**: The system continues to operate despite arbitrary partitioning due to network failures.

Networks aren't reliable, so you'll need to support partition tolerance.
- **CP** - Consistency and Partition tolerance: Waiting for a response from the partitioned node might result in a timeout error. CP is a good choice if your business needs atomic read and writes.
- **AP** - Availability and Partition tolerance: Responses return the most readily available version of the data available on any node, which might not be the latest. Writes might take some time to propagate when the partition is resolved. AP is a good choice if the business needs to allow for eventual consistency or when the system needs to continue working despite external errors.