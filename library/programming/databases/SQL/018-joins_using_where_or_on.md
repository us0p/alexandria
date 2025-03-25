# JOINS with WHERE or ON
## Extending ON clause
When you apply filters using the `WHERE` clause, all involved tables are going to be filtered.
If you want to filter one or both of the tables before joining them you can extend the `ON` clause:
```SQL
SELECT p.name,
       p.school_name,
       s.address
FROM person p
LEFT JOIN school s ON p.school_name = s.name
                   AND s.rating > 7; -- Adding extra filters on JOIN

```
The query above joins `person` and `schools`, but joins only schools with rating bigger than 7.
It will returns all people but won't display any information about schools with rating below 7, even if with a matching name.

The above `AND` is evaluated before the join occurs. Think of it as a `WHERE` clause that only applies to one of the tables.
## Filtering in the WHERE clause
```SQL
SELECT p.name,
       p.school_name,
       s.address
FROM person p
LEFT JOIN school s ON p.school_name = s.name
WHERE s.rating > 7;
```
The above query is a variation of the former and the difference is that i won't return any school **or** people whose school rating is below seven, the filter is applied **after** the join.