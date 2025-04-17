# Transactions
Is a sequence of multiple operations performed on a database, and all served as a single unit of work, taking place wholly or not at all. In other words, there’s never a case that only half of the operations are performed and the results saved.

Typically, a term like **rollback** refers to the process that undoes any changes made by the transaction, and the term **commit** is used to refer to a permanent change made by the transaction.

In relational databases, transactions must be atomic, consistent, isolated and durable. These properties are commonly abbreviated as [ACID](ACID.md). ACID properties ensure that a database transaction is processed reliably.
## Deeper dive, a transaction life cycle
During its lifecycle, a database transaction goes through multiple states. These states are called transaction states and are typically one of the following:
- Active states: It is the first state during the execution of a transaction. A transaction is active as long as its instructions (read or write operations) are performed.
- Partially committed: A change has been executed in this state, but the database has not yet committed the change on disk. In this state, data is stored in the memory buffer, and the buffer is not yet written to disk.
- Committed: In this state, all the transaction updates are permanently stored in the database. Therefore, it is not possible to rollback the transaction after this point.
- Failed: If a transaction fails or has been aborted in the active state or partially committed state, it enters into a failed state.
- Terminated state: This is the last and final transaction state after a committed or aborted state. This marks the end of the database transaction life cycle.