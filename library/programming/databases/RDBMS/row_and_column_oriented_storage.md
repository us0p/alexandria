## Row-oriented and Column-oriented storage 
Database stores data into two main formats:

**Row oriented storage**: Relation between columns is retained. Which means that one record is composed of all the columns for that one row.
![[Pasted image 20250714083656.png]]

**Column oriented storage**: Relation between rows is retained. Which means that one record is all the rows for one column.
![[Pasted image 20250714083808.png]]

Notice how all zoo animal names are stored together and how species are stored together across many rows.

However, the relationship between the name and species is lost in column storage.

>PostgreSQL inherently uses row oriented storage.
## Row Oriented Storage
Because all columns for one row are stored together, it's fast to append or delete whole rows. Additionally, a query to return one column, is as fast as a query to return all columns.

The number of rows returned impacts query speed, so returning all rows is slow.
## Using Column Oriented Storage
This type of storage is ideal for analytics.
- One column stored in same location.
- Quick to return all rows.
- Fast to perform column calculations.

Because one column is stored in the same location, queries to return all rows are quick.

Calculations using all rows from a single column are also quick.

Column oriented storage is not well suited for transactional database need. This storage retains the relationship between rows for a single column.
- Slow to return all columns
- Slow to load data.

Because a whole row is not stored in the same location, queries to return all columns are slow.

Loading data is also slow since data is usually loaded on a row basis.

Transactional databases focuses on inserting and deleting records quickly.

Common examples of column oriented storage databases:

| Database Server | Solution                               |
| --------------- | -------------------------------------- |
| PostgreSQL      | Citus Data, Greenplum, Amazon Redshift |
| MySQL           | MariaDB                                |
| Oracle          | Oracle In-Memory Cloud Store           |
| Multiple RDMS   | Clickhouse, Apache Druid, CrateDB      |
As always, with large data, limiting the number of columns returned will improve performance.

You can limit columns by using `SELECT *` sparingly.

Instead, use the `information_schema` to explore data.

Work through calculations for the columns of interest in individual queries.

```PostgreSQL
-- Structured for column oriented
-- Operates only in a small number of columns
SELECT
	MIN(age),
	MAX(age)
FROM zoo_animals
WHERE species = 'zebra';

-- Structured for row-oriented
-- Same query but return all columns.
SELECT *
FROM zoo_animals
WHERE species = 'zebra'
ORDER BY age;
```
