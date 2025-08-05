## Keep wild cards ate the end of LIKE operator
Pairing a leading wildcard with the ending wildcard will check for all records matching between the two wildcards.
```sql
-- will check all rows to serch for names including 'ram'
SELECT name, salary FROM employee WHERE name LIKE '%Ram%';

-- will returns only the rows that start with 'ram'
SELECT name, salary FROM employee WHERE name like 'Ram%';
```
## Use EXIST instead of IN
When checking if a value is part of a smaller group, using EXISTS is usually faster than IN. This is because EXISTS lets the database stop looking the moment it finds a matching record, while IN require going through the whole dataset.
## Avoid Cartesian products
Cartesian product occur when every row from one table is joined with every row from another table, resulting in a massive dataset. Make sure you're joining the tables based on the specific relationship you want to explore.
```sql
-- Joins every author with every book.
SELECT * FROM author JOIN book;

-- Join authors with their corresponding book based on author ID.
SELECT author.name, book.title FROM author JOIN book on author.id = book.author_id;
```
## Use appropriate datatypes
Opting for the most appropriate data type for each column helps to optimize data storage, speed up comparisons, and eliminate needless data conversions.

**Numeric vs Text**:
- Numbers have shorter lengths
- Number occupy less storage
- Speeds performance
## Use temp table or CTEs instead of subqueries
They work by dividing operations that involve many subqueries or intricate calculations into simpler, more manageable parts.
## Avoid using many OR conditions
Queries with many OR conditions can be slow because they require the database to evaluate multiple conditions. Consider restructuring your query to minimize the use of OR or using UNION to combine the results of simpler queries.