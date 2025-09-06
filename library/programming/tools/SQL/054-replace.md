SQL function used to find and replace **all occurrences** of a substring within a string.
```SQL
REPLACE(string_expression, string_to_find, string_to_replace);
```
- `string_expression`: Original string.
- `string_to_find`: Substring you want to search for.
- `string_to_replace`: Substring you want to replace it with.
## Example
```SQL
SELECT REPLACE('Hello World', 'World', 'SQL') AS Result;
-- Hello SQL

SELECT REPLACE('2025 09 01', ' ', '-') AS Result;
-- 2025-09-01
```