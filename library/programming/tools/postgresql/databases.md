Every instance of a running PostgreSQL server manages one or more databases. 

Databases are therefore the topmost hierarchical level for organizing SQL objects.
## Managing Databases
A small number of objects, like role, database, and tablespace names, are defined at cluster level and stored in the `pg_global` tablespace. Inside the cluster are multiple databases, which are isolated from each other but can access cluster-level objects. Inside each database are multiple schemas, which contain objects like tables and functions.

Full hierarchy is:
1. Cluster
2. Database
3. Schema
4. Table, Function, etc

It's not possible to access more than one database per connection.

Database-level security has two components:
- access control, managed at the connection level.
- authorization control, managed via the grant system.

Foreign data wrappers like `postgres_fdw` allow for objects within one database to act as a proxies for objects in other database or clusters.

To determine the set of existing databases, examine the `pg_database` [system catalog](system_catalogs_and_views.md).
## Creating a Database
The first database is always created by the `initdb` command when the data storage area is initialized. This database is called `postgres`. So to create the first “ordinary” database you can connect to `postgres`.

Two additional databases, `template1` and `template0`, are also created during database cluster initialization.

Whenever a new database is created within the cluster, `template1` is essentially cloned. This means that any changes you make in `template1` are propagated to all subsequently created databases. 

`template0` is meant as a pristine copy of the original contents of `template1`. It can be cloned instead of `template1` when it is important to make a database without any such site-local additions.
## Tablespaces
Allow database administrators to define locations in the file system where the files representing database objects can be stored. Once created, a tablespace can be referred to by name when creating database objects.