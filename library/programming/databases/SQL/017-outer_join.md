# OUTER JOIN
Are joins that return matched values and unmatched values from either or both tables.
The behavior of repeating rows of one table, to represent multiple matches in the other is the same of `INNER JOIN`.
## LEFT JOIN
Returns matched rows in both tables as well as **unmatched rows from the left table**.
![[Pasted image 20250323201545.png]]

```SQL
-- Returns all the rows in the table person, even those that doesn't have the "school_name" attribute.
-- Returns only the schools that have a match.
SELECT p.name,
       p.school_name,
	   s.address
FROM person p
LEFT JOIN school s ON p.school_name = s.name;

-- Can also be written as
SELECT p.name
	   p.school_name,
	   s.address
FROM person p
LEFT OUTER JOIN school s ON p.school_name = s.name;
```
## RIGHT JOIN
Returns all rows from the **joined table** and **only matching rows from the table in the `FROM` clause**.
![[Pasted image 20250324145718.png]]

```SQL
-- Returns all the rows in the table school, even those that doesn't have a matching person.
-- Returns only the people that have a match.
SELECT p.name,
	   p.school_name,
	   s.address
FROM person p
RIGHT JOIN school s ON p.school_name = s.name;

-- Can also be written as
SELECT p.name
	   p.school_name,
	   s.address
FROM person p
RIGHT OUTER JOIN school s ON p.school_name = s.name;
```
## FULL OUTER JOIN
Returns all rows from both tables, **matched and unmatched**. It's commonly used in conjunction with aggregations to understand the amount of overlap between two tables.

Can also be written as `FULL OUTER JOIN`
```SQL
SELECT 
	-- Count the number of people that didn't had a school
	COUNT(
		CASE WHEN p.school_name IS NOT NULL 
		     AND s.name IS NULL 
		THEN p.shool_name 
		ELSE NULL END
	) person_only,
	-- Count the number of people that had a school
	COUNT(
		CASE WHEN p.school_name IS NOT NULL 
		     AND s.name IS NOT NULL 
		THEN p.shool_name 
		ELSE NULL END
	) person_and_schools,
	-- Count the number of schoolc that didn't had any people
	COUNT(
		CASE WHEN p.school_name IS NULL 
		     AND s.name IS NOT NULL 
		THEN s.name 
		ELSE NULL END
	) schools_only,
FROM person p
FULL JOIN school s ON p.school_name = s.name;
```