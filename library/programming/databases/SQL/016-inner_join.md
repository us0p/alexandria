# INNER JOIN
Is the default join applied for the reduced syntax `... JOIN ... ON ...`.

Inner joins eliminates rows from both tables that do not satisfy the join condition set forth in the `ON` statement. It represents the intersection between the two tables, where only rows that can be represented in the two tables are displayed.
![[Pasted image 20250323195228.png]]

Note that the results can only support one column with a given name—when you include 2 columns of the same name, the results will simply show the exact same result set for both columns **even if the two columns should contain different data**. You can avoid this by naming the columns individually.

```SQL
-- Consiter the following table:
/*
	Table School
	|address       |name            |
	|Anchieta      |Unip            |
	|Capão Redondo |Unip            |
	|Paulista      |São Judas       |
	|Vila Olímpia  |Anhembi Morumbi |

	Table Person
	|name   |school_name     |
	|Lucas  |Unip            |
	|Luan   |Anhembi Morumbi |
	|Mariana|FAM             |
*/

-- Namming columns individually to avoid collision.
SELECT p.*, s.*, p.name p_name, s.name s_name FROM person p JOIN school s ON p.school_name = s.name;

-- For the query above, te following rows are going to be returned
/*
	|p_name |school_name     |address       |s_name          |
	|Lucas  |Unip            |Anchieta      |Unip            |
	|Lucas  |Unip            |Capão Redondo |Unip            |
	|Luan   |Anhembi Morumbi |Vila Olímpia  |Anhembi Morumbi |
*/

-- Note that Lucas got two entries to match all universities with that had a matching name.

-- Note that Mariana didn't appear as there wasn't a school with that name in the school table.
```