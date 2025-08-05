# FILTER
Used in aggregate function to include only rows that meet a specific condition.

Allows you to apply conditions to aggregation without needing to use [case expressions](013-case.md) making the query cleaner and often easier to read.

>You can use with **any** aggregate function.
## Syntax
```SQL
AGGREGATE_FUNCTION(column) FILTER (WHERE condition)
```
## Examples
```PostgreSQL
-- Count total users and active users
SELECT
	COUNT(*) total_users,
	COUNT(*) FILTER (WHERE active) active_users -- active is a boolean
FROM users;


-- Sum orders by status
SELECT
	SUM(amount) FILTER (WHERE status = 'shipped') shipped_total,
	SUM(amount) FILTER (WHERE status = 'pending') pending_total
FROM orders;

-- Grouped aggregations with FILTER
SELECT
	country,
	COUNT(*) total,
	COUNT(*) FILTER (WHERE gender = 'male') males,
	COUNT(*) FILTER (WHERE gender = 'female') females
FROM users
GROUP BY country;
```