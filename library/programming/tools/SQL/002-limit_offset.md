# LIMIT
Restricts how many rows the SQL query returns.
It's a simple way to keep the queries from taking too long to return.
```SQL
SELECT * FROM table_name LIMIT 100;
```
Note that `LIMIT` doesn't stop the search after the limit number of rows is reached.

If you pay attention, `LIMIT` is executed **after** the query is ran, this means that the DB **will first execute the query** and only after the query is executed, will return only the first 100 rows.
## OFFSET
Used to skip a specified number of rows before starting to return rows in a query result.
```SQL
SELECT
	column1,
	column2
FROM
	your_table
OFFSET
	10;
```

Can be used with `LIMIT` to paginate results in a query.
## Considerations
- `OFFSET` makes the database scan and discard the skipped rows, which can be slow for large offsets.
- For better performance in large datasets, consider keyset pagination using a `WHERE id > last_seen_id` condition.