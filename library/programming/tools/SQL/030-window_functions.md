# Window Functions
A window function performs a calculation across a set of table rows that are somehow related to the current row.

This is comparable to the type of calculation that can be done with an aggregate function. But unlike regular aggregate functions, use of a window function does not cause rows to become grouped into a single output row, the rows retain their separate identities.

Behind the scenes, the window function is able to access more than just the current row of the query result.
```SQL
SELECT duration_seconds,
	SUM(duration_seconds) OVER (OERDER BY start_time) AS running_total
FROM tutorial.dc_bikeshare_q1_2012;
```

The above query creates an aggregation without using `GROUP BY`.
## Basic windowing syntax
Adding `OVER` to an aggregation function like `SUM` designates it as a window function.

If you'd like to narrow the window from the entire dataset to individual groups within the dataset, you can use `PARTITION BY` to do so:
```SQL
SELECT start_terminal,
	   duration_seconds,
	   SUM(duration_seconds) OVER
		   (PARTITION BY start_terminal ORDER BY start_time)
		   AS running_total
FROM tutorial.dc_bikeshare_q1_2012
WHERE start_time < '2012-01-08';
```

The above query groups and orders the query by `start_terminal`. Within each value of `start_terminal`, it is ordered by `start_time`, and the running total sums across the current row and all previous rows of `duration_seconds`.

When `start_terminal` value changes you will notice that `running_total` starts over. That's what happens when you group using `PARTITION BY`.

In case you're still stumped by `ORDER BY`, it simply orders by the designated column(s) the same way the `ORDER BY` clause would, except that it treats every partition as separate. It also creates the running total, without `ORDER BY`, each value will simply be a sum of all the `duration_seconds` values in its respective `start_terminal`.

>You can't include window functions in a `GROUP BY` clause.