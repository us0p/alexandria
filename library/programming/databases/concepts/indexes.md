## Indexes
Method of creating sorted column keys to improve search.

It Creates sorted column keys to improve search.
 - Similar to book index.
 - Reference to data location.

>Indexes require setup and maintenance from DBA.

Any column, or combinated columns can be an Index or a Partition.

>Database administrator should document this in a database diagram.
### Why
- Faster Queries: Searching ordered keys instead of the raw data is faster.
### Where
- Common filter columns such as date or location used in WHERE, JOIN, ORDER BY conditions, etc.
- Primary Key
![[Pasted image 20250714091849.png]]

You can see four values for fried rice sorted together in the index.

When you query the cookbook table, the query looks at this ordered index table. The query quickly finds all the fried rice entries because they are together. The query uses the corresponding pointer values to find the fried rice rows in the original cookbook table.

Searching a sorted, grouped index is faster than searching each row of the cookbook table.

Anyone can find existing indexes with a query. `pg_tables` schema is similar to `information_schema` and is specific to PostgreSQL. This schema contains views with metadata about the database.

`pg_indexes` is a view that contains all the indexes. It list the schema, table, index name, storage location, and the index creation SQL statement.

Use an index:
- Large tables
- Common filter conditions
- Often used on Primary Keys
Avoid an index
- Small tables
- Columns with many nulls
- Frequently updated tables
	- Index will become fragmented
	- Writes data in two places
![[Pasted image 20250714092801.png]]

Notice how `basil` is not grouped with other recipes of `spaghetti & meatballs`. This is index fragmentation.

This can be fixed by re-indexing the table, but it is an additional processing step.