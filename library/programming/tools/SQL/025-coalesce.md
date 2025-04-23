# COALESCE
Takes one or more arguments and returns the first non-null argument.

If all inputs are `NULL` it returns `NULL`.
```SQL
-- Returns second parameter when name is NULL
SELECT COALESCE(name, 'No name') FROM person;
```