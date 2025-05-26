# DISTINCT
Used when you want to look only to distinct values on a given column.
```SQL
SELECT DISTINCT name from table_name;

-- You can also selecet multiple columns, in which case, only distinct combinations of those columns are going to be returned
SELECT DISTINCT name, age from table_name;
```
## DISTINCT with aggregation functions
You can use `DISTINCT` when performing an aggregation.
You'll probably use it most commonly with the `COUNT` function.
```SQL
-- Counts the number of distinct names in the table
SELECT COUNT(DISTINCT name) FROM table_name;
```
## DISTINCT ON
Allows us to retrieve unique rows based on specific columns. Allow us to specify which row to keep for each unique value based on an [`ORDER BY`](006-order_by.md) clause.

Allows fetching the first unique row based on specified columns.

This expression is used to return only the first row of each set of rows where the given expression has the same value, effectively removing duplicates based on the ordering specified in the `ORDER BY` clause.

It must always match the leftmost expression in the `ORDER BY` clause to ensure predictable results.

Unlike the standard `DISTINCT` clause that discard all duplicate rows, `DISTINCT ON` enable us to determine which row to retain by arranging the rows in a particular order through the [`ORDER BY`](006-order_by.md) clause.

```SQL
SELECT DISTINCT ON (column1, column2, ...) column1, column2, ...
FROM table_name
ORDER BY column1, column2, ...;
```

- `DISTINCT ON`: Return the first row for each unique combination of the specified columns.
- `ORDER BY`: Is crucial because it determines which row from each group of duplicates will be kept. The rows are ordered based on the columns specified here.