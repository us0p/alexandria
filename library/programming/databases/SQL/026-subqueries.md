# Writing Subqueries in SQL
Subqueries aka Inner queries or Nested queries, are a tool for performing operations in multiple steps.
Subqueries can be used in several places within a query, let's start with the `FROM` statement:
```SQL
SELECT p.*
FROM (
	SELECT *
	FROM person
	WHERE person.age > 30;
) p
WHERE p.age < 40;
```
First, the database runs the inner query. Once the inner query runs, the outer query will run using the results from the inner query as its underlying table.

Subqueries are required to have names.

>Your inner query must actually run on its own, as the database will treat it as an independent query.
## Using subqueries to aggregate in multiple stages
The example above could be solved simply by adding more conditions to the `WHERE` clause.
Subqueries are the best tool for when you have two or more steps in the process. Each step is treated by one query:
```SQL
SELECT 
	month,
	AVG(births_per_week)
FROM (
	SELECT 
		EXTRACT('month' FROM birth) AS month,
		EXTRACT('week' FROM birth) AS week,
		COUNT(*) births_per_week
	FROM person
	GROUP BY 1, 2
) p
GROUP BY 1;
```
## Subqueries in conditional logic
You can use subqueries in conditional logic `WHERE`, `JOIN/ON`, or `CASE` statements.
```SQL
-- Returns all the people with the earliest birth day known.
SELECT * FROM person WHERE birth = (SELECT MIN(birth) FROM person);
```

The above query works because the result of the subquery is only one cell. However, `IN` is the only type of conditional logic that will work when the inner query contains multiple results:
```SQL
-- Return all people with the same birth day as the first 5 early birth days in the table.
SELECT 
	* 
FROM person 
WHERE birth IN (
	SELECT 
		birth 
	FROM person 
	ORDER BY birth 
	LIMIT 5
);
```

Note that you should not include an alias when you write a subquery in a conditional statement as the subquery is treated as an individual value rather than as a table.
## Joining subqueries
The following query produces the same result as the previous example:
```SQL
SELECT 
	*
FROM person p
JOIN (
	SELECT
		birth
	FROM person
	ORDER BY birth
	LIMIT 5
) sub ON p.birth = sub.birth
```
You can also use subqueries to improve the performance of queries, specially in the case of [cartesian products](cartesian_problem.md). You can use subqueries to perform calculation on much smaller datasets and then join then together avoiding calculation in the full product which would take much longer time.
```SQL
-- Pretty slow query, COUN(DISTINCT ...) will run on every result of the cartesian product.
SELECT COALESCE(acquisitions.acquired_month, investments.funded_month) AS month,
       COUNT(DISTINCT acquisitions.company_permalink) AS companies_acquired,
       COUNT(DISTINCT investments.company_permalink) AS investments
  FROM tutorial.crunchbase_acquisitions acquisitions
  FULL JOIN tutorial.crunchbase_investments investments
    ON acquisitions.acquired_month = investments.funded_month
 GROUP BY 1

-- Same query with improved performance, using sub queries to perform calculation on smaller sets and then performing the product.
SELECT COALESCE(acquisitions.month, investments.month) AS month,
       acquisitions.companies_acquired,
       investments.companies_rec_investment
  FROM (
        SELECT acquired_month AS month,
               COUNT(DISTINCT company_permalink) AS companies_acquired
          FROM tutorial.crunchbase_acquisitions
         GROUP BY 1
       ) acquisitions

  FULL JOIN (
        SELECT funded_month AS month,
               COUNT(DISTINCT company_permalink) AS companies_rec_investment
          FROM tutorial.crunchbase_investments
         GROUP BY 1
       )investments

    ON acquisitions.month = investments.month
 ORDER BY 1 DESC
```
## Sub queries and UNIONs
You can use `UNION` to create virtual tables that can be used to query data, this is specially useful if you data set is divided into parts, in which case you can `UNION ALL` the parts in a sub query and them perform queries in the data set as a whole rather its parts.
```SQL
SELECT COUNT(*) AS total
FROM (
	SELECT * FROM peson_part1
	UNION ALL
	SELECT * FROM person_par2
) sub;
```