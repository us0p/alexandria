# SQL USING in SELECT
Simplifies table join operations by allowing developers to specify common columns between tables. It enhances query readability and reduces redundancy by eliminating the need to qualify column names with table aliases.

```SQL
SELECT colmn_list
FROM table1
JOIN table2
USING (common_column);
```
## Common Mistakes
1. Qualifying columns: Do not qualify the column specified in the `USING` clause with a table name or alias.
2. Reusing columns from the `USING` clause in `WHERE` conditions: Avoid referencing the `USING` clause column in `WHERE` conditions without proper handling.
```SQL
-- Incorrect:
SELECT l.location_id, l.street_address, l.postal_code, c.country_name  
FROM locations l JOIN countries c  
USING (country_id)  
WHERE c.country_id = 'IT';

-- Correct:
SELECT l.location_id, l.street_address, l.postal_code, c.country_name  
FROM locations l JOIN countries c  
USING (country_id)  
WHERE country_id = 'IT';
```
## SQL USING in ALTER TABLE
In an `ALTER TABLE` statement (specifically when changing a column's type), `USING` tells PostgreSQL how to convert the existing data from the old type to the new type.

```SQL
ALTER TABLE my_table
ALTER COLUMN my_column TYPE bytea
USING convert_to(my_column::text, 'UTF8');
```

Here, `USING` defines the expression used to transform `my_column` from its current type (e.g., `jsonb`) to the new type (`bytea`).
If you don't use `USING` when it's required (i.e., when PostgreSQL cannot safely cast the types automatically), you'll get a type conversion error.