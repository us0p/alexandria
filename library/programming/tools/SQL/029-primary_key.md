A primary key is a column or a set of columns that **uniquely identifies each row in the table**.

A table includes one and only one primary key.

If a primary key includes two or more columns, these are primary key columns. The primary key is also known as **composite key**.

A primary key has the following characteristics:
- Unique
- Non-Nullable
- Immutable
```SQL
CREATE TABLE projects (
	project_id INT PRIMARY KEY, -- Adding primary key constraint
	project_name VARCHAR(255) NOT NULL
)

-- Another way of defining a primary key is as a table constraint
-- Can be specified after the column list
-- This syntax is more suitable for defining a primary key with two or more columns.
CREATE TABLE projects (
	project_id INT,
	employee_id INT,
	project_name VARCHAR(255) NOT NULL,
	PRIMARY KEY (project_id, employee_id)
)
```
## Primary Key Constraint Names
When defining a primary key constraint, you can assign it a name using the `CONSTRAINT` clause:
```SQL
CONSTRAINT constraint_name PRIMARY KEY (column1, column2, ...)
```

If you don't provide a name for the `PRIMARY KEY` constraint, the database system will generate a default name for it. It vary depending on the database system.

| database   | Default Primary Key Constraint Name |
| ---------- | ----------------------------------- |
| PostgreSQL | TableName_pkey                      |
| SQLite     | sqlite_autoindex_TableName_n        |
## Removing a primary key from a table
```SQL
ALTER TABLE table_name DROP CONSTRAINT primary_key_constraint;
```
## Adding the primary key to an existing table
```SQL
ALTER TABLE table_name
ADD CONSTRAINT constraint_name
PRIMARY KEY (column1, column2, ...);
```