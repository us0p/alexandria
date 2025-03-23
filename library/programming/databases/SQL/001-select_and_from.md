# Select and FROM
`SELECT` indicates which columns you'd like to view
`FROM` identifies the table that they live in.
```SQL
SELECT col1, col2, col3 FROM table_name;

-- You can use an * to get all the columns from a table
SELECT * FROM table_name;

-- You can rename columns for ease when reading
SELECT col1 AS Name FROM table_name;

-- You can also use it to rename table names to make queires more readable
SELECT col1 AS Name FROM table_name AS Person;

-- Note that you can also rename without using AS:
SELECT p.col1 Name FROM table_name p;
```

