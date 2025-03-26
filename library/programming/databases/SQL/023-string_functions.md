# SQL String Functions
Most of the functions are specific to certain data types. However, using a particular function will, in many cases, change the data to the appropriate type.

Note you should also check your database provider for the implementation of those functions.
The functions listed bellow are available on PostgreSQL but some aren't available for SQLite.
## LEFT
Pull certain number of characters from the left side of a string and present them as a separate string.
```SQL
-- File names are prefixed with a 10 digit string of the date the file was created.
SELECT file_name,
	   LEFT(file_name, 10) created_datetime
FROM files;
```
## RIGHT
Same thing as `LEFT` but from the right side
```SQL
-- Date time representation inclide hour information at the end.
-- Here we're striping the full datetime and then striping the hour from it.
SELECT file_name,
	LEFT(file_name, 10) created_datetime,
	RIGHT(LEFT(file_name, 10), 17) created_time
FROM files;
```
## LENGTH
Returns the length of a string.
```SQL
SELECT p.name,
       LENGTH(p.name)
FROM person;
```
## TRIM
Removes characters from the beginning and end of a string.
```SQL
SELECT p.bio
	   TRIM(leading ' ' FROM p.bio) remove_space_from_start,
	   TRIM(trailing ' ' FROM p.bio) remove_space_from_end,
	   TRIM(both ' ' FROM p.bio) remove_space_from_both_ends
FROM profile p;
```
## POSITION and STRPOS
Returns the numerical position where the provided substring first appears in the target.
Both functions are case sensitive.
```SQL
-- Using POSITION()
SELECT name,
	   POSITION('Lua' IN name) -- returns 1 for 'Luan';
FROM person;

-- Using STRPOS
SELECT name,
	   STRPOS(name, 'Lua')
FROM person;
```
## SUBSTR
Same as `LEFT` and `RIGHT` but start in the middle of the string instead of starting at the edges.
The syntax is
`SUBSTR(STR, starting_position, number_of_character_to_take)`
```SQL
SELECT name,
	   SUBSTR(name, 6, 5) sub_str -- Return 'Lopes' for 'Luan Lopes de Faria'
FROM person; 
```