Stored Procedures
A stored procedure in SQL is a group of SQL queries that can be saved and 
reused multiple times. It is very useful as it reduces the need for 
rewriting SQL queries. It enhances efficiency, reusability, and security 
in database management.
Users can also pass parameters to stored procedures so that the stored 
procedure can act on the passed parameter values.
Stored Procedures are created to perform one or more DML operations on the 
Database. It is nothing but a group of SQL statements that accepts some 
input in the form of parameters, performs some task, and may or may not 
return a value.

Important Points About SQL Stored Procedures
- Stored procedures allow for code that is used repeatedly to be saved on 
  the database and run from there, rather than from the client. This 
  provides a more modular approach to database design.
- Since stored procedures are compiled and stored in the database, they 
  are highly efficient. SQL Server compiles each stored procedure once and 
  then reutilizes the execution plan. This leads to tremendous performance 
  boosts when stored procedures are called repeatedly.
- Stored procedures provide better security to your data. Users can execute 
  a stored procedure without needing to execute any of the statements 
  directly. Therefore, a user can be granted permission to execute a stored 
  procedure without having any permissions on the underlying tables.
- Stored procedures have better support for error handling.
- Stored procedures can be used to provide advanced database functionality, 
  such as modifying data in tables, and encapsulating these changes within 
  database transactions.
