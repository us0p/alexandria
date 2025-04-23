```SQL
CREATE TABLE table_name (
	column_name1 datatype constraint,
	column_name2 datatype constraint,
	...
)
```

Constraints are an optional rule for data.
```SQL
CREATE TABLE courses (
	name VARCHAR(255) NOT NULL,
	description TEXT,
	duration DEC(4,2) NOT NULL
)
```

The `courses` table has three columns:
	- `name`: The data type is `VARCHAR` with a maximum of 255 characters. The `NOT NULL` constraint is used to ensure the this column will always have data.
	- `description`: The data type is `TEXT`, which can store very large text.
	- `duration`: The data type is `DEC` which stores decimals numbers. The number 4 represents the maximum number of digits the decimal can have. The number 2 represents the number of digits that must exist after the decimal point. Examples:
		- 12.34: valid, 4 digits in total, 2 after decimal
		- 1.23: valid, 3 digits, 2 after decimal
		- 99.99: valid: 4 digits, 2 after decimal, maximum value the column can store.
		- 123.45: invalid, 5 digits.
		- 100.0: invalid, 4 digits, has only 1 digit after decimal.

The database will issue an error if you attempt to create a table that already exists. To avoid the error, you can use the `IF NOT EXISTS` option:
```SQL
CREATE TABLE IF NOT EXISTS table_name (
	column_name1 datatype constraint,
	column_name2 datatype constraint,
	...
)
```