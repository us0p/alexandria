# Window Functions
A window function performs a calculation across a set of table rows that are somehow related to the current row.

Returns one row per input row.

This is comparable to the type of calculation that can be done with an aggregate function. But unlike regular aggregate functions, use of a window function does not cause rows to become grouped into a single output row, the rows retain their separate identities.

Behind the scenes, the window function is able to access more than just the current row of the query result.
```SQL
-- Example shows how to compare each employee's salary with the avg salary in the department
SELECT
	depname,
	empno,
	salary,
	AVG(salary) OVER(PARTITION BY depname)
FROM
	empsalary;

-- Output result
--   depname  | empno | salary |          avg
-- -----------+-------+--------+-----------------------
--  develop   |    11 |   5200 | 5020.0000000000000000
--  develop   |     7 |   4200 | 5020.0000000000000000
--  develop   |     9 |   4500 | 5020.0000000000000000
--  develop   |     8 |   6000 | 5020.0000000000000000
--  develop   |    10 |   5200 | 5020.0000000000000000
--  personnel |     5 |   3500 | 3700.0000000000000000
--  personnel |     2 |   3900 | 3700.0000000000000000
--  sales     |     3 |   4800 | 4866.6666666666666667
--  sales     |     1 |   5000 | 4866.6666666666666667
--  sales     |     4 |   4800 | 4866.6666666666666667

-- The query below creates an aggregation without using `GROUP BY`.
SELECT 
	duration_seconds,
	SUM(duration_seconds) OVER (OERDER BY start_time) AS running_total
FROM 
	tutorial.dc_bikeshare_q1_2012;
```

The rows considered by a window function are those of the "virtual table" produced by the query's `FROM` clause as filtered by its `WHERE`, `GOUP BY`, and `HAVING` clauses if any.

A query can contain multiple window functions that slice up the data in different ways using different `OVER` clauses, but they all act on the same collection of rows defined by this virtual table.
## Window Frame
We already saw that `ORDER BY` can be omitted if the ordering of rows is not important. It is also possible to omit `PARTITION BY`, in which case there is a single partition containing all rows.

For each row, there is a set of rows within its partition called its **window frame**.
Some window functions act only on the rows of the window frame, rather than of the whole partition. By default, if `ORDER BY` is supplied then the frame consists of all rows form the start of the partition up through the current row, plus any following rows that are equal to the current row according to the `ORDER BY` clause. When `ORDER BY` is omitted the default frame consists of all rows in the partition.
```SQL
-- Applies the function to the whole window
SELECT
	salary,
	SUM(salary) OVER()
FROM
	empsalary;

--  salary |  sum
-- --------+-------
--    5200 | 47100
--    5000 | 47100
--    3500 | 47100
--    4800 | 47100
--    3900 | 47100
--    4200 | 47100
--    4500 | 47100
--    4800 | 47100
--    6000 | 47100
--    5200 | 47100

-- Applies the function to the current and previous items
SELECT
	salary,
	SUM(salary) OVER(ORDER BY salary)
FROM
	empsalary;

--  salary |  sum
-- --------+-------
--    3500 |  3500
--    3900 |  7400
--    4200 | 11600
--    4500 | 16100
--    4800 | 25700
--    4800 | 25700
--    5000 | 30700
--    5200 | 41100
--    5200 | 41100
--    6000 | 47100
```

Window functions are permitted only in the `SELECT` list and the `ORDER BY` clause of the query. They are forbidden elsewhere, such as `GROUP BY`, `HAVING` and `WHERE` clauses. This is because they logically execute after the processing of those clauses. Also, window functions execute after non-window aggregate functions. This means it is valid to include an aggregate function call in the arguments of a window function, but not the opposite.

When a query involves multiple window functions, it is possible to write out each one with a separate `OVER` clause, but this is duplicative and error-prone if the same windowing behavior is wanted for several functions. Instead, each windowing behavior can be named in a `WINDOW` clause and then referenced in `OVER`. For example:

```SQL
SELECT sum(salary) OVER w, avg(salary) OVER w
  FROM empsalary
  WINDOW w AS (PARTITION BY depname ORDER BY salary DESC);
```
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

