```SQL
-- My solution
SELECT 
    employee_id 
FROM 
    Salaries 
WHERE 
    employee_id NOT IN (
        SELECT 
            employee_id 
        FROM 
            Employees
    )
UNION
SELECT 
    employee_id 
FROM 
    Employees 
WHERE 
    employee_id NOT IN (
        SELECT 
            employee_id 
        FROM 
            Salaries
    )
ORDER BY
    1;
```
- `NOT IN` performs **poorly** if the subquery returns `NULL`, unless explicitly filtered.
- Not as efficient on **large** or **unindexed** datasets, since each `NOT IN` can lead to full scans.
- Execute subqueries twice, no sharing.

```SQL
-- Using LEFT and RIGHT joins to mimic a FULL JOIN
JOIN implementation
SELECT 
  T.employee_id 
FROM 
  (
    SELECT 
      * 
    FROM 
      Employees 
      LEFT JOIN Salaries USING(employee_id) 
    UNION 
    SELECT 
      * 
    FROM 
      Employees 
      RIGHT JOIN Salaries USING(employee_id)
  ) AS T 
WHERE 
  T.salary IS NULL 
  OR T.name IS NULL 
ORDER BY 
  employee_id;
```
- More robust than `NOT IN` with `NULL`.
- Can work well with indexes if used carefully.
- `UNION` overhead.

```SQL
-- Using FULL JOIN, usefull for databases where it's supported.
SELECT 
    COALESCE(e.employee_id, s.employee_id) employee_id
FROM 
    Employees e 
FULL JOIN 
    Salaries s USING(employee_id)
WHERE
    e.name IS NULL
OR
    s.salary IS NULL
ORDER BY
    1;
```
- Best performance and cleanest logic.
- Uses a single join operation and avoids subqueries.
- Safe with `NULL`.
- Indexes can be used more effectively on `employee_id`.