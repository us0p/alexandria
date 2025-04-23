# ORDER BY
Allows you to reorder your results based on the data in one or more columns.
```SQL
-- Orders in ascending order by default
SELECT * FROM table_name ORDER BY age;

SELECT * FROM table_name ORDER BY age DESC;

-- You can also order by more than one column;
-- Ordering results for names in ascending order and ages in descending order
SELECT * FROM table_name ORDER BY name, age DESC;

-- You should use it before LIMIT statements
SELECT * FROM table_name ORDER BY name LIMIT 10;
```

>The results are sorted by the first column mentioned, then by the following columns.

It's useful to order data by multiple columns if your data falls into categories and you'd like to organize rows by date.

You can also use numbers instead of column names in an `ORDER BY` clause. The numbers will correspond to the order in which you list columns in the `SELECT` clause.
```SQL
SELECT name, age FROM table_name ORDER BY 2, 1;

-- Is the same as
SELECT name, age FROM table_name ORDER BY age, name;
```

>This functionality is not supported by every SQL flavor. But it's supported by SQLite and PostgreSQL.

Note that this functionality should be discouraged in favor of explicit column names for better readability.