# MIN/MAX
Are aggregate functions that return the lowest and the highest values in a particular column.
Can be used in non-numerical columns.
```SQL
SELECT MIN(name) min_name, MAX(birthday) max_birth FROM table_name;
```