Query Planner
- Query: SQL instructions.
- Query Execution Plan: Actual steps to execute the instructions.

Queries are not processed in a given written order.

Joins are a way of combining data.

Alternative methods to combining data are:
- Sub-queries
- Common Table Expressions (CTE)
## Sub-queries
Can use sub-queries in `SELECT`, `FROM`, and `WHERE` statements.

Sub-queries in `WHERE` statements are dynamic filters.

Using sub-queries in `FROM` clauses decreases readability and limits query plan flexibility. In the query planner, sub-queries in `SELECT` and `WHERE` statements are analogous to joins. Sub-queries in the `FROM` statement are not, which limits the optimizer capacity.
## CTE
Standalone query with temporary results set. Creates a temporary table that is executed only one time.

Temporary tables are advantageous when working with large or complex tables that are resource intensive to query.
## Temporary Tables
Available only during the database session.
Available to multiple distinct queries.

Slow, large tables are usually converted to temporary tables when we constantly need only a small set of that data.

Views are similar to tables, but views points to the data, mean while, tables actually materialize and makes data available.

Temporary tables don't need to execute a query every time it's accessed, like a view does.

Referencing the same table multiple times is inefficient and slow. Instead, you can create a temp table of the common, large, table. The table is available in memory and it's available to subsequent CTE joins to this table.

It's a good practice to add `ANALYZE` after a temporary table creation so we can provide statistics of the table to help the query planner to optimize the queries to this table.
## Algebra order of operations
- Lexical (as written)
- Logical (as executed)

The order queries are written (Lexical) is different from order queries are executed (Logical).

**Table with logical order of operations**

| Order | Clause              |
| ----- | ------------------- |
| 1     | FROM                |
| 2     | JOIN                |
| 3     | WHERE               |
| 4     | GROUP BY            |
| 5     | SUM(), COUNT(), etc |
| 6     | SELECT              |
| 7     | DISTINCT            |
| 8     | ORDER BY            |
| 9     | LIMIT               |
Queries requires aggregate functions and GROUP BY clauses to have the same level of granularity.
## Filtering in the WHERE clause
Happens early in the query and reduces the number of rows returned.

There are several ways of filtering data to produce the same result set. Depending on how the filter is structured the query planner can apply the filters separately incurring more processing time.

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
### Data types advantages
Numeric vs Text
- Numbers have shorter lengths
- Number occupy less storage
- Speeds performance

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
## Why and When to aggregate data
Each row of a table is unique based on the granularity or the level of detail.

The level of detail can come from one or more columns.

![[Pasted image 20250709161847.png]]

In the following table, `game` is the lowest level of granularity. It's a column that describes an unique record. Since each game also has a unique `id`, the `id` column also describes an unique record.

![[Pasted image 20250709162025.png]]

Considering the two tables, there are multiples rows per game, so `game` is no longer the table grain.

Instead, `game` and `platform` together describes each unique row. So now two columns are needed to describe the granularity, `game_id` and `platform`.
## Joining different granularities
To avoid duplicates and improve query performance, you need to aggregate tables to the same level of detail before joining them.

CTE are useful to aggregate data before performing joins.

Suppose you want to know the number of platforms for each game, and the last platform the game was available.

![[Pasted image 20250709162451.png]]

In the case of Legend of Zelda, we can see that it maps to multiples platforms in the platforms table.

![[Pasted image 20250709162635.png]]

Instead of selecting a single game most recent platform you've added records for each platform for that game.

The Legend of Zelda went from 1 record in the game's table to the 3 record shown here.

The output table is now of the `Game_Platforms` grain.
### Setting up a granularity change
To return the results in the `Video_Games` table grain, you can turn the query into two steps.
1. Sets the stage for easy identification of the most recent year platform by aggregating the data from `Game_Platforms` to represent what we want: **The number of platforms for each game and the last platform the game was available**.
```SQL
SELECT
	game_id,
	platform,
	year,
	COUNT(platform) AS no_platforms,
	MAX(year) AS last_platform_yr
FROM game_platforms
GROUP BY game_id, platform, year;
```

