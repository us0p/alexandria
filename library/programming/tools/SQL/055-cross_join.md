# Cross Join
Returns the Cartesian product of two tables.

It requires no condition like other join methods.

```SQL
SELECT
  *
FROM table1
CROSS JOIN table2;

-- It's the same as writing
SELECT
  *
FROM table1, table2;
```
## Considerations
**Cartesian Products** are dangerous and can increase the dataset exponentially, always try to understand the data size and use filters.
## When to use
Use it when you want all combinations of some data and not when you just want to get join some data.
