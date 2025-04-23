# LIMIT
Restricts how many rows the SQL query returns.
It's a simple way to keep the queries from taking too long to return.
```SQL
SELECT * FROM table_name LIMIT 100;
```
Note that `LIMIT` doesn't stop the search after the limit number of rows is reached.

If you pay attention, `LIMIT` is executed **after** the query is ran, this means that the DB **will first execute the query** and only after the query is executed, will return only the first 100 rows.