>You can't include window functions in a `GROUP BY` clause.
## Window function structure
```SQL
SELECT 
	Gender,
	Name,
	Total, 
	ROW_NUMBER() OVER(ORDER BY Total DESC) AS Popularity
FROM 
	baby_names;
```
- `ROW_NUMBER`: Is the **function**
- `OVER(ORDER BY Total DESC)`: Is the **window**
The **window** determines how you want to be viewing your data when you apply your **function**.

In the query above, when the `ROW_NUMBER()` is applied, the data of the table should be ordered by total in descending order.

The goal of a window function is to make some calculation for each row of your data.

The window is essentially the view of the table you want when you are applying your function.

Inside your window you can also split your data into groups and your functions are going to start over whenever a new group starts.
```SQL
SELECT
	Gender,
	Name,
	Total,
	ROW_NUMBER() OVER(PARTITION BY Gender ORDER BY Total DESC) AS Popularity
FROM
	baby_names;
```

The query above is going to separate the data in the window into different group of Genders and order those groups by the Total amount.
The `ROW_NUMBER()` is going to start from the beginning whenever the group change.

For each row, the window function is computed across the rows that fall into the same partition as the current row.
## Window x Aggregate Functions
- Aggregate functions: Group rows together based on `GROUP BY`.
	- Returns one row per group.
	- Usually faster for grouped summaries.
	- Less flexible, can only be applied to groups.
- Window functions: Perform calculations across a set of rows related to the current row.
	- Returns one row per input row (no row reduction).
	- Involves sorting a window frame calculation.
	- Can be slower than aggregates, especially with large windows and complex partitioning.
	- More flexible, access to full row + group total.
### When to chose which
- Use aggregate functions when you want collapsed/grouped results.
- Use window functions when you want row-level detail + group stats.
## Builtin Window Functions
In addition to these functions, any built-in or user-defined ordinary aggregate (i.e., not ordered-set or hypothetical-set aggregates) can be used as a window function;

| Function Name                         | Behavior                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ROW_NUMBER()`                        | Returns the number of the current row within its partition, counting from 1.                                                                                                                                                                                                                                                                                         |
| `RANK()`                              | Returns the rank of the current row, with gaps(the row number of the first row is per group (partition)).                                                                                                                                                                                                                                                            |
| `DENSE_RANK()`                        | Returns the rank of the current row, without gaps.                                                                                                                                                                                                                                                                                                                   |
| `PERCENT_RANK()`                      | Returns the relative rank of the current row, that is $\frac{(rank - 1)}{(totalPartitionRows - 1)}$. The value ranges from 0 to 1 inclusive.                                                                                                                                                                                                                         |
| `CUME_DIST()`                         | Returns the cumulative distribution, that is $\frac{NPRPoPWR}{TPR}$. Where `NPRPoPWR`: number of partition rows preceding or peers with current row, and `TPR`: total partition rows. The value thus ranges from $\frac{1}{N}$ to 1.                                                                                                                                 |
| `NTILE(num_buckets)`                  | Returns an integer ranging from 1 to the argument value, dividing the partition as equally as possible.                                                                                                                                                                                                                                                              |
| `LAG(value [, offset [, default]])`   | Returns _`value`_ evaluated at the row that is _`offset`_ rows before the current row within the partition; if there is no such row, instead returns _`default`_ (which must be of a type compatible with _`value`_). Both _`offset`_ and _`default`_ are evaluated with respect to the current row. If omitted, _`offset`_ defaults to 1 and _`default`_ to `NULL`. |
| `LEAD(value, [, offset [, default]])` | Returns _`value`_ evaluated at the row that is _`offset`_ rows after the current row within the partition; if there is no such row, instead returns _`default`_ (which must be of a type compatible with _`value`_). Both _`offset`_ and _`default`_ are evaluated with respect to the current row. If omitted, _`offset`_ defaults to 1 and _`default`_ to `NULL`.  |
| `FIRST_VALUE(value)`                  | Returns _`value`_ evaluated at the row that is the first row of the window frame.                                                                                                                                                                                                                                                                                    |
| `LAST_VALUE(value)`                   | Returns _`value`_ evaluated at the row that is the last row of the window frame.                                                                                                                                                                                                                                                                                     |
| `NTH_VALUE(value, n)`                 | Returns _`value`_ evaluated at the row that is the _`n`_'th row of the window frame (counting from 1); returns `NULL` if there is no such row.                                                                                                                                                                                                                       |
