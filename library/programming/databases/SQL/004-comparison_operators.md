# Comparison Operators
Are used with `WHERE` and other conditional keywords to determine comparison between values
## Numerical data
| name                  | sign     |
| --------------------- | -------- |
| Equal to              | =        |
| Not equal to          | <> or != |
| Greater than          | >        |
| Less than             | <        |
| Greater or equal to   | >=       |
| Less than or equal to | <=       |
```SQL
SELECT * FROM table_name WHERE age > 15;
```
## Non-numerical data
All of the above operators work on non-numerical data as well.
```SQL
SELECT * FROM table_name WHERE name = 'Luan';
SELECT * FROM table_name WHERE name != 'Luan';
```

The other operators can also be used, they filter based on alphabetical order.
```SQL
-- Return all register that have the name column starting with "L" or further letters.
SELECT * FROM table_name WHERE name >= 'L';
```
## Arithmetic in SQL
Uses the same operators as programming languages (`+, -, *, /`). However, you can only perform arithmetic across columns of the same row.
```SQL
-- Sms age + 100 and renames it to "Centenary"
SELECT age + 100 "Centenary" FROM table_name;

-- As in programming languages you can use parenthese to manage the order of operations
SELECT (age + 2) * 2 "Some random calc" FROM table_name;
```

It occasionally makes sense to use parentheses even when it's not absolutely necessary just to make your query easier to read.