# PostgreSQL
Open-source Object-Relational Database Management System (ORDBMS) that is known for its robustness, extensibility, and SQL compliance.
## PostgreSQL vs. MySQL
- It stands out among other RDBMS options due to its open-source nature.
- MySQL is preferred for managing read-only commands. It is not preferred when concurrency is required.
- PostgreSQL is preferred for managing read-write operations, large datasets, and complex queries. But i's not preferred for read-only operations.
- MySQL offers fewer features than PostgreSQL, but this allows MySQL to stay lighter, more stable, and faster at processing.
- PostgreSQL was built to be ACID-compliant from the ground up and it's optimal when concurrent transactions (MVCC) are required, but is slower and less stable when it comes to read-only operations.
- MySQL is highly compatible with many different types of data storage engines. Whereas PostgreSQL is highly compatible with many different NoSQL formats.
- Some MySQL storage engines like MyISAM don't support ACID. If you need ACID compliance with MySQL, try InnoDB.
- PostgreSQL supports a wider range of data types, including arrays and hstore.
- PostgreSQL is an ORDBMS. This allows you to define objects and table inheritance, translating to more complicated data structures.
## Relational Databases
Relational databases organize data into structure tables, allowing for efficient storage, retrieval, and manipulation of information.
## Tables
Composed of columns (aka as field or attributes) and rows (aka records or tuples). Columns define the different types of information that can be stored (data types).
Rows represents individual instances or entries within the table.
## Primary Keys
Unique identifier for each record in a table. Ensures that each row within the table can be uniquely identified and accessed.
## Foreign Keys
Columns within a table that establish relationships with the primary key of another table. They create connections between different tables.
## Entity-Relationship Diagrams (ERDs)
Visual representation of the relationship between tables in a database.
## [Normalization](normalization.md)
## High-level database concepts
### Database and Schema
A PostgreSQL database is a container for your data, and within it, you have schemas to organize objects like tables, views, and more.
```SQL
-- Create a database
CREATE DATABASE company;

-- Connect to the database
\c company;

-- Create a schema
CREATE SCHEMA hr;
```
### pg_hba.conf
Is the PostgreSQL Host-Based Authentication configuration. It defines who can connect to the database, and how.
### postgresql.conf
Is a file that holds various configuration settings for PostgreSQL, from memory allocation to connection limits.
### pg_stat_statement
Is a module for tracking execution statistics of all SQL statements executed.
```SQL
-- Enable pg_stat_statements in postgresql.conf
shared_preload_libraries = 'pg_stat_statements'

-- Query for statement statistics
SELECT * FROM pg_stat_statements;
```
### pg_dump
Utility for backing up a PostgreSQL database. It produces a script file that can be used to restore the database.
```bash
pg_dump -U username -d database_name > backup.sql
```
### pg_restore
Utility used to restore a PostgreSQL database from an archive created by `pg_dump`
```bash
pg_restore -U username -d new_database < backup.sql
```
## [ACID](ACID.md)