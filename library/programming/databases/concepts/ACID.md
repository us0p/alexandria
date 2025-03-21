# ACID - (Atomicity, Consistency, Isolation, Durability)
Are the four properties of any database system that help in making sure that we are able to perform the transactions in a reliable manner.
- **Atomicity**: The transaction either happens completely or doesn’t happen at all.
- **Consistency**: Data is consistent before and after a transaction without any missing information.
- **Isolation**: Multiple transactions can happen concurrently without reading the wrong data.
- **Durability**: Transactional success is robust to system failure.
## Transaction
Is a series of logically grouped database operations, an indivisible unit of work that may involve many different data operations.
## Goal
- Transactions can fail without hurting data integrity.
- Multiple transactions can occur concurrently without reading and writing the 
  wrong data.

The DBMS achieve ACID compliance through the use of locks to keep the database on hold while transactions happen.
Once a transaction begins and acquires a lock, it can either finish successfully and commit, or run into an error and abort.

ACID model database are a  perfectly fit for use cases where data reliability and consistency are the topmost priority like in banking.
## Dirty Reads
If a transaction is in the middle of updating some data and hasn’t committed yet, and another transaction is allowed to read that uncommitted data, that’s dirty, and could lead to your app showing incorrect data that got rolled back.
## Non-Repeatable Reads
If you’ve got two consecutive reads in one transaction with a concurrent update in between, those reads are going to show different results even though they’re part of the same transaction.
## Phantom Reads
If a transaction reads data and then a concurrent transaction inserts data that would have been read in the original transaction, that’s a phantom read.