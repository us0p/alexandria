Normalization
Database normalization is a process used to organize a database into 
tables and columns. The idea is that a table should be about a specific 
topic and that only those columns which support that topic are included. 
This limits the number of duplicate data contained within your database. 
This makes the database more flexible by eliminating issues stemming from 
database modifications.

Normal Forms:
1. Each cell must contain only a single value.
   All the data in a given column has the same type.
   Each row must be uniquely identified.
2. All attributes (Non-Key Columns) depend on the primary-key. If a given 
   column
   depend on other column rather than the key, they should be extracted to 
   another table.
3. Has no transitive functional dependencies.
4. No multi-valued dependencies. You can't have a duplicated row for the
   same entity, you should extract the multi-values column to another 
   table.

Transitive Functional Dependencies
Is when changing a non-key column, might cause any of the other non-key
columns to change.

Denormalization
Denormalization is the opposite of normalization. It is the process of adding 
redundant data to a database to improve read performance. This is done by adding 
duplicate data into multiple tables to avoid expensive joins. This is done at the 
expense of increased storage and decreased write performance.