![[Pasted image 20250709163045.png]]
2. Query the `Video_Games` table to get only the data we want and joins it with the aggregated result we have.
```PostgreSQL
WITH platform_cte AS (
	SELECT
		game_id,
		platform,
		year,
		COUNT(platform) AS no_platforms,
		MAX(year) AS last_platform_yr
	FROM game_platforms
	GROUP BY
		game_id,
		platform,
		year
)
SELECT
	g.id,
	g.game,
	cte.no_platforms,
	cte.platform AS last_platform
FROM video_games g
JOIN platforms_cte cte
	ON g.id = cte.game_id
	AND cte.last_platform_yr = cte.year;
```

The query above will return only a single row, following the granularity that we expected, avoiding duplicated data and duplicated calculations, reducing the result size to the minimum required number of records.

![[Pasted image 20250709163738.png]]
## Tables
Organized storage that contain data.

They have an ETL process that loads the data into the storage space.
## Temporary Table
Generally mirror base tables they organized storage with data.

Loaded from a query, which means that they are created, loaded and exists for the duration of the database session.

Ultimately, temporary tables comes from data of exiting base tables.
## Standard View
Aren't data storage, but rather stored queries.

Instead of containing data, a view contains a view definition which is directions to the data.

When referencing a query, the view runs the instructions to find and transform the data.

Data comes from existing tables.
### Utility
- Combine commonly joined tables.
- Computed columns.
	- Summary metrics.
- Show partial data in a table.
	- Show employees but hide salaries.
## Materialized View
A cross between Standard Views and Temporary Tables.

It's a stored query like a view. But, unlike a view, it contains data. the data comes from a refresh proccess that runs the view definition in some defined interval.

The rerfesh process is simmilar to how base tables are loaded
## Summary of `FROM` clause references
| What              | Why                                      |
| ----------------- | ---------------------------------------- |
| Table             | Base Storage                             |
| Temp Table        | Speeds query using big table             |
| View              | Complicated logic or calculated fields   |
| Materialized view | Complicated logic that slows performance |
If the logic to create a view is complex enough queries referencing this view are slow scheduling data refreshes thus materializing the view fixes this slowness.
Materializing a view retains the complexity of a view and the speed of a table.
## Row-oriented storage and partitions
Database stores data into two main formats:

**Row oriented storage**: Relation between columns is retained. Which means that one record is composed of all the columns for that one row.
![[Pasted image 20250714083656.png]]

**Column oriented storage**: Relation between rows is retained. Which means that one record is all the rows for one column.
![[Pasted image 20250714083808.png]]

Notice how all zoo animal names are stored together and how species are stored together across many rows.

However, the relationship between the name and species is lost in column storage.

>PostgreSQL inherently uses row oriented storage.
## Row Oriented Storage
Because all columns for one row are stored together, it's fast to append or delete whole rows. Additionally, a query to return one column, is as fast as a query to return all columns.

The number of rows returned impacts query speed, so returning all rows is slow.
## Partitions
Method os splitting one (parent) table into many, smaller (children) tables.
## Indexes
Method of creating sorted column keys to improve search.

>Partitions and Indexes require setup and maintenance from DBA.

Any column, or combinated columns can be an Index or a Partition.

>Database administrator should document this in a database diagram.
## Partition Structure
Exists in a parent table that is visible in a database front end and it's the table you reference in queries and it's the table that contains all information.

The Animals table is partitioned on animal habitat. Each continent is its own child table. This continent tables, aren't visible on the front end, but are visible to queries.

Partitions are referenced the same as any filter condition using the `WHERE` clause.
```PostgreSQL
SELECT species
FROM zoo_animals
WHERE habitat = 'Africa';
```

![[Pasted image 20250714084535.png]]
**Parent Table**:
- Visible in database front end
- Write queries
**Children Tables**:
- Not visible in database front end
- Queries search

Partitions split one table into many smaller tables.

- Provide storage flexibility: Each child table can be stored on a different server, with seldom-used partitions on cheaper, slower storage options.
- Faster queries: Because the main table is functionally split, referencing a partition allows the query to search a subset of rows, speeding the search.
- Are often on common filter conditions, such as date or location columns.
## Index Overview
 Creates sorted column keys to improve search.
 - Similar to book index.
 - Reference to data location.
### Why
- Faster Queries: Searching ordered keys instead of the raw data is faster.
### Where
- Common filter columns such as date or location.
- Primary Key
![[Pasted image 20250714091849.png]]

