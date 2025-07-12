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

- Index Scan: visits an index to find the locations of rows matching the index condition can serve as an ordering step if the order rows are filter is already the expected order.
- Heap Scan: Physically visits the values of an index to find the values of the row's locations identified by the Index Scan.
- Bitmap: Mechanism does the sorting of some scan (e.g. Bitmap Index Scan).
- Sort: Represent the sorting of the data set by some criteria.
- Incremental Sort: Used when part of the plan guarantees an ordering on a prefix of the required sort keys. It further the data set.
- BitmapAnd/BitmapOr: Can be used to combine indexes if there are indexes on several columns in the `WHERE`.
- Limit: Limits the number registers retrieved, it can reduce the number of units of computations in terms of disk reads.
- Nested Loop: Runs the inner child once for each row obtained from the outer child (the latest node in the Nested Loop plan). The costs of the loop are the cost of the outer scan plus one repetition of the inner scan.
- Filter: Represents the application of a filter into the data set.
- Join: Represents the union of two datasets, usually used with some other operation that can only be applied **after** the datasets are combined.
- Materialize: used inside a NestedLoop node and means that the child bellow it will only be scanned once. It saves data in memory as it's read and return data from memory on each subsequent pass.
- Hash Join: rows of one table are entered into an in-memory hash table, after which the other table is scanned and the hash table is probed for matches to each row. The input to the Hash node is the constructor of the hash table. That's then returned to the Hash Join node, which reads rows from tits outer child plan and searches the hash table for each one.
- Merge Join: Requires its input data to be sorted on the join keys.
- SubPlan: Arise from sub-selects in the original query. can sometimes be transformed into ordinary join plans. Values from the outer plan level can be passed down into a subplan and the results of the sub-select are available to the outher plan. Those result values are shown by `EXPLAIN` with notations like `(subplan_name).colN`, which refers to the `Nth` output column of the sub-select.
- ALL: operator that runs a subplan again for each row of the outer query.
- InitPlan: sub-select that doesn't reference any variables of the outer query and doesn't return more than one row. It's run only once per execution of the outer plan, and its results are saved for re-use in later rows of the outer plan.


- Table rows fetched in index order are expensive to read because rows are fetched separately. By sorting the row physical locations before reading the planner can minimize the cost of separate fetches
- When dealing with outer joins, you might see join plan nodes with both "Join Filter" and plain "Filter" conditions attached. "Join Filter" conditions come from the outer join's `ON` clause, so a row that fails the "Join Filter" condition could still get emitted as a null-extended row. But a plain Filter condition is applied after the outer-join rules and so acts to remove rows unconditionally. In an inner join there is no semantic difference between these types of filters.
- One way to look at variants plans is to force the planner to disregard whatever strategy it thought was the cheapest by using enable/disable `SET enable mergedjoin = off;` before the query execution;
- When the query is an `INSERT`, `UPDATE`, `DELETE`, or `MERGE` command, the actual work of applying the table changes is done by a top-level Insert, Update, Delete, or Merge plan node. The plan nodes underneath this node perform the work of locating the old rows and/or computing the new data. It's worth noting that although the data-modifying node can take a considerable amount of run time, the planner does not currently add anything to the cost estimates to account for that work. That's because the work to be done is the same for every correct query plan, so it doesn't affect planning decisions.
## EXPLAIN ANALYZE
With this option, `EXPLAIN` actually executes the query, and then displays the true row counts and true run time accumulated within each plan node, along with the same estimates that a plain `EXPLAIN` shows.

```SQL
EXPLAIN ANALYZE SELECT *
FROM tenk1 t1, tenk2 t2
WHERE t1.unique1 < 10 AND t1.unique2 = t2.unique2;

--                                   QUERY PLAN
-- ----------------​--------------------------------------------------------------
--  Nested Loop  (cost=4.65..118.50 rows=10 width=488) (actual time=0.017..0.051 rows=10 loops=1)
--    ->  Bitmap Heap Scan on tenk1 t1  (cost=4.36..39.38 rows=10 width=244) (actual time=0.009..0.017 rows=10 loops=1)
--          Recheck Cond: (unique1 < 10)
--          Heap Blocks: exact=10
--          ->  Bitmap Index Scan on tenk1_unique1  (cost=0.00..4.36 rows=10 width=0) (actual time=0.004..0.004 rows=10 loops=1)
--                Index Cond: (unique1 < 10)
--    ->  Index Scan using tenk2_unique2 on tenk2 t2  (cost=0.29..7.90 rows=1 width=244) (actual time=0.003..0.003 rows=1 loops=10)
--          Index Cond: (unique2 = t1.unique2)
--  Planning Time: 0.485 ms
--  Execution Time: 0.073 ms
```

"actual time" values are in milliseconds of real time.
The thing that's usually most important to look for is whether the estimated row counts are reasonably close to reality.

The `Planning time` shown by `EXPLAIN ANALYZE` is the time it took to generate the query plan from the parsed query and optimize it. It does not include parsing or rewriting.

