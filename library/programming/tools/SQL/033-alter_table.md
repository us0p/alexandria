# `ALTER TABLE` statement
Used to change the structure of an existing table.
```SQL
ALTER TABLE table_name
action;
```

SQL allows you to perform the following actions:
- `ADD COLUMN column_name datatype constraint`
- `DROP COLUMN column_name`
- `ALTER COLUMN column_name SET datatype`
- `RENAME COLUMN column_name TO new_name `
- `ADD CONSTRAINT constraint_name constraint`
- `DROP CONSTRAINT constraint_name`
- Renaming the Table
- `ADD PRIMARY KEY (column_name)`
- `DROP PRIMARY KEY`
- `ADD CONSTRAINT constraing_name FOREIGN KEY (column1) REFERENCES table2(column2)`
- `RENAME TO new_name`
```SQL
CREATE TABLE test {
	id INTEGER PRIMARY KEY
};

ALTER TABLE test
ADD COLUMN username VARCHAR NOT NULL;
```