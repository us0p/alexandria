SQL - Structure Query Language
It’s used for relational databases. A SQL database is a collection of 
tables that stores a specific set of structured data.
SQL databases usually scalle vertically (Increase the size of the machine 
you have).
SQL is a query language.

Relational Databases
Provides a storage for related data tables.

ACID:
- Atomicity
- Consistency
- Isolation
- Durability

New SQL databases (usually cloud based) can are capable of horizontally
scalling Relational Databases by using partitioning and sharding.
A partition is a division of a logical database or its constituent
elements into distinct independent parts.

Relational databases must have a stadardized schema for each of its tables,
which must be defined before use.
Every relational database follow the structured query language but each one
have its own implementation which leads to some differences in query structure
and behavior between RDBMS.
Relational databases are ACID complient, thus keeping tables in sync and
ensuring transactions.
In relational databases you usually don't want to have duplicated data, as
you'll be utilizing the stablished relations to join related data.

---
SQL keywords are capitalized by convention to make queries easier to read.
SQL treats any number of space or a line break to be the same thing.
SQL return column names as lower case, if you want to return them capitalized, wrap the column name in double quotes.
SQL uses single quote to reference column values.
You can't perform arithmetic operations on NULL values.
Use `--` to comment a single line and `/* */` to comment multiple lines.
Aggregate functions only aggregate vertically. If you cant to perform a calculation across rows, you would do this with simple arithmetic.