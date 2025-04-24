# `UPDATE` Statement
Used to modify data of one or more rows in a table.
```SQL
UPDATE table_name
SET
	column1 = value1,
	column2 = calue2
WHERE
	condition;
```

The `WHERE` clause is optional. If you omit the `WHERE` clause, the `UPDATE` statement will update all the rows in the table.