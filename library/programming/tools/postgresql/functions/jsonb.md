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
## `jsonb_typeof`
Used to determine the type of a JSONB value at a particular path or field.

It returns the type as a text string, such as:
- `object`
- `array`
- `string`
- `number`
- `boolean`
- `null`
```PostgreSQL
-- Signature
-- jsonb_typeof(jsonb_value)

SELECT jsonb_typeof('{"a":1}'::jsonb);     -- object
SELECT jsonb_typeof('[1, 2, 3]'::jsonb);    -- array
SELECT jsonb_typeof('"hello"'::jsonb);     -- string
SELECT jsonb_typeof('123'::jsonb);         -- number
SELECT jsonb_typeof('true'::jsonb);        -- boolean
SELECT jsonb_typeof('null'::jsonb);        -- null
```
## `jsonb_object_keys`
Extract the keys from a JSONB object
```PostgreSQL
-- Signature
-- jsonb_object_keys(jsonb_object)

-- Consider a table with the following data
-- | id | config                                                   |
-- | -- | -------------------------------------------------------- |
-- | 1  | '{"theme": "dark", "language": "en", "timezone": "UTC"}' |

SELECT
	id,
	jsonb_object_keys(config) config
FROM settings;

-- The query above will produce the following output:
-- | id | config   |
-- | -- | -------- |
-- | 1  | theme    |
-- | 1  | language |
-- | 1  | timezone |
```
## `jsonb_each`, `jsonb_each_text`
Expands a JSONB object into a set of key-value text pairs:
- `jsonb_each`: Expands a JSONB object into a set of key-value text pairs with values in JSONB format.
- `jsonb_each_text`: Same as above but values are in text format.
```PostgreSQL
-- Signature
-- jsonb_each(jsonb)
-- jsonb_each_text(jsonb)

-- Consider a table with the following data
-- | id  | data                                            |
-- | --- | ----------------------------------------------- |
-- | 1   | '{"name": "Alice", "age": 30, "city": "Paris"}' |
-- | 2   | '{"name": "Bob", "age": 25, "city": "London"}'  |

SELECT
	p.id,
	kv.key k1,
	kv.value v1,
	kv2.key k2,
	kv2.value v2
FROM
	Person p,
	jsonb_each_text(p.data) kv,
	jsonb_each(p.data) kv2;

-- The query above will produce the following output:
-- | id  | k1   | v1     | k2   | v2       |
-- | --- | ---- | ------ | ---- | -------- |
-- | 1   | name | Alice  | name | "Alice"  |
-- | 1   | age  | 30     | age  | 30       |
-- | 1   | city | Paris  | city | "Paris"  |
-- | 2   | name | Bob    | name | "Bob"    |
-- | 2   | age  | 25     | age  | 25       |
-- | 2   | city | London | city | "London" |
```
## `jsonb_array_elements`, `jsonb_array_elements_text`
- `jsonb_array_elements`: Expands a JSONB array into a set of JSONB values, one per element in array.
- `jsonb_array_elements_text`: Same as above but returns text values rather than JSONB values.
```PostgreSQL
-- Signature
-- jsonb_array_elements(jsonb_array)
-- jsonb_array_elements_text(jsonb_array)

-- Consider a table with the following data
-- | id  | data                            |
-- | --- | ------------------------------- |
-- | 1   | '["apple", "banana", "cherry"]' |
-- | 2   | '["x", "y"]'                    |

SELECT
	e.id,
	value,
	t_values
FROM
	Example e,
	jsonb_array_elements(e.data) value
	jsonb_array_elements_text(e.data) t_values;

-- The query above will produce the following output:
-- | id  | value     | t_values |
-- | --- | --------- | -------- |
-- | 1   | "apple"   | apple    |
-- | 1   | "banana"  | banana   | 
-- | 1   | "cherry"  | cherry   |
-- | 2   | "x"       | x        |
-- | 2   | "y"       | y        |
```
## `jsonb_array_length`
Returns the number of elements in a JSONB array.
```PostgreSQL
-- Signature
-- jsonb_array_length(jsonb_array)

-- Consider a table with the following data
-- | id  | data                            |
-- | --- | ------------------------------- |
-- | 1   | '["apple", "banana", "cherry"]' |
-- | 2   | '["x", "y"]'                    |

SELECT
	id,
	data,
	jsonb_array_length(data) data_count
FROM Example e;

-- The query above will produce the following output
-- | id  | tags                         | tag_count |
-- | --- | ---------------------------- | --------- |
-- | 1   | ["sql", "postgres", "jsonb"] | 3         |
-- | 2   | ["plpgsql"]                  | 1         |
-- | 3   | []                           | 0         |
```
## `jsonb_agg`
Set-aggregation function. It takes all the input values from the aggregate group and produces a single **JSONB array** containing those values.
```PostgreSQL
SELECT
	jsonb_agg(id)
FROM (VALUES (1), (2), (3)) t(id);

-- [1, 2, 3]

-- You can aggregate whole rows into JSONB objects
SELECT
	jsonb_agg(to_jsonb(u))
FROM users u;

-- [
--   {"id": 1, "name": "Alice"},
--   {"id": 2, "name": "Bob"}
-- ]

-- You can use it with GROUP BY to collect values per group.
SELECT
	department,
	jsonb_agg(name ORDER BY name) employees
FROM employees
GROUP BY department;

-- [
--   {"department": "HR", "employees": ["Alice", "Bob"]},
--   {"department": "IT", "employees": ["Charlie", "Dave"]}
-- ]
```