Non-standard, database-specific SQL command used to display runtime settings, configuration parameters, or metadata of the database system.
## PostgreSQL
Used to inspect configuration parameters:
```PostgreSQL
SHOW work_mem;
SHOW search_path;
SHOW ssl;

-- See all settings
SHOW ALL;
```
## SQLite
Not supported use `PRAGMA` instead.

Can be used to query or modify internal database settings, behaviors, and metadata.
```SQLite
PRAGMA pragma_name;
PRAGMA pragma_name = value;

-- Example getting table info
PRAGMA table_info(table_name);
```