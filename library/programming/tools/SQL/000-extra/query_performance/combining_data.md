## Sub-queries
Can use sub-queries in `SELECT`, `FROM`, and `WHERE` statements.

Sub-queries in `WHERE` statements are dynamic filters.

Using sub-queries in `FROM` clauses decreases readability and limits query plan flexibility. 

In the [query planner](query_plan_and_execution.md), sub-queries in `SELECT` and `WHERE` statements are analogous to joins.

Sub-queries in the `FROM` statement are not, which limits the [optimizer](query_plan_and_execution.md) capacity.
## CTE
Standalone query with temporary results set. Creates a temporary table that is executed only one time.

Temporary tables are advantageous when working with large or complex tables that are resource intensive to query.

Also good to group data to a particular granularity.
## Temporary Tables
Loaded from a query, which means that they are created, loaded and exists for the duration of the database session.

Ultimately, temporary tables comes from data of exiting base tables.

Slow, large tables are usually converted to temporary tables when we constantly need only a small set of that data. Also commonly used in PL/PGSQL scripts.

Temporary tables don't need to execute a query every time it's accessed, like a view does.

Views are similar to tables, but views points to the data, mean while, tables actually materialize and makes data available.

>It's a good practice to add `ANALYZE` after a temporary table creation so we can provide statistics of the table to help the query planner to optimize the queries to this table.
## Standard View
Aren't data storage, but rather stored queries.

Instead of containing data, a view contains a view definition which is directions to the data.

When referencing a query, the view runs the instructions to find and transform the data.

Data comes from existing tables.

**Utility**:
- Combine commonly joined tables.
- Computed columns.
	- Summary metrics.
- Show partial data in a table.
	- Show employees but hide salaries.
## Materialized View
A cross between Standard Views and Temporary Tables.

It's a stored query like a view. But, unlike a view, it contains data. the data comes from a refresh process that runs the view definition in some defined interval.

The refresh process is similar to how base tables are loaded
## Summary of `FROM` clause references
| What              | Why                                      |
| ----------------- | ---------------------------------------- |
| Table             | Base Storage                             |
| Temp Table        | Speeds query using big table             |
| View              | Complicated logic or calculated fields   |
| Materialized view | Complicated logic that slows performance |
If the logic to create a view is complex enough queries referencing this view are slow scheduling data refreshes thus materializing the view fixes this slowness.
Materializing a view retains the complexity of a view and the speed of a table.
## Query Structure Choices
### Sub-queries and Joins
As long as the subqueries occur in the `SELECT` or `WHERE` clauses, the query planner treats them the same as joins.

The order of the query plan is also the same in both of the query structures.
### CTE and Temporary Tables
Additional ways to combine data, especially large data.

In terms of the query plan, CTEs are equivalent to temporary tables.

>Because Postgre inherently uses row storage, limiting the number of records to search and return speeds the query performance. The simplest way to limit the data is by adding filter conditions. Filtering on columns with an Index results in a faster search.

Joins bring together data.

Joining a table that records data at a less granular level will duplicate the values at the lowest granularity.
In this case, aggregating in a CTE prior to joining results in faster execution time.

Ideally, the query plan limits the number of records as soon as possible. Putting a filter in the CTE may restrict the query planner's ability to perform this filter condition early so may result in a larger number of rows still being present further down the query plan.