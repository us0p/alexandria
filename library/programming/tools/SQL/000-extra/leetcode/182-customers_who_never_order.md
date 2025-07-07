```PostgreSQL
SELECT
    name as Customers
FROM
    Customers c
LEFT JOIN
    Orders o
ON
    c.id = o.customerId
WHERE
    o.id IS NULL;
```
- Joins entire `Orders` column, can be slow if there're a lot of orders and duplicated user entries.
- Scans every matching order row (many duplicates per customer = more work).
```PostgreSQL
-- Safest approach instead of NOT IN, avoid NULL checks
SELECT
    name Customers
FROM Customers c
WHERE NOT EXISTS (
        SELECT 
        1 
    FROM 
        Orders o
    WHERE
        o.customerId =
    GROUP BY 1
);
```
- For each customer checks if any order exists.
- Stops scanning as soon as one match if found. Avoids scanning all `Orders` rows.
- Safe for NULLS unlike `NOT IN`.
```PostgreSQL

-- Better performance for large Orders data by removing multiple user orders.
WITH o AS (
    SELECT
        customerId
    FROM
        Orders o
    GROUP BY 1
)
SELECT
    name Customers
FROM
    Customers c
LEFT JOIN o
ON
    o.customerId = c.id
WHERE
    o.customerId IS NULL;
```