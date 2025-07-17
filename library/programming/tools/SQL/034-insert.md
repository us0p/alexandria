# `INSERT` Statement
Used to insert one or more rows into a table.
```SQL
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

If you don't provide a column in the `INSERT` statement, it will take a default value which is `NULL` or a value defined by a `DEFAULT` constraint.
```SQL
INSERT INTO dependents (first_name, last_name, relationship, employee_id)
VALUES
	('Luan', 'Lopes', 'Me', 1)
	('Mariana', 'Batistone', 'Gf', 2)
	...;
```
## INSERT from a SELECT
```SQL
INSERT INTO t (column1, column2, ...)
SELECT
	column1,
	column2,
	...
FROM t2;
```