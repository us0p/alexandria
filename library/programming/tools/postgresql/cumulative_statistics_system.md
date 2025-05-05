# The Cumulative Statistics System
Supports collection and reporting of information about server activity. Presently, accesses to tables and indexes in both disk-block and individual-row terms are counted. The total number of rows in each table, and information about vacuum and analyze actions for each table are also counted. If enabled, calls to user-defined functions and the total time spent in each one are counted as well.
## Statistics Collection Configuration
Since collection of statistics adds some overhead to query execution, the system can be configured to collect or not collect information. This is controlled by configuration parameters that are normally set in `postgresql.conf`.
## Viewing Statistics
Several predefined views, are available to show the current state of the system. There are also several other views, available to show the accumulated statistics. 
### Collected Statistics Views
`pg_statio_user_tables`: Shows I/O statistics for user-defined tables (not system tables), and includes data like:
- `schemaname`: name of the schema of the table
- `relname`: name of the table
- `relid`: OID (Object ID) of the table.  It's a reference to the `pg_class.oid`, which uniquely identifies a table (or any relation) in the PostgreSQL system catalog.
- I/O counter like `heap_blks_read`, `idx_blks_hit`, etc.
### Dynamic Statistics Views
`pg_stat_ssl`: Contain one row per backend or `WAL` sender process, showing statistics about SSL usage on this connection. Can be joined to `pg_stat_activity` or `pg_stat_replication` on the `pid` column to get more details about the connection. Some columns are:
- `pid: integer`: Process ID of a backend or WAL sender process.
- `ssl: boolean`: True if SSL is used on this connection.