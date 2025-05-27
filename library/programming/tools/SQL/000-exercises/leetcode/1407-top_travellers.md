```PostgreSQL
-- My implementation
SELECT 
	u.NAME,  
    SUM(
	    CASE  
	        WHEN r.distance IS NULL THEN 0  
            ELSE r.distance  
        END
    ) AS travelled_distance  
FROM
	users u  
LEFT JOIN 
	rides r ON r.user_id = u.id  
GROUP  BY 
	1,  
    u.id  
ORDER  BY 
	2 DESC,  
    1 ASC;

-- Using COALESCE() insteade of CASE expressions
SELECT
    u.name,
    SUM(
	    COALESCE(r.distance, 0)
	) AS travelled_distance
FROM 
	Users u
LEFT JOIN 
	Rides r ON r.user_id = u.id
GROUP BY 
	1,
	u.id
ORDER BY 
	2 DESC,
	1 ASC;
```
- Not a big difference in performance between the two queries.
- Use of `COALESCE` makes second query more clear and idiomatic.

```SQL
-- Using CTE with window function
WITH cte AS (
    SELECT 
	    u.id,
	    u.name,
	    r.distance 
	FROM users u 
    LEFT JOIN 
	    rides r ON u.id = r.user_id
)

SELECT 
	DISTINCT name,
	SUM(
		COALESCE(distance,0)
	) OVER (
		PARTITION BY id
	) AS travelled_distance
FROM 
	cte
ORDER BY 
	travelled_distance DESC, 
	name ASC;
```
- Less efficient than the `GROUP BY` versions.
- `SUM(...) OVER(...)` recalculates for each row, even duplicates.