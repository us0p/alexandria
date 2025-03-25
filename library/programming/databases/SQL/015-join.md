# JOIN
A statement used to relate two or more tables based on a common or common fields.
```SQL
-- Dispaying the name of a person and the name of its school by joining information from two different tables.
SELECT p.name, s.name FROM person p JOIN school s ON s.name = p.school_name;
```

In plain English, this means:
	Join all rows from the `person` table on to rows in the `school` table for which the `school_name` field in the `person` table is equal to the `name` field in the `school` table.
## ON
It's used after the `JOIN` and indicates how the table of `FROM` and the table of `JOIN` relate to each other.
The two columns that map to one another, are referred to as "foreign keys". And their mapping ir written as a conditional statement:
```SQL 
ON p.school_name = s.name

-- You can use any conditional into the ON clause
ON p.school_name = s.name AND s.founded_at > 2000
```
## Joined Result
If there's a match, SQL takes all columns from the `school` table and joins them to all the columns in the `person` table. The result is a table combining all the columns of the `person` table and the `school` table.

If you want to return all the results from one side and only some from the other:
```SQL
SELECT p.*, t.address FROM person p JOIN school s ON p.school_name = s.name;
```

Note that if there's more than one distinct school for a given `p.school_name`, the `person` row that matches those different `schools` is going to get duplicated, so that each school can be successfully displayed in a relationship.

Also note that, if a person school name doesn't exist in the school table, the result depends on the type of join being made. As per the example above, the default join applied is the [INNER JOIN](016-inner_join.md).
## Joins on Multiple Keys
There are two reasons why you might want to join tables on multiple keys:
1. Accuracy
2. Performance
Joining on multiple keys can increase the performance of your query if you are joining on multiple indexed columns.