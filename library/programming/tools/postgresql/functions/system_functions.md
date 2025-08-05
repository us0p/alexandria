## `pg_size_pretty`
Convert a size in **bytes** into a more human readable format, like kB, MG, GB, etc.

```PostgreSQL
-- Signature
-- pg_size_pretty(bigint)

SELECT pg_size_pretty(1024); -- '1024 bytes'
SELECT pg_size_pretty(2048);         -- → '2048 bytes'
SELECT pg_size_pretty(4096);         -- → '4096 bytes'
SELECT pg_size_pretty(1048576);      -- → '1024 kB'
SELECT pg_size_pretty(1073741824);   -- → '1 GB'
```
## `pg_total_relation_size`
Returns the total disk space in bytes, used by a table including:
- table data
- TOAST data
- All indexes attached to the table
```PostgreSQL
-- Signature
-- pg_total_relation_size('regclass') -- name of the table as a string or identifier.

SELECT pg_total_relation_size('table_name'); -- returns the size in bytes of the table.
```
## `pg_typeof`
Used to return the data type of **any expression**.

It returns a `regtype` a PostgreSQL internal type representation.
```PostgreSQL
-- Signature
-- pg_typeof(expression)

SELECT pg_typeof(42);
-- Output: integer

SELECT pg_typeof(3.14);
-- Output: numeric

SELECT pg_typeof('hello');
-- Output: text
```