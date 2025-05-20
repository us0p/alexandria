# Views
It's a named query stored in the database system.

Unlike a table, a view doesn't store data physically. The database system only stores the view's definition.

Some views can be updatable. It means you can modify the underlying table's data via updatable views.
```SQL
CREATE VIEW [IF NOT EXISTS] view_name
AS
query
```

The tables queried during the view creation are known as **base tables**.

By default the view uses the column names of the defining query. If you want to use different names, you can explicitly specify them in the `CREATE VIEW` clause:
```sql
CREATE VIEW view_name(column1, column2, ...)
AS
query;
```
### Concrete Example
```SQL
CREATE VIEW IF NOT EXISTS payroll (first_name, last_name, job, compensation)
AS
SELECT
	first_name,
	last_name,
	job_title,
	salary
FROM
	employees e
	INNER JOIN jobs j ON j.job_id = e.job_id
ORDER BY
	first_name;
```
### Querying data from views
Is the same as selecting data from tables.
```SQL
SELECT * FROM payroll;
```
## Modifying Views
Use `CREATE OR REPLACE VIEW` statement to add or remove columns from a view.
```SQL
CREATE OR REPLACE view_name
AS
query;
```

>To update a column in a view, is necessary define the whole structure again.
## Removing an SQL View
```SQL
DROP VIEW view_name;
```