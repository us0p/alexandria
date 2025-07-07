```SQL
-- My solution
SELECT
    customer_number
FROM
    Orders
GROUP BY
    customer_number
ORDER BY
    COUNT(customer_number) DESC
LIMIT 1;
```
- Performance: Minimal overhead, best of the three.
- Index: Can benefit from indexes.
- Memory usage: low.

```SQL
-- Using Window functions
SELECT 
    tab2.customer_number 
FROM  (
    SELECT 
        tab.customer_number,
        DENSE_RANK() OVER (ORDER BY order_number DESC) rk 
    FROM (
        SELECT 
            customer_number,
            COUNT(order_number) AS order_number 
		FROM 
            Orders 
        GROUP BY 
            customer_number
	) tab
) tab2 
WHERE 
    tab2.rk=1;
```
- Performance: Slow, extra window + subqueries
- index: Can use but nested structure reduces benefit.
- Memory usage: Higher due to `DENSE_RANK()`.

```SQL
-- Using CTE
WITH CTE AS (
    SELECT 
        customer_number,
        COUNT(customer_number) as cnt
    FROM 
        Orders
    GROUP BY 
        customer_number
)
SELECT 
    customer_number
FROM 
    CTE
ORDER BY 
    cnt DESC
LIMIT 1;
```
- Performance: Nearly as fast as query 1.
- Index usage: Same as query 1.
- Memory usage: Low.

>The CTE version should be used only when you want to reuse aggregated data.