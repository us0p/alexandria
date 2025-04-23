## Database Object Management Functions
The functions bellow are used to calculate the disk space usage of database objects, or assist in presentation or understanding of usage results. `bigint` results are measured in bytes.

```plaintext
pg_total_relation_size(regclass) -> bigint
Computes the total disk space used by the specified table, including all indexes and TOAST data. The result is equivalent to pg_table_size + pg_indexes_size.

pg_relation_size(relation regclass [,fork text]) -> bigint
Computes the disk space used by one "fork" of the specified relation. With one argument, this returns the size of the main data fork of the relation. The second argument can be provided to specify which fork to examine:
- main returns the size of the main data fork of the relation (table size).
- fsm returns the size of the Free Space Map associated with the relation.
- vm returns the size of the Visibility Map associated with the relation.
- init returns the size of the initialization fork, if any, associated with the relation.

pg_size_pretty (bigint | numeric) -> text
Converts a size in bytes into a more easily human-readable format with size units (bytes, kB, MB, GB, TB, or PB).
```

`pg_catalog` is the default system schema in PostgreSQL. it holds all the internal system tables, views, and functions PostgreSQL uses to manage the database.
It contain thins like:
- `pg_class`: info about tables, indexes, sequences
- `pg_attribute`: info about columns
- `pg_stat*`: statistical and performance data
- `pg_tables`, `pg_views`: convenience views for user-facing metadata.
Usually you don't have to specify `pg_catalog` in queries because it's in the default `search_path`.

`pg_statio_user_tables` is a system view in the `pg_catalog` schema.
It shows I/O statistics for user-defined tables (not system tables), and includes data like:
- `schemaname`: name of the schema of the table
- `relname`: name of the table
- `relid`: OID (Object ID) of the table.  It's a reference to the `pg_class.oid`, which uniquely identifies a table (or any relation) in the PostgreSQL system catalog.
- I/O counter like `heap_blks_read`, `idx_blks_hit`, etc.