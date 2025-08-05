## Query Processing
A backend process basically handles all queries issued by the connected client. This backend consists of five subsystems:
1. **Parser**: Generates a parse tree from an SQL statement in plain text.
2. **Analyzer**: Carries out a semantic analysis of a parse tree and generates a query tree.
3. **Re-writer**: Transforms a query tree using the rules stored in the **rule system** if such rules exist.
4. **Planner**: Generates the plan tree that can most effectively be executed from the query tree.
5. **Executor**: Executes the query by accessing the tables and indexes in the order that was created by the plan tree.

![[Pasted image 20250715104222.png]]

![[Pasted image 20250715082318.png]]

Query planner and optimizer adjust with SQL structure changes so can be impacted by changing your query.
## Planner
The planner in PostgreSQL is based on pure cost-based optimization. It does not support rule-based optimization or hints.

>Order of joined relations is insignificant. PostgreSQL has a cots based optimizer so it doesn't matter the position of the statements.

The planer generates a tree with many nodes/steps.

The trees are unique plans that vary the query steps order.

The planner uses the `pg_class` table and `pg_stats` view to create its plan and cost estimates.
![[Pasted image 20250715082741.png]]

## EXPLAIN
In an `EXPLAIN` result, the cost estimate of the sequential scan is dimensionless.

Use it to compare two structures of a query with the same output. Do not use cost to compare queries with different output.

The first cost number describes the startup cost.
The second describes the total cost (startup cost + any additional cost).

The top row and rows with arrows are the plan steps.

```sql
EXPLAIN SELECT * FROM tbl_a WHERE id < 300 ORDER BY data;                          

--                           QUERY PLAN
-- ---------------------------------------------------------------
-- Sort  (cost=182.34..183.09 rows=300 width=8)
--    Sort Key: data
--    ->  Seq Scan on tbl_a  (cost=0.00..170.00 rows=300 width=8)
--          Filter: (id < 300)
-- (4 rows)
```

>Autovacuum cannot `ANALYZE` temporary tables because these tables are only visible to the creating session.

For values that aren't to common, which often represent 5% or less of your data, it's worthy to start looking at indexes. If not, it's not worthy to access and read all of those index pages to find the data.

For more common data the planner will probably choose to use a sequential scan.
## Order of operations
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