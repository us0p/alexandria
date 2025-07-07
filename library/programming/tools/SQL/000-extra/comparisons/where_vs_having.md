## WHERE
- Filters **rows before** any **grouping or aggregation**.
- Used to restrict which rows are **included in the query**.
- Cannot use aggregate functions (`COUNT`, `SUM`, etc.).
## HAVING
- Filters **groups after** aggregation (`GROUP BY`).
- Used to restrict which **aggregated results** are returned.
- Can use aggregate functions.
## Example with both
```SQL
SELECT department, AVG(salary) as avg_salary
FROM employees
WHERE hire_date > '2020-01-01'         -- filter raw rows
GROUP BY department
HAVING AVG(salary) > 50000;            -- filter aggregated groups
```