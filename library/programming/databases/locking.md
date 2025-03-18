Locking
Locks are used to prevent data from being modified by multiple processes at the 
same time. This is important because if two processes are modifying the same 
data at the same time, the data can become corrupted.
Locks are used when you are working with concurrency or your application has many
users running it at the same time.

There are two types of locks:
- Shared locks: let you read the row or the table that is being locked. Hence, 
  it’s also called a read lock. Multiple transactions (you can think of each 
  transaction as a separate process) can acquire a shared lock on the same resource 
  and read from it. No transaction is allowed to update the resource while it has 
  a shared lock.
- Exclusive: locks lock the row or table entirely and let the transaction update 
  the row in isolation. Unlike shared locks, only one transaction can acquire an 
  exclusive lock on a certain resource at one point in time. And while it acquires 
  the lock on that resource, other processes that want to acquire the lock on the 
  same resource will have to wait. Once the lock is released, the remaining 
  processes can acquire it and make modifications.

Optmistic Locking:
let the processes update the same records in parallel. Only when one process 
successfully commits its changes, the other process is told that there exists a 
conflict due to which the other process will have to attempt the transaction again.

Pessimistic Locking:
ock the row as soon as one process attempts to modify it (or delete it) and ask 
the other processes to wait before doing anything.

Transaction Isolation
ACID-compliant databases need to make sure that each transaction is carried out in 
isolation. This means that the results of the transaction is only visible after a 
commit to the database happens. Other processes should not be aware of what’s 
going on with the records while the transaction is carried out.
