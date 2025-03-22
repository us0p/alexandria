# Logical Operators
## LIKE
Match similar values, instead of exact values.
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
Specify a list of values you'd like to include.
```SQL
SELECT * FROM table_name WHERE age IN (18, 19, 20);

-- Or by using non-numerical lists
-- Note that you can't use Wildcards outside the LIKE operator
SELECT * FROM table_name WHERE name in ('Luan', 'Mari');
```
## AND
Select only rows that satisfy two conditions.
```SQL
SELECT * FROM table_name WHERE year = 2012 AND month_index <= 10;

-- You can chain AND operators
SELECT * FROM table_name WHERE year = 2012 AND month_index <= 10 AND day <= 5;

-- You can use and with other operators
SELECT * FROM table_name WHERE age >= 20 AND name LIKE 'Luan%';
```
## BETWEEN
Select only rows within a certain range. It has to be applied with the `AND` operator.
Note that it includes the range bounds that you specify in the query, in addition to the values between them.
```SQL
SELECT * FROM table_name WHERE age BETWEEN 20 AND 30;

-- It's the same as
SELECT * FROM table_name WHERE age >= 20 AND age <= 30;
```
## IS NULL
Select rows that contain no data in a given column.
```SQL
SELECT * FROM table_name WHERE name IS NULL;
```
## OR
Select rows that satisfy either of two conditions.
```SQL
SELECT * FROM table_name WHERE age = 18 OR age = 30;

-- You can combine AND with OR using parenthesis
SELECT * FROM table_name WHERE name LIKE 'Luan%' AND (age = 18 OR age = 30);
```
## NOT
Select rows that do not match a certain condition. Can be put before any conditional statement to select rows for which that statement is false.
```SQL
SELECT * FROM table_name WHERE year = 2014 AND age NOT BETWEEN 1 AND 16;

-- Usign with other operators
SELECT * FROM table_name WHERE name NOT LIKE 'Luan%';

-- Identifying not null columns
SELECT * FROM table_name WHERE name IS NOT NULL;
```