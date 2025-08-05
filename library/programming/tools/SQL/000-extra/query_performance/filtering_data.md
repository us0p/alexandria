## Filtering in the WHERE clause
Happens early in the query and reduces the number of rows returned.

When you're filtering your data, create your filters in a way that the query planner produces only a single step so that you can reduce the processing time of your query.

**Example**: Querying for phones codes in different countries.
```PostgreSQL
EXPLAIN
SELECT * FROM phones
WHERE country LIKE 'Ch%'
	OR country LIKE 'In%';
```

The query above can produce the following plan. Note that it performs two steps in the Filter node to satisfy the query provided.
```plaintext
Seq Scan on phones (cost = 0.00..29.05, rows = 13, width = 36)
	Filter: ((country~~'Ch%'::text) OR (coutry~~'In%'::text))
```

Next, you change the query to use a list of values instead of using multiple conditions:
```PostgreSQL
EXPLAIN
SELECT * FROM phones
WHERE country LIKE ANY(ARRAY['Ch%', 'In%']);
```

The query now produces the following plan. Note that now it uses only a single step processing and that the cost of computing it actually is lower.
```plaintext
Seq Scan on phones (cost = 0.00..25.88, rows = 13, width = 36)
	Filter: ((country~~ANY('{Ch%, In%}'::text[]))
```

Separate comparison operator are also treated as a single filter operation by the planner.
## Filtering while joining
While joins are used to combine data, they can also be used to filter data

Because joins are processed after `FROM` clauses, any other filter in the join condition might result in a smaller number of rows in the result.

For example, a `INNER JOIN` will actually reduce the number o lines retrieved based on the match condition. `LEFT` and `OUTER` join will only reduce the number of columns retrieved.

Also, using conditions inside joins or `WHERE` clauses can produce very different in `LEFT` or `OUTER` joins. Specially if the filter condition is in the secondary table.

**Example**: Filtering all appointments while also including male patient data: 
```SQL
SELECT *
FROM appointments a
LEFT JOIN patients p
	ON a.patient_id = p.patient_id
	AND p.sex = 'M';
```
The query above will return all appointment data and only patient data for male patients. The `LEFT JOIN` will only populate columns where patient id matches and the patient is male.

But, if we change the join condition to a `WHERE` clause:
```SQL
SELECT *
FROM appointments a
LEFT JOIN patients p
	ON a.patient_id = p.patient_id
WHERE p.sex = 'M';
```
The query will return only appointment data for patients that are male. 

The join conditions will populate columns where patient id matches.

The `WHERE` condition will remove **all lines** that don't have a male patient data.