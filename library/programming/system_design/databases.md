A relational database like SQL is a collection of data items organized in tables.

**ACID** is a set of properties of relational database transactions.
- **Atomicity** - Each transaction is all or nothing
- **Consistency** - Any transaction will bring the database from one valid state to another
- **Isolation** - Executing transactions concurrently has the same results as if the transactions were executed serially
- **Durability** - Once a transaction has been committed, it will remain so

There are many techniques to scale a relational database:
- [master-slave replication](availability-patterns.md###Master-Slave)
- [master-master replication](availability-patterns.md###Master-Master)
- [federation](##Federation)
- [sharding](##Sharding)
- [denormalization](##Denormalization)
- [SQL tuning](##SQL%20Tuning)
## Federation
![[Pasted image 20250623174900.png]]
Federation (or functional partitioning) splits up databases by function.

For example, instead of a single, monolithic database, you could have three databases: 
- **forums**,
- **users**,
- **products**,

Resulting in less read and write traffic to each database and therefore less replication lag.

Smaller databases result in more data that can fit in memory, which in turn results in more cache hits due to improved cache locality.

With no single central master serializing writes you can write in parallel, increasing throughput.
### Disadvantage(s): federation
- Federation is not effective if your schema requires huge functions or tables.
- You'll need to update your application logic to determine which database to read and write.
- Joining data from two databases is more complex with a [server link](http://stackoverflow.com/questions/5145637/querying-data-by-joining-two-tables-in-two-database-on-different-servers).
- Federation adds more hardware and additional complexity.
## Sharding
![[Pasted image 20250623175148.png]]
Sharding distributes data across different databases such that each database can only manage a subset of the data.

Taking a users database as an example, as the number of users increases, more shards are added to the cluster.

Similar to the advantages of [federation](##Federation), sharding results in less read and write traffic, less replication, and more cache hits. Index size is also reduced, which generally improves performance with faster queries.

If one shard goes down, the other shards are still operational, although you'll want to add some form of replication to avoid data loss.

Like federation, there is no single central master serializing writes, allowing you to write in parallel with increased throughput.

Common ways to shard a table of users is either through the user's last name initial or the user's geographic location.
### Disadvantage(s): sharding
- You'll need to update your application logic to work with shards, which could result in complex SQL queries.
- Data distribution can become lopsided in a shard. For example, a set of power users on a shard could result in increased load to that shard compared to others.
    - Rebalancing adds additional complexity. A sharding function based on [consistent hashing](http://www.paperplanes.de/2011/12/9/the-magic-of-consistent-hashing.html) can reduce the amount of transferred data.
- Joining data from multiple shards is more complex.
- Sharding adds more hardware and additional complexity.
## Denormalization
Denormalization attempts to improve read performance at the expense of some write performance.

Redundant copies of the data are written in multiple tables to avoid expensive joins. Some RDBMS such as PostgreSQL and Oracle support materialized views which handle the work of storing redundant information and keeping redundant copies consistent.

Once data becomes distributed with techniques such as [federation](##Federation) and [sharding](##Sharding), managing joins across data centers further increases complexity. Denormalization might circumvent the need for such complex joins.

In most systems, reads can heavily outnumber writes 100:1 or even 1000:1. A read resulting in a complex database join can be very expensive, spending a significant amount of time on disk operations.
### Disadvantage(s): denormalization
- Data is duplicated.
- Constraints can help redundant copies of information stay in sync, which increases complexity of the database design.
- A denormalized database under heavy write load might perform worse than its normalized counterpart.
## SQL Tuning
It's important to **benchmark** and **profile** to simulate and uncover bottlenecks.
- **Benchmark** - Simulate high-load situations with tools such as [ab](http://httpd.apache.org/docs/2.2/programs/ab.html).
- **Profile** - Enable tools such as the [slow query log](http://dev.mysql.com/doc/refman/5.7/en/slow-query-log.html) to help track performance issues.
## NoSQL
NoSQL is a collection of data items represented in a **key-value store**, **document store**, **wide column store**, or a **graph database**. Data is denormalized, and joins are generally done in the application code. Most NoSQL stores lack true ACID transactions and favor eventual consistency.

**BASE** is often used to describe the properties of NoSQL databases. In comparison with the [CAP Theorem](cap_theorem.md), BASE chooses availability over consistency.

- **Basically available** - the system guarantees availability.
- **Soft state** - the state of the system may change over time, even without input.
- **Eventual consistency** - the system will become consistent over a period of time, given that the system doesn't receive input during that period.

In addition to choosing between SQL or NoSQL, it is helpful to understand which type of NoSQL database best fits your use case
#### Key-Value store
>Abstraction: hash table.

A key-value store generally allows for O(1) reads and writes and is often backed by memory or SSD. Data stores can maintain keys in lexicographic order (generalization over alphabetical order), allowing efficient retrieval of key ranges.

Key-value stores provide high performance and are often used for simple data models or for rapidly-changing data, such as an in-memory cache layer. Since they offer only a limited set of operations, complexity is shifted to the application layer if additional operations are needed.
#### Document store
>Abstraction: Key-Value store with documents stored as a value

A document store is centered around documents (XML, JSON, binary, etc), where a document stores all information for a given object.

Document stores provide APIs or a query language to query based on the internal structure of the document itself.

Based on the underlying implementation, documents are organized by collections, tags, metadata, or directories. 
Although documents can be organized or grouped together, documents may have fields that are completely different from each other.

Document stores provide high flexibility and are often used for working with occasionally changing data.
### Wide column store
>Abstraction: nested map `ColumnFamily<RowKey, Columns<ColKey, Value, Timestamp>>`

![[Pasted image 20250628111810.png]]

A wide column store's basic unit of data is a column (name/value pair). A column can be grouped in column families (analogous to a SQL table). Super column families further group column families. You can access each column independently with a row key, and columns with the same row key form a row. Each value contains a timestamp for versioning and for conflict resolution.

Google introduced Bigtable as the first wide column store, which influenced the open-source HBase often-used in the Hadoop ecosystem, and Cassandra from Facebook. Stores such as BigTable, HBase, and Cassandra maintain keys in lexicographic order, allowing efficient retrieval of selective key ranges.

Wide column stores offer high availability and high scalability. They are often used for very large data sets.
### Graph database
>Abstraction: graph

![[Pasted image 20250628112929.png]]

In a graph database, each node is a record and each arc is a relationship between two nodes. Graph databases are optimized to represent complex relationships with many foreign keys or many-to-many relationships.

Graphs databases offer high performance for data models with complex relationships, such as a social network. They are relatively new and are not yet widely-used; it might be more difficult to find development tools and resources. Many graphs can only be accessed with REST APIs.
## SQL vs NoSQL
Reasons for **SQL**:
- Structured data
- Strict schema
- Relational data
- Need for complex joins
- Transactions
- Clear patterns for scaling
- More established: developers, community, code, tools, etc
- Lookups by index are very fast

Reasons for **NoSQL**:
- Semi-structured data
- Dynamic or flexible schema
- Non-relational data
- No need for complex joins
- Store many TB (or PB) of data
- Very data intensive workload
- Very high throughput for IOPS

Sample data well-suited for NoSQL:
- Rapid ingest of clickstream and log data
- Leaderboard or scoring data
- Temporary data, such as a shopping cart
- Frequently accessed ('hot') tables
- Metadata/lookup tables