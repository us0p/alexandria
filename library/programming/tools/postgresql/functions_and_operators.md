# String 
## `string_to_array`
Splits the string at `delimiter` into a **text array**. 
- if delimiter is `NULL`, each character in the string will become a separate element in the array. 
- If delimiter is an empty string then the string is treated as a single field. 
- if `null_string` is supplied and is not `NULL`, fields matching that string are replaced by `NULL`.
```SQL
-- Signature
-- string_to_array(str text, delimiter text [, null_string text]) -> text[]
SELECT string_to_array('asdf;fdsa', ''); -- {asdf;fdsa}
SELECT string_to_array('asdf;fdsa', NULL); -- {a,s,d,f,;,f,d,s,a}
SELECT string_to_array('asdf;fdsa', ';'); -- {asdf,fdsa}
SELECT string_to_array('asdf;fdsa;a', ';', 'a'); -- {asdf,fdsa,NULL}
```
## `split_part`
Splits `str` at occurrences of `delimiter` and returns the `nth` field
```sql
-- Signature
-- split_part(str text, delimiter text, n int) -> text
SELECT split_part('asdf,fdsa', ',', 1); -- 'asdf'
SELECT split_part('asdf,fdsa', ',', 2); -- 'fdsa'
```
# JSON/JSONB
## `to_jsonb`
Takes a PostgreSQL value (like a number, text, array, row, etc.) and converts it into a `JSONB` value.
```SQL
-- Signature
-- to_jsonb(anyelement) -> jsonb
SELECT to_jsonb("hello world"); -- "hello world"
SELECT to_jsonb(42); -- 42
SELECT to_jsonb(true); -- true
SELECT to_jsonb(ARRAY['apple', 'banana']) -- ["apple", "banana"]
SELECT to_jsonb(ROW[1, 'book', true]); -- [1, "book", true]
```