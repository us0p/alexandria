There's a limit on how many columns a table can contain. Depending on the column types, it's between 250 and 1600.
## Generated Columns
A generated column is a special column that is always computed from other columns. Thus, it is for columns what a view is for tables.

There are two kinds of generated columns:
- Stored: Is computed when it is written (inserted or updated) and occupies storage as if it were a normal column.
- Virtual: Occupies no storage and is computed when it is read.

A virtual generated column is similar to a view and a stored generated column is similar to a materialized view.

>PostgreSQL currently implements only stored generated columns.

```PostgreSQL
CREATE TABLE people (
	...,
	height_cm numeric,
	height_in numeric GENERATED ALWAYS AS (height_cm / 2.54) STORED
);
```

A generated column cannot be written to directly, but the keyword `DEFAULT` may be specified.