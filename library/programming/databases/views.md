Views

Views in SQL are a kind of virtual table. A view also has rows and columns like 
tables, but a view doesn’t store data on the disk like a table. View defines a 
customized query that retrieves data from one or more tables, and represents the 
data as if it was coming from a single source.
We can create a view by selecting fields from one or more tables present in the 
database. A View can either have all the rows of a table or specific rows based 
on certain conditions.
Views take very little space to store; the database contains only the definition 
of a view, not a copy of all the data that it presents.

There are two types of database views:. 
- Dynamic views: contain data from one or two tables and automatically include 
  all of the columns from the specified table or tables. Dynamic views are 
  automatically updated when related objects or extended objects are created or 
  changed. 
- Static views: contain data from multiple tables and the required columns from 
  these tables must be specified in the SELECT and WHERE clauses of the static 
  view. Static views must be manually updated when related objects or extended 
  objects are created or changed.

When to use SQL Views
- Restricting data access – Views provide an additional level of table security 
  by restricting access to a predetermined set of rows and columns of a table.
- Hiding data complexity – A view can hide the complexity that exists in multiple 
  joined tables.
- Simplify commands for the user – Views allow the user to select information 
  from multiple tables without requiring the users to actually know how to 
  perform a join.
- Store complex queries – Views can be used to store complex queries.
- Rename Columns – Views can also be used to rename the columns without affecting 
  the base tables provided the number of columns in view must match the number of 
  columns specified in a select statement. Thus, renaming helps to hide the names 
  of the columns of the base tables.
- Multiple view facility – Different views can be created on the same table for 
  different users.
