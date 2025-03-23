# Query Optimization
Process of refining SQL queries to improve their efficiency and performance.
## Using Indexes
Identify frequently used columns in WHERE, JOIN and ORDER BY clauses, and create indexes on those columns. 
Adding many indexes can slow down adding and updating data.
Only create indexes on columns that will provide significant search speed improvements.
## Use WHERE clause instead of HAVING
WHERE filters are recorded before groups are created and HAVING filters are recorded after the creation of groups. This means that using WHERE instead of HAVING will enhance the performance and minimize the time taken.
```sql
-- Display only the names whose age is greater than or equal to 18.
SELECT name FROM table_name WHERE age >= 18;

-- First renames the row and then display only those which pass the condition.
SELECT age COUNT(A) AS Students FROM table_name GROUP BY age HAVING COUNT(A) > 1;
```
## Avoid queries inside a loop
Performing queries inside a loop creates the N+1 problem. Many queries to the database are much slower than a single query big query as the overload of many database requests increase the time taken to retrieve all values.
## Avoid using SELECT *
Running queries with SELECT * will retrieve all the table information which are rarely useful. Specially in the case of JOIN clauses, where all the data of the joined rows are also going to be included.
Prefer to use strict SELECT statements and return only the columns needed for a specific purpose.
## Keep wild cards ate the end of LIKE operator
Pairing a leading wildcard with the ending wildcard will check for all records matching between the two wildcards.
```sql
-- will check all rows to serch for names including 'ram'
SELECT name, salary FROM employee WHERE name LIKE '%Ram%';

-- will returns only the rows that start with 'ram'
SELECT name, salary FROM employee WHERE name like 'Ram%';
```
## Use EXIST instead of COUNT
Both are used to search whether the table has a specific record or not. But in most cases EXIST is much more efficient than COUNT. EXIST will run till it finds the first matching entry whereas COUNT will keep on running and provide all the matching records.
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
## Consider Denormalization
Denormalization involves strategically adding redundant data to a database to improve query performance. It can reduce the need for JOIN operations but should be balanced with considerations for data integrity and maintenance overhead. JOIN operations, which combine data from multiple tables, can be slow. Denormalization aims to reduce the need for JOINS by copying some data from one table to another.
For example, Imagine tables for Customers and Orders. Normally, you’d link them with a foreign key in the Orders table. To speed up queries that retrieve customer information along with their orders, you could denormalize by adding some customer details directly into the Orders table.
## Optimize JOIN operations
Select the JOIN type that aligns with the data you want to retrieve.
## Avoid using too many joins
Using joins too much can make queries run slowly. Try different methods like subselects or temporary tables could help.
## Simplify joins
Reduce the number of tables involved in a join.
## Use appropriate datatypes
Opting for the most appropriate data type for each column helps to optimize data storage, speed up comparisons, and eliminate needless data conversions.
## Use LIMIT and OFFSET
These commands help by pulling a specific chunk of records at a time, which is especially useful for speeding up the loading of big datasets.
## Avoid SELECT DISTINCT
This is because the database has to sift through the data to remove any duplicates.
## Avoid subqueries
Whenever possible it's better to use joins or temporary tables instead.
## Prefer UNION ALL to UNION
Opt for UNION ALL if you don't need to get rid of duplicate entreis. It skips the step of sorting data to eliminate duplicates.
```sql
SELECT name FROM employee WHERE status = 'active'
UNION ALL
SELECT name FROM contractores WHERE status = 'active';
```
## Use stored procedures
A procedure wrap up complex tasks and improve performance by being pre-compiled and reusing execution plans efficiently.
## Avoid cursors
Cursors handle one row at a time, it can use a lot of resources because of their sequential processing approach.
Working with data in batches is generally more efficient than processing it row by row.
## Use temp table instead of subqueries
They work by dividing operations that involve many subqueries or intricate calculations into simpler, more manageable parts.
## Avoid negative searches
Queries that include conditions such as NOT IN, NOT EXISTS, or start with wildcards tend to run slower. This is because such conditions make it harder to use indexes effectively.
## Avoid using many OR conditions
Queries with many OR conditions can be slow because they require the database to evaluate multiple conditions. Consider restructuring your query to minimize the use of OR or using UNION to combine the results of simpler queries.

---
# Query optimization debugging strategies
## Add EXPLAIN to the beginning of queries
It explains how SQL queries are being executed. This description includes how tables are joined, their order, and many more. It is a beneficial query optimization tool that further helps in knowing the step-by-step details of execution.
Running EXPLAIN queries takes time so it should only be used during the query optimization process.

- query execution plans
- database profiling tools