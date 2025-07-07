# Consistency Patterns
With multiples copies of the same data, we are faced with options on how to synchronize them so clients have a consistent view of the data.

With consistency, every read receives the most recent write or an error.
## Eventual consistency
After a write, reads will eventually see it (typically within milliseconds). Data is replicated asynchronously.

This approach is seen in systems such as DNS and email. Eventual consistency works well in highly available systems.
## Weak consistency
This approach is seen in systems such as memcached. Weak consistency works well in real time use cases such as video chat, and realtime multiplayer games. For example, if you are on a phone call and lose reception for a few seconds, when you regain connection you do not hear what was spoken during connection loss.

In another words, after a write, reads may or may not see it. A best effort approach is taken.

It's very similar to **Eventual consistency**, but, there's no guarantees that data will be consistent in any time in the future. But it can also take some time to the data to be consistent.
## Strong consistency
After a write, reads will see it. Data is replicated synchronously.

This approach is seen in file systems and RDBMSes. Strong consistency works well in systems that need transactions.