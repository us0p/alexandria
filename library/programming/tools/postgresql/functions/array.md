##  `unnest`
Expand an array into a set of rows, essentially flattening the array so each element becomes its own row.
```PostgreSQL
-- Signature
-- unnest(array)

SELECT unnest(ARRAY[1, 2, 3]) numbers;

-- The query above will produce:
-- | numbers |
-- | ------- |
-- | 1       |
-- | 2       |
-- | 3       |
```
##  `array_dims`
Returns the dimensions of an array. It tells you the size of each dimension in the form of a string like `[lower:upper]`.
```PostgreSQL
-- Signature
-- array_dims(array)

SELECT array_dims(array[1, 2, 3]) -- [1:3] -> 1 dimensional array starting at index 1 and ending at index 3.

SELECT array_dims(array[[1,2], [3,4]]) -- [1:2][1:2] -> 2 dimensional array having 2 rows from idx 1 to 2, second dimension also has 2 rows from idx 1 to 2.
```
## `array_length`
Returns the length of a specified dimension of an array.
```PostgreSQL
-- Signature
-- array_length(array, dimension)

SELECT 
	array_length(array[[1,2], [3,4]], 1) rows, -- len of 1st dimension, rows
	array_length(array[[1,2], [3,4]]), 2) cols,	-- len of 2nd dimension, cols
	array_length(array[]::int[], 1) null_check; -- returns NULL for empty array

-- The query above will produce:
-- | rows | cols | null_check |
-- | ---- | ---- | ---------- |
-- | 2    | 2    | NULL       |
```
## `cardinality`
Returns the number of elements in an array
```PostgreSQL
-- Signature
-- cardinality(array)

SELECT cardinality(array[1, 2, 3]); -- 3

SELECT cardinality(array[]::int[]); -- 0, returns 0 for empty arrays

SELECT 
	array_length(array[[1,2], [3,4]], 1), -- 2 rows
	cardinality(array[[1,2],[3,4]]); -- 4, returns the total number of elmeents, regardless of shape
```
## `array_append`
Add a new element to the end of an array.

The data type of the appended element must match the array's element type.
```PostgreSQL
-- Signature
-- array_append(array, element)

SELECT array_append(array[1, 2], 3); -- {1, 2, 3}

SELECT array_append(array[1, 2], NULL); -- {1, 2, NULL}
```
## `array_position`, `array_positions`
- `array_position`: Returns the index (1-based) of the first occurrence of a given element in an array. If the element is not found, it returns NULL.
- `array_positions`: Same as above, but return all occurrences of the element in the array.
```PostgreSQL
-- Signature
-- array_position(array, element)
-- array_positions(array, element)

SELECT array_position(array[1, 2, 3, 4], 3); -- returns idx 3
SELECT array_position(array[1, 2, 3, 4], 5); -- NULL

SELECT array_positions(array[1, 2, 1, 3, 4], 1); -- {1, 3} returns all occurrences for element 1 at idx 1 and 3.
```
## `array_agg`
Builds an array from a **set** of input values.

It's specially useful when you want to group rows and collect values **into an array** per group.
```PostgreSQL
-- Signature
-- array_agg(expression)

SELECT array_agg(name) FROM employees; -- {Alice, Bob, Carol, Dave}

-- With GROUP BY
SELECT 
	department, 
	array_agg(DISTINCT name ORDER BY name) -- Ensures name are unique and sorted
FROM employees
GROUP BY department;

-- Out put would be:
-- department   |     employees
-- -------------+-----------------------
-- HR           | {Alice, Bob}
-- Engineering  | {Carol, Dave, Eve}
-- Sales        | {Frank}

```