# Temp table
Is a special kind of table that exista temporarily during a session or transaction.

Exists only for the duration of the current database session and it's automatically dropped when the session ends.

```SQL
-- Create a temporary table
CREATE TEMP TABLE temp_users AS (
	id SERIAL,
	name TEXT
) [ON COMMIT [DROP] | [[PRESERVE, DELETE] ROWS];
```

- `ON COMMIT PRESERVE ROWS`: Keeps rows across transactions.
- `ON COMMIT DELETE ROWS`: Deletes rows after commit.
- `ON COMMIT DROP`: Drops table after commit.