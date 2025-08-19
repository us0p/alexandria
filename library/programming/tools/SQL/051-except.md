# EXCEPT
Is a set operator that returns rows from the **first query** that **do not appear** in the second query.

Think of it like subtraction for query results: **First set** - **Second set**.
## Rules
1. Both queries must have the **same number of columns**.
2. Data types must be the **same or compatible in each column position**.
3. Remove **duplicate rows** automatically (like `DISTINCT`).
## Examples
```SQL
-- Find customers who bought something in 2024 but not in 2025
SELECT CustomerID, Product
FROM Sales2024
EXCEPT
SELECT CustomerID, Product
FROM Sales2025;

-- Find products sold in 2024 but not in 2025
SELECT Product
FROM Sales2024
EXCEPT
SELECT Product
FROM Sales2025;

-- ORDER MATTERS
-- Same query as above, inverted original tables.
-- Can produce different results!
SELECT Product
FROM Sales2025
EXCEPT
SELECT Product
FROM Sales2024;
```