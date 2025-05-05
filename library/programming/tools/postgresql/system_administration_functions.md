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

## Session Information Functions
`pg_backend_pid() -> integer`: Returns the process ID of the server process attached to the current session.
