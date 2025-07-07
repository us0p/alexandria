```SQL
-- My solution
SELECT
    name
FROM
    Customer
WHERE
    referee_id IS NULL 
OR 
    referee_id <> 2;

-- Using COALESCE and avoiding NULL check
SELECT
    name
FROM
    Customer
WHERE
    COALESCE(referee_id, 0) <> 2;
```
- Using `IS NULL` is better in performance as it can use indexes while function calls like `COALESCE` cannot.
- `IS NULL` can also be optimized by the query planner separately while function calls cannot.
- `IS NULL` is more likely to be pushed down, while `COALESCE` is less likely due to function wrapping.