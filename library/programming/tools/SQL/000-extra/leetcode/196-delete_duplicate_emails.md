## Goal
Delete all duplicate emails, keeping only one unique email with the smallest `id`.
## Solution 1 (Mine)
```PostgreSQL
WITH p AS (
    SELECT
        DISTINCT ON(email)
        id,
        email
    FROM
        Person
    ORDER BY
        email, id
)
DELETE FROM 
    Person
WHERE id NOT IN (
    SELECT
        id
    FROM
        p
);
```
Creates a CTE that returns a list of registers with distinct emails with the lowest id.
Them deletes all elements from `Person` that aren't present in the result set of the CTE.
## Solution 2
```PostgreSQL
DELETE FROM
    Person
WHERE id NOT IN (
    SELECT
        MIN(id)
    FROM
        Person
    GROUP BY
        email
);
```
Deletes registers from Person where the id is not present in the sub-query.

The sub-query groups registers by the email and return the minimum id for each group.
## Solution 3
```PostgreSQL
DELETE FROM Person p2
USING Person p1
WHERE p1.email = p2.email
AND p1.id < p2.id;
```
Performs a "lateral join" in the Person table with the `USING` statement.
Deletes only registers from Person where have the same id but higher id values.

**In solution 1 and 2:**
The solutions uses `NOT IN` as you can't use aliases in `DELETE` without a `USING` or a subquery with a  `FROM` clause so you can use `NOT EXISTS`.

Another way of writing the condition with `NOT EXISTS` instead would be:
```PostgreSQL
-- ...
DELETE FROM Person
WHERE NOT EXISTS (
	SELECT 1
	FROM p
	WHERE Person.id = p.id  -- use a direct reference.
)
```