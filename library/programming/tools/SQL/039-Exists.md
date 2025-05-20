# EXIST operator
Allows you to check if a subquery returns any row.

It returns `true` if the subquery returns at least one row or `false` otherwise.
```SQL
SELECT
	column1,
	column2
FROM
	table_name
WHERE
	EXISTS (subquery);
```

Typically, you use the `EXISTS` operator to filter rows in a table based on the existence of rows from a related table.

This operator is quite fast because it stops processing when it finds the first matching row.

You can negate the `EXISTS` operator with `NOT`:
```SQL
SELECT
	column1,
	column2
FROM
	table_name
WHERE
	NOT EXISTS (subquery);	
```
## SQL EXISTS operator and NULL
If the subquery returns `NULL`, the `EXISTS` operator returns `true`. This operator only checks for the existence of the row returned by the subquery. It doesn't matter if the row is `NULL` or not.
## Example
```SQL
SELECT
	employee_id,
	first_name,
	last_name
FROM
	employees e
WHERE
	EXISTS (
		SELECT
			1
		FROM
			dependents d
		WHERE
			d.employee_id = e.employee_id
	);
```

For each row in the `employees` table:
- The subquery checks if the `dependents` table has a row with the value in `employee_id` column equals to a value in the `employee_id` column of the current row from the `employees` table. 
- If yes, meaning the current employee has at least one dependent. The subquery returns a row with a value `1`. The `EXISTS` condition evaluates to `true`. The outer query includes the current row of the `employees` table in the final result set.
- If no, meaning the current employee has no dependents. The subquery returns no row. The `EXISTS` condition evaluates to `false`. The outer query does not include the current row from the `employees` table in the final result set.