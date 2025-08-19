In normal SQL comparisons (`=`), `NULL = NULL`is **unknown** (so it's treated as false).

But in **set operations** like [EXCEPT](051-except.md) and [INTERSECT](050-intersect.md), `NULL`values are **treated as equals** for the purpose of determining duplicates.

That means if both queries return a row where a certain column is `NULL` in the same position, that row counts as a match and will be removed.
## Examples
Consider the two tables

| TableA | ID  | Value  |
| ------ | --- | ------ |
| TableA | 1   | Apple  |
| TableA | 2   | NULL   |
| TableA | 3   | Banana |

| TableB | ID  | Value  |
| ------ | --- | ------ |
| TableB | 1   | Apple  |
| TableB | 2   | NULL   |
| TableB | 4   | Cherry |
```SQL
-- How INTERSECT handles NULL
SELECT Value
FROM TableA
INTERSECT
SELECT Value
FROM TableB;

-- Returns APPLE and NULL
-- Even though NULL = NULL is fase, set operations treats them as equals

-- How EXCEPT handles NULL
SELECT Value
FROM TableA
EXCEPT
SELECT Value
FROM TableB;

-- Returns BANANA
-- The reason NULL was excluded is the same as above.
```