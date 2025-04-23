# UNION
Joins allow you to combine two datasets side-by-side, but `UNION` allows you to stack one dataset on top of the other.

SQL has strict rules for appending data:
- Both tables must have the same number of columns
- The columns must have the same data types in the same order as the first table
```SQL
SELECT * FROM person WHERE id <= 50

UNION

SELECT * FROM person WHERE id > 50;

-- Is the same as
SELECT * FROM person;
```
## UNION ALL
`UNION` only appends distinct values. If you'd like to append all the values from the second table, use `UNION ALL`.
```SQL
SELECT * FROM person WHERE id <= 50

UNION ALL

SELECT * FROM person WHERE id > 25;

-- Duplicates registers with id 26-50
```