The `Execution time` shown by `EXPLAIN ANALYZE` includes executor start-up and shut-down time, as well as the time to run any triggers that are fired, but it does not include parsing, rewriting, or planning time. Time spent executing `BEFORE` triggers, if any, is included in the time for the related Insert, Update, or Delete node; but time spent executing `AFTER` triggers is not counted there because `AFTER` triggers are fired after completion of the whole plan. The total time spent in each trigger (either `BEFORE` or `AFTER`) is also shown separately. Note that deferred constraint triggers will not be executed until end of transaction and are thus not considered at all by `EXPLAIN ANALYZE`.

The time shown for the top-level node does not include any time needed to convert the query's output data into displayable form or to send it to the client. While `EXPLAIN ANALYZE` will never send the data to the client, it can be told to convert the query's output data to displayable form and measure the time needed for that, by specifying the `SERIALIZE` option. That time will be shown separately, and it's also included in the total `Execution time`.

In some query plans, it is possible for a subplan node to be executed more than once. For example, the inner index scan will be executed once per outer row in the above nested-loop plan. In such cases, the `loops` value reports the total number of executions of the node, and the actual time and rows values shown are averages per-execution. This is done to make the numbers comparable with the way that the cost estimates are shown. Multiply by the `loops` value to get the total time actually spent in the node. In the above example, we spent a total of 0.030 milliseconds executing the index scans on `tenk2`.

In some cases `EXPLAIN ANALYZE` shows additional execution beyond the plan node execution and row counts.

```plaintext
...
Sort (...)
	...
	Sort Method: quicksort  Memory: 74kB
...
Hash (...)
	...
	Buckets: 1024  Batches: 1  Memory Usage: 35kB
...
Rows Removed by Filter: 99999
```

The Sort node shows the sort method used and the amount of memory or disk space needed. In particular, whether the sort was in-memory or on-disk.

The Hash node shows the number of hash buckets and batches as well as the peak amount of memory used for the hash table. If the number of batches exceeds one, there will also be disk space usage involved, but that is not shown.

The "Rows Removed" line only appears when at least one scanned row, or potential join pair in the case join node, is rejected by the filter condition.
## Rolling back data changes with analyze
If you want to analyze a data-modifying query without changing your table, you can roll the command back afterwards by wrapping the query in a transaction;

```plaintext
BEGIN;

EXPLAIN ANALYZE UPDATE tenk1 SET hundred = hundred + 1 WHERE unique1 < 100;

                                     QUERY PLAN
--------------------​-------------------------------------------------------------
 Update on tenk1  (cost=5.06..225.23 rows=0 width=0) (actual time=1.634..1.635 rows=0 loops=1)
   ->  Bitmap Heap Scan on tenk1  (cost=5.06..225.23 rows=100 width=10) (actual time=0.065..0.141 rows=100 loops=1)
         Recheck Cond: (unique1 < 100)
         Heap Blocks: exact=90
         ->  Bitmap Index Scan on tenk1_unique1  (cost=0.00..5.04 rows=100 width=0) (actual time=0.031..0.031 rows=100 loops=1)
               Index Cond: (unique1 < 100)
 Planning Time: 0.151 ms
 Execution Time: 1.856 ms

ROLLBACK;
```
## EXPLAIN BUFFERS
`EXPLAIN` has a `BUFFERS` option that can be used with `ANALYZE` to get even more runtime statistics:

The numbers provided by `BUFFERS` help to identify which parts of the query are the most I/O-intensive

```plaintext
EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM tenk1 WHERE unique1 < 100 AND unique2 > 9000;

                                     QUERY PLAN
---------------------------------------------------------------------------------
 Bitmap Heap Scan on tenk1  (cost=25.07..60.11 rows=10 width=244) (actual time=0.105..0.114 rows=10 loops=1)
   Recheck Cond: ((unique1 < 100) AND (unique2 > 9000))
   Heap Blocks: exact=10 --> BUFFERS INFO
   Buffers: shared hit=14 read=3 --> BUFFERS INFO
   ->  BitmapAnd  (cost=25.07..25.07 rows=10 width=0) (actual time=0.100..0.101 rows=0 loops=1)
         Buffers: shared hit=4 read=3 --> BUFFERS INFO
         ->  Bitmap Index Scan on tenk1_unique1  (cost=0.00..5.04 rows=100 width=0) (actual time=0.027..0.027 rows=100 loops=1)
               Index Cond: (unique1 < 100)
               Buffers: shared hit=2 --> BUFFERS INFO
         ->  Bitmap Index Scan on tenk1_unique2  (cost=0.00..19.78 rows=999 width=0) (actual time=0.070..0.070 rows=999 loops=1)
               Index Cond: (unique2 > 9000)
               Buffers: shared hit=2 read=3 --> BUFFERS INFO
 Planning:
   Buffers: shared hit=3 --> BUFFERS INFO
 Planning Time: 0.162 ms
 Execution Time: 0.143 ms
```