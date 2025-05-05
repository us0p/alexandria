# Schema
A database contains one or more named *schemas*, which in turn contain tables. 

Schemas also contain other kinds of named objects, including data types, functions, and operators.

Within one schema, two objects of the same type cannot have the same name.

Furthermore, tables, sequences, indexes, views, materialized views, and foreign tables share the same namespace.

Unlike databases, schemas are not rigidly separated, a user can access objects in any of the schemas in the database they are connected to, if they have privileges to do so.

Schemas are analogous to directories at the operating system level, except that schemas cannot be nested.
## Schema operations
```PostgreSQL
CREATE SCHEMA schema_name;

-- To create or access objects in a schema.
-- This works anywhere a table name is expected.
SELECT * FROM schema.table;

DROP SCHEMA schema_name;

-- Drops schema including all contained objects.
DROP SCHEMA schema_name CASCADE;
```

>Schema names beginning with `pg_` are reserved for system purposes and cannot be created by users.
## The `public` schema
By default, tables and other objects are automatically put into a schema named `public`. Every new database contains such a schema.
## The schema search path
Tables are often referred to by *unqualified names*, which consists of just the table name. The system determines which table is meant by following a *search path*, which is a list of schemas to look in.

The first schema named in the search path is called the current schema. Aside from being the first schema searched, it is also the schema in which new tables will be created if no other schema name is provided.

```PostgreSQL
SHOW search_path;
```

The first schema to be searched is a schema with the same name as the current user. If no such schema exists, the entry is ignored. The second element refers to the `public` schema.

To put a new schema in the path:
```PostgreSQL
SET search_path TO new_schema,public;
```

There is nothing special about the public schema except that it exists by default. It can be dropped too. In the example above we could just leave the `public` schema out and we wouldn't have access to it anymore.
## Schemas and Privileges
By default users cannot access any objects in schemas they do not own. To allow that, the owner of the schema must grant the `USAGE` privilege on the schema. By default, everyone has that privilege on the schema `public`.
## The System Catalog Schema
In addition to `public` and user-created schemas, each database contains a [`pg_catalog`](system_catalogs_and_views.md) schema, which contains the system tables and all the built-in data types, functions, and operators.

`pg_catalog` is always effectively part of the search path. If it's not named explicitly it is implicitly searched before searching the path's schemas. However, you can explicitly place `pg_catalog` at the end of your search path if you prefer to have user-defined names override built-in names.