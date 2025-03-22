# GROUP BY
An aggregate function that aggregates only part of a table. It separate data into groups, which can be aggregated independently of one another.
```SQL
-- Return only the column "year" of all rows.
SELECT year FROM table_name;

-- Return only the column "year" with only distinct values. It grouped repeated years into a single row.
SELECT year FROM table_name GROUP BY year;

-- Return a list of all the different years in the set and a counting of how many times did they appear in the set.
SELECT year, COUNT(*) count FROM table_name GROUP BY year;

-- You can also use numbers to refer to the position of the selected columns just like in GROUP BY
SELECT year, month, COUNT(year) FROM table_name GROUP BY 1, 2;
```

Note that `COUNT(*)` with `GROUP BY` will count only the occurrences of the last group
```SQL
-- Returns the number of times that each month appeard for each year.
-- Basically counts the number of days of each month.
/*
	|year|month|count|
	|2000|1    |20   |
	|2000|2    |20   |
	|... |...  |...  |
*/
SELECT year, month, COUNT(*) FROM table_name GROUP BY year, month;
```
## Using GROUP BY with ORDER BY
The order of column names in your `GROUP BY` clause doesn't matter, the results will be the same regardless. If you want to control how the aggregations are grouped together, use `ORDER BY`
```SQL
-- Counts how many times year column has appeard in each month.
SELECT 
	year,
	month,
	COUNT(*)
FROM table_name 
GROUP BY year, month 
ORDER BY month, year;

-- Produces different output, counts how many times each month appeard in each year. 
SELECT 
	year,
	month,
	COUNT(*)
FROM table_name 
GROUP BY year, month 
ORDER BY year, month; -- The difference is here
```
## LIMIT
`GROUP BY` is evaluated before the `LIMIT` clause. If you group by a column with enough unique values that it exceeds the `LIMIT` number, the aggregates will be calculated, and then some rows will simple be omitted from the results.

## TIPS
### Group by the common factor
You'll want to group the results by columns that repeat, you can only group similar values. 

For example, if you want to group the volume of transactions for each month in all your account history:
```SQL
-- The common factor (the one that repeats) is "month"
-- You wan't to group all the months and sum all the valumes in the column "volume"
SELECT month, SUM(volume) vol_count FROM transactions GROUP BY month;
```