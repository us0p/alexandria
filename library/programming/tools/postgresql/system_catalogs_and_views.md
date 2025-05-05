# System Catalogs
Is the place where a RDBMS stores schema metadata, such as information about tables and columns, and internal bookkeeping information.

PostgreSQL's system catalogs are regular tables. Normally, one should not change the system catalogs by hand, there are normally SQL commands to do that. For example `CREATE DATABASE` inserts a row into the `pg_database` catalog and actually creates the database on disk.

These system tables are physically stored in the `pg_catalog` schema.

| Catalog Name   | Purpose                                |
| -------------- | -------------------------------------- |
| `pg_extension` | Installed extensions                   |
| `pg_database`  | Databases within this database cluster |
| `pg_class`     | Info about tables, indexes, sequences  |
| `pg_attribute` | Info about columns                     |
## System Views
In addition to the system catalogs, PostgreSQL provides a number of built-in views. Some system views provide convenient access to some commonly used queries on the system catalogs. Others provide access to internal server state.

The [Information Schema](information_schema.md) provides an alternative set of views which overlap the functionality of the system views. Since the information schema is SQL-standard whereas the views described here are PostgreSQL-specific, it's usually better to use the information schema if it provides all the information you need.

| View Name   | Purpose                           |
| ----------- | --------------------------------- |
| `pg_tables` | User facing metadata about Tables |
| `pg_views`  | User facing metadata about Views  |
