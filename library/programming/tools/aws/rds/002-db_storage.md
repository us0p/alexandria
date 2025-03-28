## DB instance storage
All database engines excluding Amazon Aurora use `EBS` volumes for database and log storage.

DB instance storage comes in the following types:
- General Purpose (`SSD`): Ideal for workloads running on medium-sized DB instances. Good for development and testing environments.
- Provisioned `IOPS` (`PIOPS`): designed to meet I/O-intensive workloads which require low I/O latency and consistent I/O throughput. Best suited for production environments.
- Magnetic: supported for backwards compatibility, should use `SSD` or `IOPS SSD` for new storage needs.

Each DB instance has min and max storage requirements depending on the storage type and db engine it supports. It's important to have sufficient storage for db grow and for the db engine to write content or log entries.

[RDS DB instance storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html)
## Provisioned `IOPS SSD` storage
For a production application that requires fast and consistent I/O performance, provisioned `IOPS` storage is recommended. It delivers predictable performance, and consistently low latency. It's optimized for **online transaction processing (`OLTP`)** workloads.
## Combining Provisioned `IOPS` storage with Multi-AZ deployments
For production `OLTP` use cases, it's recommended that you use [Multi-AZ](aws_az.md) deployments for enhanced fault tolerance for provisioned `IOPS` storage for fast and predictable performance.

The type of storage for a read replica is independent of that on the primary DB instance. For example, you might use General Purpose `SSD` for read replicas with a primary instance that uses Provisioned `IOPS SSD` to reduce costs.
## Performance impact when you modify an SSD volume
When you modify a General Purpose SSD or Provisioned IOPS SSD volume, it goes through a sequence of states.

While the volume is in the `optimizing` state, your volume performance is between the source and target configuration specifications.

When you modify an instance's storage so that it goes from one volume to four volumes, or when you modify an instance using magnetic storage, RDS doesn't use the Elastic Volumes feature. Instead, RDS provisions new volumes and transparently moves the data from the old to the new volumes. This operation consumes significant amount of IOPS and throughput of both old and new volumes. Depending on the size of the volume and the amount of database workload during the modification, this operation can consume a high amount of IOPS, significantly increase I/O latency, and take several hours to complete, while the RDS instance remains in the `Modifying` state.