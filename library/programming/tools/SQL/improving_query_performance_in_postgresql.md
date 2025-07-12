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