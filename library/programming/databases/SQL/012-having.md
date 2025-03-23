# Having
Used to filter a query that has been aggregated.
It should be used AFTER `GROUP BY` statements.
```SQL
-- Selects the max high for each month of every year in which high was above 400
SELECT year,
	   month,
	   MAX(high) month_high
FROM stock
GROUP BY year, month
HAVING MAX(high) > 400
ORDER BY year, month;
```
