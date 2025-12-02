# Data Types
It's the type of the data stored in each column of your table.
There are a lot of data types, and each database provider might have it's own specifications about each type, you should follow the database specification about supported datatypes and their names.
- [SQLite Data Types Docs](https://www.sqlite.org/datatype3.html)
- [PostgreSQL Data Types Docs](https://www.postgresql.org/docs/17/datatype.html)
## Composite Key
Is a primary key composed of multiple columns. Each column in the composite key can contain duplicate values, but the combination of all the columns in the composite key must be unique.
## Changing a column's data type
It's possible to change the data type of a column in your query. This is done by using `CAST` clauses.
```SQL
-- In the following example, "date" is stored as string
SELECT CAST(p.birth AS DATE) FROM person p;
```

Each database provider can also have built-in functions that convert one data type to another, it's worth to take a look at your provider documentation.
## JSON and JSONB
`JSON` and `JSONB` accept almost identical sets of values as input. The major practical difference is efficiency.
- `JSON`: Stores an exact copy of the input, which processing functions must reparse on each execution.
- `JSONB`: Stored in decomposed binary format that makes it slightly slower to input due to added conversion overhead, but significantly faster to process, since no reparsing is needed. `JSONB` also supports indexing, which can be a significant advantage.

Also, `JSONB` removes duplicated keys and unnecessary spaces in the string representation, which makes it more compact.
## JSON Operators
In the example bellow all operators used in JSON are also available for JSONB.
```PostgreSQL
-- '->' Get JSON array element (indexed from zero, negative integers count from the end).
'[{"a": "foo"}, {"b": "bar"}, {"c": "baz"}]'::json->2 -- {"c":"baz"}

-- '->' Get JSON object field by key
'{"a": {"b": "foo"}}'::json->'a' -- {"b": "foo"}

-- '->>' Get JSON array element AS text
'[1,2,3]'::json->>3 -- 3

-- '->>' Get JSON array elements starting from the back
'[1,2,3]'::jsonb ->> -1 -- 3

-- '->>' Get JSON object field AS text
'{"a": 1, "b": 2}'::json->>'b' -- 2

-- '#>' Get JSON object at specified path. Expects an array in the right side of the operand
'{"a": {"b": {"c": "foo}}}'::json#> '{a,b}' -- {"c": "foo"}

-- '#>>' Get JSON object at specified path. Also expects an array in the right side of the operand
'{"a": [1,2,3], "b": [4,5,6]}'::json#>>'{a,2}' -- 3
```
## JSONB only operators
```PostgreSQL
-- '@>' Does the left JSON value contains the right JSON path/values entries at the top level?
'{"a": 1, "b": 2}'::jsonb @> '{"b": 2}'::jsonb -- true

-- '<@' Are the left JSON path/value entries contained at the top level within the right JSON?
'{"b": 2}'::jsonb <@ '{"a": 1, "b": 2}'::jsonb -- true

-- '?' Does the string exist as a top-level key within the JSON value?
'{"a": 1, "b": 2}'::jsonb ? 'b' -- true

-- '?|' Do any of these array strings exist as top-level keys?
'{"a": 1, "b": 2, "c": 3}'::jsonb ?| array['b', 'c'] -- true

-- '?&' Do all of these array strings exist as top-level keys?
'["a", "b"]'::jsonb ?& array['a', 'b']

-- '||' Concatenate two jsonb values into a new jsonb value
'["a", "b"]'::jsonb || '["c", "d"]'::jsonb -- '["a", "b", "c", "d"]'

-- '-' delete key/value pair or string element from left operant.
'{"a": "b"}'::jsonb - 'a' -- '{}'

-- '-' delete the array element with specified index. Throws an error if top level container is not an array
'["a", "b"]'::jsonb - 1 -- '["a"]'

-- '#-' delete the field of element with specified path
'["a", {"b": 1}]'::jsonb #- '{1,b}' -- '["a", {}]'
```
## ARRAY
Array literal definition `'{{"a", "b", "c"},{"d", "e", "f"}, {"g", "h", "i"}}'` this is an multidimensional array, multidimensional arrays must have matching extents for each dimension. A mismatch causes an error.

Another of constructing an Array is `ARRAY[1,1,1,1]`.

Access a single element of an array: `array_column[1]`.

By default PostgreSQL uses a one-based numbering convention for arrays.

We can also access arbitrary rectangular slices of an array, or sub-arrays:

```PostgreSQL
-- This query retrieves the first item on Bill's schedule for the first two days of the week.
SELECT schedule[1:2][1:1] FROM sal_emp WHERE name = 'Bill';
```

If any dimension is written as a slice, then all dimensions are treated as slices. Any dimension that has only a single number is treated as being from 1 to the number specified.
```PostgreSQL
-- [2] is treated as [1:2], as in this example
SELECT schedule[1:2][2] FROM sal_emp WHERE name = 'Bill';
```

An array subscript expression will return null if either the array itself or any of the subscript expressions are null. Also, null is returned if a subscript is outside the array bounds.

New array values can also be constructed using the concatenation operator `||`:
```PostgreSQL
-- '||' Concatenate elements or arrays to other array.
SELECT ARRAY[1,2] || ARRAY[3,4]; -- {1,2,3,4}

SELECT ARRAY[1,2,3] || ARRAY[[4,5,6],[7,8,9]] -- {{1,2,3},{4,5,6},{7,8,9}}

SELECT 3 || ARRAY[4,5,6] -- {3,4,5,6}

SELECT ARRAY[4,5,6] || 7 -- {4,5,6,7}


-- '@>' Contains
SELECT ARRAY[1,4,3] @> ARRAY[3,1,3] -- true

-- '<@' Is contained by
SELECT ARRAY[2,2,7] <@ ARRAY[1,7,4,2,6] -- true

-- '&&' overlap (have elements in common)
SELECT ARRAY[1,4,5] && ARRAY[2,1] -- true
```

Note that the concatenation operator actually creates a new array to handle all the values.

To search for a value in an array:
```PostgreSQL
-- Returns any rows where pay_by_quarter includes 10000
SELECT * FROM sal_emp WHERE 10000 = ANY (pay_by_quarter);
```