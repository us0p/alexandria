# System Catalogs
Is the place where a RDBMS stores schema metadata, such as information about tables and columns, and internal bookkeeping information.

These system tables are physically stored in the `pg_catalog` schema.

| Catalog Name           | Purpose                                |
| ---------------------- | -------------------------------------- |
| `pg_extension`         | Installed extensions                   |
| `pg_database`          | Databases within this database cluster |
| `pg_class`             | Info about all relations               |
| `pg_attribute`         | Info about columns                     |
| `pg_event_trigger`     | Info about event triggers              |
| `pg_namespace`         | Schemas                                |
| `pg_partitioned_table` | Info about partition key of tables     |
| `pg_trigger`           | Info about triggers                    |
## Understanding references and relationships under system catalogs
Every table under the system catalog, represents an database object. Every object has an `oid` (Object Identifier) which is its unique identifier in the system.

Object relationship are represented by referencing another table's `oid`, usually by also referencing the target table name e.g. `pg_class.relnamespace` references `pg_namespace.oid`.
## Relations
Is a general term used to refer to any database object that holds data in a structured format (tables, indexes, views, sequences, etc).
## System Views
In addition to the system catalogs, PostgreSQL provides a number of built-in views. Some system views provide convenient access to some commonly used queries on the system catalogs. Others provide access to internal server state.

Those views are also available under `pg_catalog` schema.

| View Name     | Purpose                                  |
| ------------- | ---------------------------------------- |
| `pg_config`   | Compile-time configuration parameters    |
| `pg_group`    | Groups of database users                 |
| `pg_indexes`  | High level info about indexes            |
| `pg_matviews` | High level info about materialized views |
| `pg_roles`    | Information about database roles         |
| `pg_settings` | Parameter settings                       |
| `pg_stats`    | Planner statistics                       |
| `pg_tables`   | High level info about tables             |
| `pg_users`    | High level info about users              |
| `pg_views`    | High level info about views              |

>The [Information Schema](information_schema.md) provides an alternative set of views which overlap the functionality of the system views. Since the information schema is SQL-standard whereas system views are PostgreSQL-specific, it's usually better to use the information schema if it provides all the information you need.
## Information Schema
The information schema consists of a set of views that contain information about the objects defined in the current database.

The information schema is defined in the SQL standard and can therefore be expected to be portable and remain stable. The information schema views do not, however, contain information about PostgreSQL-specific features; to inquire about those you need to query the system catalogs or other PostgreSQL-specific views.
### Data types

| Type              | Description                                                  |
| ----------------- | ------------------------------------------------------------ |
| `cardinal_number` | A non-negative number                                        |
| `character_data`  | A character string (without specific max len)                |
| `sql_identifier`  | Character string used for SQL identifiers                    |
| `time_stamp`      | A domain over the `timestamp with time zone`                 |
| `yes_or_no`       | A character string domain that contains either `YES` or `NO` |
## Views

| View                                | Description                                                                                                                                                                                |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `administrable_role_authorizations` | Identify roles that a given user can grant to others. It shows which roles the current user is authorized to administer.                                                                   |
| `applicable_roles`                  | Identify all roles that are directly or indirectly granted to the current user or role. It shows which roles are applicable to the current session through inheritance or explicit grants. |
| `columns`                           | Contains information about all table/views columns in the database (System columns are not included)                                                                                       |
| `constraint_column_usage`           | Identifies all columns in the current database that are used by some constraint.                                                                                                           |
| `constraint_table_usage`            | Identifies all tables in the current database that are used by some constraint and are owned by a currently enabled role.                                                                  |
| `enabled_roles`                     | Identifies the currently "enabled roles".                                                                                                                                                  |
| `referential_constraints`           | Contains all referential (foreign key) constraints in the current database.                                                                                                                |
| `role_table_grants`                 | Identifies all privileges granted on tables or views where the grantor or grantee is a currently enable role.                                                                              |
| `schemata`                          | Contains all schemas in the current database that the current user has access to.                                                                                                          |
| `table_constraints`                 | Contains all constraints belonging to tables that the current user owns or has some privilege other than `SELECT` on.                                                                      |
| `table_privileges`                  | Identifies all privileges granted on tables or views to a currently enabled role or by a currently enabled role.                                                                           |
| `tables`                            | Contains all tables and views defined in the current database.                                                                                                                             |
| `triggers`                          | Contains all triggers defined in the current database on tables and views that the current user owns or has some privilege other than `SELECT` on.                                         |
| `views`                             | Identify all views defined in the current database.                                                                                                                                        |
