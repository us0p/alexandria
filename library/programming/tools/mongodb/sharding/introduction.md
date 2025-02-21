## Sharded Cluster
A sharded cluster consists of the following components:
- **shard**: Each shard contains a subset of the sharded data. Each shard 
  must be deployed as a `replica set`.
- **mongos**: Act as a query router, providing an interface between client
  applications and the sharded cluster.
- **config servers**: Store metadata and configuration settings for the 
  cluster. Config servers must be deployed as a replicaset (CSRS).

!["Iteration between components within a sharded cluster"](https://www.mongodb.com/docs/manual/images/sharded-cluster-production-architecture.bakedsvg.svg)
  
MongoDB shards data at the `collection` level, distributing the collection
data across the shards in the cluster.  
  
## Shard Keys
MongoDB uses the `shard key` to distribute the collection's documents 
across shards. The shard key consists of a field or multiple fields in the
documents.  
You select the shard key when `sharding a collection`.  
A document shard key value determines its distribution across the shards.

**Shard Key Index**  
To shard a populated collection, the collection must have an `index` that 
starts with the shard key. When sharding an empty collection, MongoDB 
creates the supporting index if the collection does not already have an 
appropriate index for the specified shard key.
  
**Shard Key Strategy**  
The choice of shard key affects the performance, efficiency, and 
scalability of a sharded cluster. A cluster with the best possible hardware
and infrastructure can be bottlenecked by the choice of shard key. The 
choice of shard key and its backing index can also affect the `sharding 
strategy` that your cluster can use.
  
## Chunks
MongoDB partitions sharded data into `chunks`. Each chunk has an inclusive
lower and exclusive upper range based on the `shard key`.

## Balancer and Even Data Distribution
In an attemp to achieve an even distribution of data across all shards in 
the cluster, a `balancer` runs in the background to migrate `ranges` across
the `shards`.  
  
## Considerations Before Sharding
Sharded cluster infrastructure requirements and complexity require careful
planning, execution, and maintenance.  
While you can `reshard your collection` later, it is important to carefully
consider your shard key choice to avoid scalability and performance 
issues.  
If queries do not include the shard key or the prefix of a `compound` shard 
key, `mongos` performs a `broadcast operation`, querying all shards in the
sharded cluster. These scatter/gather queries can be long running 
operations.  
  
## Sharded and Non-Sharded Collections
A database can have a mixture of sharded and unsharded collections. Sharded
collections are `partitioned` and distributed across the `shards` in the 
cluster. Unsharded collections can be located on any shard but cannot span
across shards.  

!["sharded and non-sharded collections representation"](https://www.mongodb.com/docs/manual/images/sharded-cluster-primary-shard.bakedsvg.svg)
  
## Connecting to a Sharded Cluster
You must connect to a `mongos` router to interact with any collection in 
the `sharded cluster`. This includes sharded and unsharded collections. 
Clients should never connect to a single shard in order to perform read or
write operations.  
  
!["connection representation"](https://www.mongodb.com/docs/manual/images/sharded-cluster-mixed.bakedsvg.svg)

## Sharding Strategy
MongoDB supports two sharding strategies for distributing data across 
`sharded clusters`. 
  
**Hashed Sharding**  
Hashed Sharding involves computing a hash of the shard key field's value. 
Each `chunk` is then assigned a range based on the hashed shard key 
values.  
  
> MongoDB automatically computes the hashes when resolving queries using 
hashed indexes. Applications do **not** need to compute hashes.
  
!["hashed sharding representation"](https://www.mongodb.com/docs/manual/images/sharding-hash-based.bakedsvg.svg)
  
While a range of shard keys may be "close", their hashed values are 
unlikely to be on the same `chunk`. Data distribution based on hashed 
values facilitates more even data distribution, especially in data sets 
where the shard key changes `monotonically`.  
However, hashed distribution means that range-based queries on the shard 
key are less likely to target a single shard, resulting in more cluster 
wide `broadcast operations`.  
  
**Ranged Sharding**  
Involves dividing data into ranges based on the shard key values. Each 
`chunk` is then assigned a range based on the shard key values.  
  
!["ranged sharding representation"](https://www.mongodb.com/docs/manual/images/sharding-range-based.bakedsvg.svg)
  
A range of shard keys whose values are "close" are more likely to reside on
the same `chunk`. This allows for `targeted operations` as a `mongos` can 
route the operations to only the shards that contain the required data.  
The efficiency of ranged sharding depends on the shard key chosen. Poorly 
considered shard keys can result in uneven distribution of data, which can 
negate some benefits of sharding or can cause performance bottlenecks.  
  
## Zones in Sharded Clusters
Zones can help improve the locality of data for sharded clusters that span
multiple data centers.  
In sharded clusters, you can create `zones` of sharded data based on the 
`shard key`. You can associate each zone with one or more shards in the 
cluster. A shard can associate with any number of zones. In a balanced 
cluster, MongoDB migrates `chunks` covered by a zone only to those shards 
associated with the zone.  
Each zone covers one or more ranges of `shard key` values. Each range a 
zone covers is always inclusive of its lower boundary and exclusive of its
upper boundary.  
  
!["zones in sharded clusters representation"](https://www.mongodb.com/docs/manual/images/sharded-cluster-zones.bakedsvg.svg)
  
The possible use of zones in the future should be taken into consideration
when choosing a shard key.  
  
> Setting up zones and zone ranges before you shard an empty or a 
non-existing collection allows for a faster setup of zoned sharding.
  

## Change Streams
`Change streams` are available for replica sets and sharded clusters. 
Change streams allow applications to access real-time data changes without
the complexity and risk of tailing the oplog. Applications can use change 
streams to subscribe to all data changes on a collection or collections.  
  
## Transactions
With the introduction of `distributed transactions`, multi-document 
transactions are available on sharded clusters.  
Until a transaction commits, the data changes made in the transaction are 
not visible outside the transaction.  
However, when a transaction writes to multiple shards, not all outside read
operations need to wait for the result of the committed transaction to be 
visible across the shards. For example, if a transaction is committed and 
write 1 is visible on shard A but write 2 is not yet visible on shard B, an
outside read at read concern `"local"` can read the results of write 1 
without seeing write 2.
