# Logical Operators
- `LIKE`: Match similar values, instead of exact values.
- `IN`: Specify a list of values you'd like to include.
- `BETWEEN`: Select only rows within a certain range.
- `IS NULL`: Select rows that contain no data in a given column.
- `AND`: Select only rows that satisfy two conditions.
- `OR`: Select rows that satisfy either of two conditions.
- `NOT`: Select rows that do not match a certain condition.
## LIKE
```SQL
-- Will fillter all rows where the column name starts with Luan.
SELECT * FROM table_name WHERE name LIKE 'Luan%';
```
Note that the implementation on some databases varies about the case-sensitive property of this operator:
- `SQLite`: Is case-insensitive (matches lower or upper case letters).
- `PostgreSQL`: is case-sensitive (matches only the same characters), must use `ILIKE` if case-insensitive is required.
>Note that `ILIKE` is not part of the SQL standard and thus not every DB engine has an implementation e.g. SQLite.
### Wildcards
- `%`: matches any sequence of zero or more characters.
- `_`: matches any single character.
```SQL
SELECT * FROM table_name WHERE name LIKE 'Lua_';
```
## IN
```SQL
SELECT * FROM table_name WHERE age IN (18, 19, 20);

-- Or by using non-numerical lists
-- Note that you can't use Wildcards outside the LIKE operator
SELECT * FROM table_name WHERE name in ('Luan', 'Mari');
```