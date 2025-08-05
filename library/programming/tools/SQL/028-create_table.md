```SQL
CREATE TABLE table_name (
	column_name1 datatype constraint,
	column_name2 datatype constraint,
	...
)
```

Constraints are an optional rule for data.
```SQL
CREATE TABLE courses (
	name VARCHAR(255) NOT NULL,
	description TEXT,
	duration DEC(4,2) NOT NULL,
	school_name VARCHAR DEFAULT 'E.E. VSF'
)
```

The `courses` table has three columns:
	- `name`: The data type is `VARCHAR` with a maximum of 255 characters. The `NOT NULL` constraint is used to ensure the this column will always have data.
	- `description`: The data type is `TEXT`, which can store very large text.
	- `duration`: The data type is `DEC` which stores decimals numbers. The number 4 represents the maximum number of digits the decimal can have. The number 2 represents the number of digits that must exist after the decimal point. Examples:
		- 12.34: valid, 4 digits in total, 2 after decimal
		- 1.23: valid, 3 digits, 2 after decimal
		- 99.99: valid: 4 digits, 2 after decimal, maximum value the column can store.
		- 123.45: invalid, 5 digits.
		- 100.0: invalid, 4 digits, has only 1 digit after decimal.
	- `scholl_name`: The data type is `VARCHAR` with a default value of `'E.E. VSF'`.

The database will issue an error if you attempt to create a table that already exists. To avoid the error, you can use the `IF NOT EXISTS` option:
```SQL
CREATE TABLE IF NOT EXISTS table_name (
	column_name1 datatype constraint,
	column_name2 datatype constraint,
	...
)
```

The default value to a column can be an expression, which will be evaluated whenever the default is inserted. A common example is for a `timestamp` column to have a default of `CURRENT_TIMESTAMP`.
## Table relationship
You cannot create a foreign key that references multiple different tables.
## One-to-Many
```SQL
CREATE TABLE customers (
	customer_id INT PRIMARY KEY,
	name VARCHAR(100)
);

CREATE TABLE orders (
	order_id INT PRIMARY KEY,
	order_date DATE,
	customer_id INT, -- can appear multiple times
	FOREIGN KEY (customer_id) REFERENCES customers(customer_id) -- FK
);
```
## One-to-One
```SQL
CREATE TABLE users (
	user_id INT PRIMARY KEY,
	username VARCHAR(50)
);

CREATE TABLE profiles (
	profile_id INT PRIMARY KEY,
	user_id INT UNIQUE -- can appear only once per user
	bio TEXT,
	FOREIGN KEY (user_id) REFERENCES users(user_id)	
);
```
## Many-to-Many
```SQL
-- Students table
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100)
);

-- Courses table
CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    title VARCHAR(100)
);

-- Junction table (many-to-many relationship)
CREATE TABLE Enrollments (
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
```