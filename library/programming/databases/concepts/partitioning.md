# Partitioning
Refers to splitting what is logically one large table into smaller physical pieces.
- Query performance can be improved dramatically in certain situations, particularly when most of the heavily accessed rows of the table are in a single partition or small number of partitions.
- Seldom-used data can be migrated to cheaper and slower storage media, or even to a separate table to keep only most relevant register into a small, fast table.
- Mostly used for data retention compliance.
## Declarative partitioning
The table that is divided is referred to as a **partitioned** table.

The partitioned table itself is a "virtual" table having no storage of its own. Instead, the storage belongs to **partitions**, which are ordinary tables associated with the partitioned table.

Each **partition** stores a subset of the data as defined by its **partition bounds**.

All rows inserted into a **partitioned table** will be routed to the appropriate one of **partitions** based on the values of the **partition key column(s)**.

Updating the **partition key** of a row will cause it to be moved into a different **partition** if it no longer satisfies the **partition bounds** of its original partition.

It's not possible to turn a regular table into a partitioned table or vice versa.

However, it's possible to add an existing regular or partitioned table as a partition of a partitioned table, or remove a partition from a partitioned table, turning it into a standalone table.
## Range partitioning
Table is partitioned into "ranges" defined by a key column or set of columns, with no overlap between the ranges of values assigned to different partitions.

Each range's bounds are understood as being inclusive at the lower end and exclusive at the upper end.
```PostgreSQL
-- Parent table
CREATE TABLE sales (
    id SERIAL,
    sale_date DATE NOT NULL,
    amount NUMERIC
) PARTITION BY RANGE (sale_date);

-- Partitions
CREATE TABLE sales_2023_q1 PARTITION OF sales
    FOR VALUES FROM ('2023-01-01') TO ('2023-04-01');

CREATE TABLE sales_2023_q2 PARTITION OF sales
    FOR VALUES FROM ('2023-04-01') TO ('2023-07-01');

CREATE TABLE sales_2023_q3 PARTITION OF sales
    FOR VALUES FROM ('2023-07-01') TO ('2023-10-01');
```
## List partitioning
Partition data based on discrete values, like region names, types, or categories.
```PostgreSQL
-- Parent table
CREATE TABLE customers (
    id SERIAL,
    name TEXT,
    country TEXT NOT NULL
) PARTITION BY LIST (country);

-- Partitions
CREATE TABLE customers_usa PARTITION OF customers
    FOR VALUES IN ('USA');

CREATE TABLE customers_canada PARTITION OF customers
    FOR VALUES IN ('Canada');

CREATE TABLE customers_others PARTITION OF customers
    FOR VALUES IN ('UK', 'Australia', 'Germany');
```
## Hash partitioning
The table is partitioned by specifying a modules and a remainder for each partition.

Distribute data evenly across a number of partitions when values are not naturally groupable (e.g., user IDs).
```PostgreSQL
-- Parent table
CREATE TABLE users (
    id INT,
    username TEXT
) PARTITION BY HASH (id);

-- 4 hash partitions
CREATE TABLE users_part_0 PARTITION OF users FOR VALUES WITH (MODULUS 4, REMAINDER 0);
CREATE TABLE users_part_1 PARTITION OF users FOR VALUES WITH (MODULUS 4, REMAINDER 1);
CREATE TABLE users_part_2 PARTITION OF users FOR VALUES WITH (MODULUS 4, REMAINDER 2);
CREATE TABLE users_part_3 PARTITION OF users FOR VALUES WITH (MODULUS 4, REMAINDER 3);
```
## Limitations
- Partitions cannot have columns that are not present in the parent.
- `NOT NULL` constraints of a partitioned table are always inherited by all its partitions.
- As a partitioned table does not have any data itself, attempts to use `TRUNCATE ONLY` on a partitioned table will always return an error.
## Partition Pruning
Query optimization technique that improves performance for declaratively partitioned tables.

```PostgreSQL
SET enable_partition_pruning = on;                 -- the default
SELECT count(*) FROM measurement WHERE logdate >= DATE '2008-01-01';
```

Without partition pruning, the above query would scan each of the partitions of the `measurement` table. With partition pruning enabled, the planner will examine the definition of each partition and prove that the partition need not be scanned because it could not contain any rows meeting the query's `WHERE` clause.:w

Note that partition pruning is driven only by the constraints defined implicitly by the partition keys, not by the presence of indexes.

Partition pruning can be performed not only during the planning of a given query, but also during its execution. This is useful as it can allow more partitions to be pruned when clauses contain expressions whose values are not known at query planning time, for example, using a value obtained from a subquery.
## Best practices for declarative partitioning
- **Partition by Common Filters**: Choose partition keys based on columns frequently used in `WHERE` clauses to enable effective partition pruning and improve query performance.
- **Align with Data Removal Patterns**: Design partitions to isolate data that will be dropped together, making bulk deletions efficient.
- **Balance Partition Count**: Too few partitions can harm index efficiency and cache locality; too many increase planning time, memory use, and metadata overhead.
- **Plan for Future Growth**: Anticipate changes in data volume and access patterns to avoid costly repartitioning later.
- **Minimize Post-Pruning Load**: Reduce the number of partitions left after pruning to lower query planning time and memory usage, especially in multi-session environments.