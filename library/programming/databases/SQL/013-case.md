# CASE
Is SQL way of handling if/then logic.
It's followed by at least one pair of `WHEN` and `THEN` statements.
Every `CASE` statement must end with the `END` statement
The `ELSE` statement is optional, and provides a way to capture values not specified in `WHEN/THEN` statements.
The `CASE` statement always goes in the `SELECT` clause.
You can make any conditional statement using any conditional operator available in `WHERE` clauses between `WHEN` and `THEN`

```SQL 
SELECT 
	player_name,
    year,
CASE WHEN year = 'SR' THEN 'yes'
ELSE NULL END AS is_a_senior
FROM college_football_players;
```

In the above query:
1. The `CASE` statement checks each row to see if the conditional statement—`year = 'SR'` is true.
2. For any given row, if that conditional statement is true, the word "yes" gets printed in the column that we have named `is_a_senior`.
3. In any row for which the conditional statement is false, nothing happens in that row, leaving a null value in the `is_a_senior` column.
4. At the same time all this is happening, SQL is retrieving and displaying all the values in the `player_name` and `year` columns.

```SQL 
-- You can also add as many conditions you like
SELECT player_name,
	   weight,
	   CASE WHEN weight > 250 THEN 'over 250'
				 WHEN weight > 200 AND weight <= 250 THEN '201-250'
				 WHEN weight > 175 AND weight <= 200 THEN '176-200'
			     ELSE '175 or under' END AS weight_group
FROM college_football_players;
```
## Using CASE with aggregate functions
```SQL
-- Groups students in to groups 'FR' and 'Not FR' and count the number of integrants.
SELECT CASE WHEN year = 'FR' THEN 'FR'
       ELSE 'Not FR' END AS year_group
       COUNT(*)
FROM college_football_players
GROUP BY CASE WHEN year = 'FR' THEN 'FR' ELSE 'Not FR' END;


-- The GROUP BY clause could also use the alias of the CASE clause
SELECT CASE WHEN year = 'FR' THEN 'FR'
       ELSE 'Not FR' END AS year_group
       COUNT(*)
FROM college_football_players
GROUP BY year_group;
```
## Using CASE inside aggregate functions
If you want to display data horizontally you can use `CASE` clause inside an aggregate function. This is known as "pivoting".
```SQL 
SELECT CASE WHEN year = 'FR' THEN 'FR'
            WHEN year = 'SO' THEN 'SO'
            WHEN year = 'JR' THEN 'JR'
            WHEN year = 'SR' THEN 'SR'
            ELSE 'No Year Data' END AS year_group,
            COUNT(1) AS count
FROM benn.college_football_players
GROUP BY year_group

-- Display data as
/*
	|year_group|count|
	|FR        |w    |
	|SO        |x    |
	|JR        |y    |
	|SR        |z    |
*/

SELECT COUNT(CASE WHEN year = 'FR' THEN 1 ELSE NULL END) AS fr_count,
       COUNT(CASE WHEN year = 'SO' THEN 1 ELSE NULL END) AS so_count,
       COUNT(CASE WHEN year = 'JR' THEN 1 ELSE NULL END) AS jr_count,
       COUNT(CASE WHEN year = 'SR' THEN 1 ELSE NULL END) AS sr_count
FROM benn.college_football_players

-- Display data as
/*
	|fr_count|so_count|jr_count|sr_count|
	|w       |x       |y       |z       |
*/
```