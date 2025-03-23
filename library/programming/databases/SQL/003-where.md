# WHERE
Keyword used to perform a condition check on the rows. Only the matching rows are returned.
```SQL
SELECT * FROM table_name WHERE col1 = "pewter";
```

>WHERE can't be used on aggregated columns. For that, take a look at [having](012-having.md)