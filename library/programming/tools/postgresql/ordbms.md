# Object-Relational Database Management System - ORDBMS
It's a type of database system that combines:
- The traditional features of a Relational Database (tables, rows, columns, SQL).
- Some features from Object-Oriented Programming (types, classes, inheritance, methods).

It can store and manage complex data types not just simple rows and columns.
## Why does it exist
Traditional RDBMS could only handle simple types like integer, text, date, etc.

Modern applications need to store more complex structures:
- JSON
- Arrays
- Geographic coordinates (GIS)
- Multimedia (images, audio)
- User-Defined types (e.g. a "Product" with multiple parts)

Rather than squashing everything into flat tables, ORDBMS allows you to work naturally with richer data types.
```SQL
CREATE TYPE address AS (
	street TEXT,
	city TEXT,
	zip_code TEXT
);

CREATE TABLE customers (
	id SERIAL PRIMARY KEY,
	name TEXT,
	home_address address -- can store structured "address" objects inside your rows
);
```
## Key Features of an ORDBMS
- Inheritance
- Stored Procedures/Functions
- Methods on Types