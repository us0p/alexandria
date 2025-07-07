You can use the `EXPLAIN` command to see what query plan the planner creates for any query.

The structure of a query plan is a tree of plan nodes.

Nodes at the bottom level of the tree are scan nodes, they return raw rows from a table.

There are different types of scan nodes for different table access methods:
	- Sequential scans
	- Index scans
	- Bitmap index scans

There are also non-table row sources, such as `VALUES` clauses and set-returning functions in `FROM`, which have their own scan node types.

If the query requires:
- Joining
- Aggregation
- Sorting
Or other operations on the raw rows, then there will be additional nodes above the scan nodes to perform these operations.

The output of `EXPLAIN` has one line for each node in the plan tree, showing the basic node type plus the cost estimates that the planner made for the execution of that plan node.

Additional lines, indented from the node's summary line, show additional properties of the node. The very first line (the summary line) has the estimated total execution cost for the plan.
## Example
```SQL
EXPLAIN SELECT * FROM tenk1;

--                           QUERY PLAN
-- ----------------------------------------------------------------
--  Seq Scan on tenk1  (cost=0.00..445.00 rows=10000 width=244)
```
Since this query has no `WHERE` clause, it must scan all the rows of the table.

The numbers from left to right:
- Estimated start-up cost. This is the time expended before the output phase can begin, e.g., time to do the sorting in a sort node.
- Estimated total cost. This is stated on the assumption that the plan node is run to completion, i.e., all available rows are retrieved. In practice a node's parent node might stop short of reading all available rows (e.g with `LIMIT`).
- Estimated number of rows output by this plan node. Again, the node is assumed to be run to completion.
- Estimated average row size output by this plan node (in bytes).

>The costs are measured in arbitrary units determined by the **planner's cost parameter**. Traditional practice is to measure the costs in units of disk page fetches. That is, `seq_page_cost` is conventionally set to `1.0` and the other cost parameters are set relative to that.

>The cost of an upper-level node includes the cost of all its child nodes. Also, cost only reflects things that the planner cares about, it doesn't consider the time spent to convert output to text or to transmit them to the client. Those costs are ignored because it cannot change them by altering the plan.

>The `rows` value is not the number of rows processed or scanned by the plan node, but rather the number emitted by the node. Ideally the top-level rows estimate will approximate the number of rows actually returned, updated, or deleted by the query.

```SQL
EXPLAIN SELECT * FROM tenk1 WHERE unique1 < 7000;

--                           QUERY PLAN
-- ----------------------------------------------------------------
--  Seq Scan on tenk1  (cost=0.00..470.00 rows=7000 width=244)
--      Filter: (unique1 < 7000)
```

Notice that `EXPLAIN` shows the `WHERE` clause being applied as a "filter" condition attached to the Seq Scan plan node. This means that the plan node checks the condition for each row it scans, and   outputs only the ones that pass the condition.

The estimate of output rows has been reduced because of the `WHERE` clause. However, the scan will still have to visit all 10000 rows. So the cost in fact has gone up a bit  to reflect the extra CPU time spent checking the `WHERE` condition.

- Index Scan: visits an index to find the locations of rows matching the index condition.
- Heap Scan: Physically visits the values of an index to find the values of the row's locations identified by the Index Scan.
- Bitmap: Mechanism does the sorting of some scan (e.g. Bitmap Index Scan).
- Sort: Represent the sorting of the data set by some criteria.
- Incremental Sort: Used when part of the plan guarantees an ordering on a prefix of the required sort keys. It further the data set.
- BitmapAnd/BitmapOr: Can be used to combine indexes if there are indexes on several columns in the `WHERE`.


- Table rows fetched in index order are expensive to read because rows are fetched separately. By sorting the row physical locations before reading the planner can minimize the cost of separate fetches