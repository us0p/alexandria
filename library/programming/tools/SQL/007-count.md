# COUNT
An SQL aggregate function for counting the number of non-null rows in a particular column.
```SQL
-- Returns only a single row with a single column 'count' with the number of results of the whole set.
SELECT COUNT(*) FROM table_name;

-- Provides a count of all the rows in which name IS NOT NULL.
SELECT COUNT(name) FROM table_name;

-- Renaming column name to be more explicit.
SELECT COUNT(name) name_count FROM table_name;
```