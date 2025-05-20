# SQL Triggers
Is a database object that executes a piece of code, a user-defined function, or a stored procedure in response to a specific event in a table.

A trigger is always associated with a specific table. If the table is deleted, all the associated triggers are automatically deleted

A trigger is invoked either before or after the following events:
- INSERT
- UPDATE
- DELETE
- TRUNCATE - When a table is truncated (PostgreSQL).

In some RDBMS, a trigger is also invoked as the result of executing a statement that indirectly executes the `INSERT, UPDATE`, or `DELETE` statement.

A trigger is only executed if the matching statement is executed. This means that you can perform similar operations and not invoke any trigger.

For example, the `TRUNCATE TABLE` statement removes all rows in the table but does not invoke the `BEFORE DELETE` and `AFTER DELETE` triggers. In PostgreSQL, the `TRUNCATE TABLE` statement triggers a `TRUNCATE` trigger.
```SQL
CREATE TRIGGER trigger_name
[BEFORE|AFTER] event -- event is INSERT, UPDATE, DELETE, (TRUNCATE in PGSQL)
-- trigger_type is either 'FOR EACH ROW' or 'FOR EACH STATEMENT'
-- table_column is optional.
OF table_column ON table_name trigger_type 
-- BEGIN...END block, user-defined function or stored procedure.
```
## Row-level
Executes each time a row is affected by a DML statement.

If the statement affects 10 rows, the row-level trigger will execute 10 times.
## Statement-level
Is called once, regardless of how many affected rows.

Different of the row-level, if the SQL statement doesn't affect any rows, the statement-level trigger will still be executed.
## Why use SQL Triggers
- Loggings
- Enforce complex integrity of data
## Modify SQL Triggers
To change the trigger definition, you use the `CREATE OR REPLACE TRIGGER` statement.
## Removing SQL Triggers
To drop a trigger from a database, you use the `DROP TRIGGER` statement with the following syntax:
```SQL
DROP TRIGGER [IF EXISTS] trigger_name ON table_name;
```

Without the `IF EXISTS` option, the database may issue an error if you try to drop a non-existing trigger.