# Multiversion Concurrency Control (MCC or MVCC)
non-locking concurrency control method commonly used by DBMS to provide concurrent access to the database and in programming languages to implement transactional memory.

Isolation is the property that provides guarantees in the concurrent accesses to data. Isolation is implemented by means of a concurrency control protocol. The simplest way is to make all readers wait until the writer is done, which is known as a read-write lock.

Locks are known to create contention especially between long read transactions and update transactions.

MVCC aims at solving the problem by keeping multiple copies of each data item. In this way, each user connected to the database sees a _snapshot_ of the database at a particular instant in time. Any changes made by a writer will not be seen by other users of the database until the transaction is completed.

When an MVCC database need to update a piece of data, it will not overwrite the original data, but instead creates a newer version of the data item. Thus there are multiple versions stored. The version that each transaction sees depends on the isolation level implemented.
The most common isolation level implemented with MVCC is snapshot isolation in which a transaction observes a state of the data as of when the transaction started.

MVCC provides point-in-time consistent view. Read transactions under MVCC typically use a timestamp or transaction ID to determine what state of the DB to read, and read these versions of the data. Read and write are thus isolated from each other without any need for locking.

MVCC introduces the challenge of how to remove versions that become obsolete and will never be read. In some cases, a process to periodically sweep through and delete the obsolete versions is implemented. This is often a stop-the-world process that traverses a whole table and rewrites it with the latest version of each item.

PostgreSQL can use this approach with its VACUUM FREEZE process.

Other databases split the storage into two parts: the data part and an undo log. The data part always keeps the last committed version. The undo log enables the recreation of older versions of data.
The main inherent limitation of this latter approach is that when there are update-intensive workloads, the undo log part runs out of space and then transactions are aborted.
## How does an MVCC database work
1. Every database record has a version number.
2. Concurrent reads happen against the record with the highest version number.
3. Write operations operate on copy of the record.
4. Users continue to read the older version while the copy is updated.
5. After the write operation is successful, the version id is incremented.
6. Subsequent concurrent reads use the updated version.
7. When a new update occurs, a new version is again created, continuing the cycle.