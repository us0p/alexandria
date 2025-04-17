# Query Processing
A backend process basically handles all queries issued by the connected client. This backend consists of five subsystems:
1. **Parser**: Generates a parse tree from an SQL statement in plain text.
2. **Analyzer**: Carries out a semantic analysis of a parse tree and generates a query tree.
3. **Rewriter**: Transforms a query tree using the rules stored in the **rule system** if such rules exist.
4. **Planner**: Generates the plan tree that can most effectively be executed from the query tree.
5. **Executor**: Executes the query by accessing the tables and indexes in the order that was created by the plan tree.
## Parser
The parser only checks the syntax of an input when generating a parse tree. Therefore, it only returns an error if there's a syntax error in the query.

The parser doesn't check the semantics of an input query. For example, even if the query contains a table name that doesn't exist, the parser doesn't return an error. Semantic checks are done by the analyzer.
## Planner
The planner in PostgreSQL is based on pure cost-based optimization. It does not support rule-based optimization or hints.

As in other RDBMS, the `EXPLAIN` command in PostgreSQL displays the plan tree itself. A specific example is shown below:

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