You can see four values for fried rice sorted together in the index.

When you query the cookbook table, the query looks at this ordered index table. The query quickly finds all the fried rice entries because they are together. The query uses the corresponding pointer values to find the fried rice rows in the original cookbook table.

Searching a sorted, grouped index is faster than searching each row of the cookbook table.

Anyone can find existing indexes with a query. `pg_tables` schema is similar to `information_schema` and is specific to PostgreSQL. This schema contains views with metadata about the database.

`pg_indexes` is a view that contains all the indexes. It list the schema, table, index name, storage location, and the index creation SQL statement.

Use an index:
- Large tables
- Common filter conditions
- Often used on Primary Keys
Avoid an index
- Small tables
- Columns with many nulls
- Frequently updated tables
	- Index will become fragmented
	- Writes data in two places
![[Pasted image 20250714092801.png]]

Notice how `basil` is not grouped with other recipes of `spaghetti & meatballs`. This is index fragmentation.

This can be fixed by re-indexing the table, but it is an additional processing step.
## Using Column Oriented Storage
This type of storage is ideal for analytics.
- One column stored in same location.
- Quick to return all rows.
- Fast to perform column calculations.

Because one column is stored in the same location, queries to return all rows are quick.

Calculations using all rows from a single column are also quick.

Column oriented storage is not well suited for transactional database need. This storage retains the relationship between rows for a single column.
- Slow to return all columns
- Slow to load data.

Because a whole row is not stored in the same location, queries to return all columns are slow.

Loading data is also slow since data is usually loaded on a row basis.

Transactional databases focuses on inserting and deleting records quickly.

Common examples of column oriented storage databases:

| Database Server | Solution                               |
| --------------- | -------------------------------------- |
| PostgreSQL      | Citus Data, Greenplum, Amazon Redshift |
| MySQL           | MariaDB                                |
| Oracle          | Oracle In-Memory Cloud Store           |
| Multiple RDMS   | Clickhouse, Apache Druid, CrateDB      |
As always, with large data, limiting the number of columns returned will improve performance.

You can limit columns by using `SELECT *` sparingly.

Instead, use the `information_schema` to explore data.

Work through calculations for the columns of interest in individual queries.

```PostgreSQL
-- Structured for column oriented
-- Operates only in a small number of columns
SELECT
	MIN(age),
	MAX(age)
FROM zoo_animals
WHERE species = 'zebra';

-- Structured for row-oriented
-- Same query but return all columns.
SELECT *
FROM zoo_animals
WHERE species = 'zebra'
ORDER BY age;
```

![[Pasted image 20250715082318.png]]

Query planner and optimizer adjust with SQL structure changes so can be impacted by changing your query.

The planer generates a tree with many nodes/steps.

The trees are unique plans that vary the query steps order.

The planner uses the `pg_class` table and `pg_stats` view to create its plan and cost estimates.
![[Pasted image 20250715082741.png]]
## EXPLAIN
In an `EXPLAIN` result, the cost estimate of the sequential scan is dimensionless.

Use it to compare two structures of a query with the same output. Do not use cost to compare queries with different output.

The first cost number describes the startup cost.
The second describes the total cost (startup cost + any additional cost).
### Seq Scan
Scan all rows in the table.

The top row and rows with arrows are the plan steps.
## Query Structure Choices
### Sub-queries and Joins
As long as the subqueries occur in the `SELECT` or `WHERE` clauses, the query planner treats them the same as joins.

The order of the query plan is also the same in both of the query structures.
### CTE and Temporary Tables
Additional ways to combine data, especially large data.

In terms of the query plan, CTEs are equivalent to temporary tables.

>Because Postgres inherently uses row storage, limiting the number of records to search and return speeds the query performance. The simplest way to limit the data is by adding filter conditions. Filtering on columns with an Index results in a faster search.

Joins bring together data.

Joining a table that records data at a less granular level will duplicate the values at the lowest granularity.
In this case, aggregating in a CTE prior to joining results in faster execution time.

Ideally, the query plan limits the number of records as soon as possible. Putting a filter in the CTE may restrict the query planner's ability to perform this filter condition early so may result in a larger number of rows still being present further down the query plan.

![[Pasted image 20250715104222.png]]