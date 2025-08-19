# INTERSECT
Is a set operator that returns rows that **are present in both queries**. 

It's like the logical **AND** of two `SELECT` results.
## Rules
1. Same number of columns in both queries.
2. Same data types (or at least compatible types) in corresponding columns.
3. Removes duplicate rows automatically.
## Example
```SQL
-- Returns customers that bought the same product in both years.
SELECT CustomerID, Product
FROM Sales2024
INTERSECT
SELECT CustomerID, Product
FROM Sales2025;

-- Find products sold in both years.
SELECT Product
FROM Sales2024
INTERSECT
SELECT Product
FROM Sales2025;
```