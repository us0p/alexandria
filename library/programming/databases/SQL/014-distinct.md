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