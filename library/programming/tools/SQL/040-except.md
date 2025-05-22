# EXCEPT
Can only be used with `SELECT` queries and is used to extract unique records from the first query result discarding those records which are common to the second query result.

The query result should have the same number of columns in the same order and with same datatype.

```sql
SELECT first_name, last_name from persons
EXECPT
SELECT fname, lname FROM customers;
```

The query above will return all the names in `persons` that don't exist in `customers`.