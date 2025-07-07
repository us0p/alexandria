# Predicate Pushdown
Database optimization technique. Improve query performance by filtering data before transfer and reducing the amount of data that needs to be processed and retrieved during query execution.

In a relational database management system (DBMS), queries are composed of various operations such as filtering (applying conditions), joining tables, and projecting (selecting specific columns).

Predicate pushdown specifically focuses on optimizing the filtering aspect. It enables engineers to apply filters to the data sources so the entire database does not need to be scanned during query execution.
### How Predicate Pushdown Works
When you submit a query, the database needs to process that query and retrieve the required data.

If the query involves filtering conditions or predicates, such as WHERE clauses, they are normally evaluated after the data is fetched. This means that the database retrieves all the rows from the table and then applies the filters to discard the irrelevant rows, resulting in unnecessary data processing.

Predicate pushdown works by reorganizing the execution process so that filters are pushed down closer to the data sources (the tables) before the data is retrieved. So when executing SQL queries, only the necessary datasets are scanned and processed.

This optimization is beneficial when dealing with larger datasets, as it minimizes the amount of data that needs to be read from disk, transferred across networks, or loaded into memory.

Here’s how predicate pushdown works in SQL databases:
- **Query Parsing and Analysis:** When an SQL query is submitted to the database, it is parsed, and the database optimizer analyzes it to determine the most efficient way to retrieve the data.
- **Optimization:** The optimizer considers various execution plans and evaluates filter predicates. It identifies filters in the WHERE clause that can be applied to the table or index scan operations.
- **Predicate Pushdown:** The optimizer restructures the execution plan to push down the filtering conditions to the appropriate source. For example, if a query involves filtering rows based on a specific condition, the optimizer can apply the condition during a table scan or index lookup to reduce the amount of data retrieved.
- **Data Retrieval:** With the optimized execution plan, the database system retrieves only the required data based on the applied predicates. This helps greatly reduce network traffic and the amount of data transferred, minimizing disk I/O operations.
- **Subsequent Operations:** After the data retrieval, any remaining operations, like joins, projections, and aggregations, are performed on the reduced dataset.
## When might not work
- If the predicate depends on **computed values** (e.g. `WHERE ABS(amount) > 100`), the database may not push it.
- **Non-deterministic functions** (`random()`, `now()`) may prevent pushdown.
- **Materialized CTEs or subqueries** that the planner can’t optimize through.