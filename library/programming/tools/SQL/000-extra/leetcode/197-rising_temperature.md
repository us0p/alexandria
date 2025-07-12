# Rising Temperature
Write a solution to find all dates `id` with higher temperatures compared to its previous dates (yesterday).
## Solution 1 - (Myself)
Uses a lateral join to compare temperatures and dates, uses `INTERVAL` operations to perform date arithmetic.
```PostgreSQL
SELECT
	w1.id id
FROM Weather w1
JOIN Weather w1
	ON w1.temperatrue > w2.temperature
	AND w1.recordDate - INTERVAL '1 day' = w2.recordDate;
```
## Solution 2
The solution uses the window function `LAG` which returns _`value`_ evaluated at the row that is _`offset`_ rows before the current row within the partition, `offset` is default to 1.
```PostgreSQL
WITH cte AS (
    SELECT
        *,
        LAG(temperature) OVER(ORDER BY recorddate) AS prev_day_temp,
        LAG(recorddate) OVER(ORDER BY recorddate) AS prev_date
    FROM weather
)
SELECT
    id
FROM cte
WHERE temperature > prev_day_temp
AND prev_date = recorddate::date - 1;
```