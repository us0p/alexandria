# Data Types
It's the type of the data stored in each column of your table.
There are a lot of data types, and each database provider might have it's own specifications about each type, you should follow the database specification about supported datatypes and their names.
- [SQLite Data Types Docs](https://www.sqlite.org/datatype3.html)
- [PostgreSQL Data Types Docs](https://www.postgresql.org/docs/17/datatype.html)
## Changing a column's data type
It's possible to change the data type of a column in your query. This is done by using `CAST` clauses.
```SQL
-- In the following example, "date" is stored as string
SELECT CAST(p.birth AS DATE) FROM person p;
```

Each database provider can also have built-in functions that convert one data type to another, it's worth to take a look at your provider documentation.