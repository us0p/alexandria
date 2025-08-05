# FILTER vs CASE WHEN
Both [FILTER](049-filter.md) and [CASE WHEN](013-case.md) achieve the same result, but in different ways:
```PostgreSQL
-- Using FILTER
SELECT
	COUNT(*) total_users,
	COUNT(*) FILTER (WHERE active) active_users,
	COUNT(*) FILTER (WHERE NOT active) inactive_users
FROM users;

-- Using CASE
SELECT
	COUNT(*) total_users,
	COUNT(CASE WHEN active THEN 1 END) active_users,
	COUNT(CASE WHEN NOT active THEN 1 END) inactive_users
FROM users;
```
## When to prefer `FILTER`:
- Only want to include/exclude rows in aggregation.
- Using multiple conditional aggregates.
## When to prefer `CASE WHEN`:
- When the aggregation depends on computed values.
- When you want to return different values (not only filter them out).

>Performance is the same as both lead to similar execution plans.