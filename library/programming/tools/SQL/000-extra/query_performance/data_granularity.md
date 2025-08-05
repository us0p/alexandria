## Why and When to aggregate data
Each row of a table is unique based on the granularity or the level of detail.

The level of detail can come from one or more columns.

![[Pasted image 20250709161847.png]]

In the following table, `game` is the lowest level of granularity. It's a column that describes an unique record. Since each game also has a unique `id`, the `id` column also describes an unique record.

![[Pasted image 20250709162025.png]]

Considering the two tables, there are multiples rows per game, so `game` is no longer the table grain.

Instead, `game` and `platform` together describes each unique row. So now two columns are needed to describe the granularity, `game_id` and `platform`.
## Joining different granularities
To avoid duplicates and improve query performance, you need to aggregate tables to the same level of detail before joining them.

Queries requires aggregate functions and GROUP BY clauses to have the same level of granularity.

CTE are useful to aggregate data before performing joins.

Suppose you want to know the number of platforms for each game, and the last platform the game was available.

![[Pasted image 20250709162451.png]]

In the case of Legend of Zelda, we can see that it maps to multiples platforms in the platforms table.

![[Pasted image 20250709162635.png]]

Instead of selecting a single game most recent platform you've added records for each platform for that game.

The Legend of Zelda went from 1 record in the game's table to the 3 record shown here.

The output table is now of the `Game_Platforms` grain.
### Setting up a granularity change
To return the results in the `Video_Games` table grain, you can turn the query into two steps.
1. Sets the stage for easy identification of the most recent year platform by aggregating the data from `Game_Platforms` to represent what we want: **The number of platforms for each game and the last platform the game was available**.
```SQL
SELECT
	game_id,
	platform,
	year,
	COUNT(platform) AS no_platforms,
	MAX(year) AS last_platform_yr
FROM game_platforms
GROUP BY game_id, platform, year;
```

![[Pasted image 20250709163045.png]]
2. Query the `Video_Games` table to get only the data we want and joins it with the aggregated result we have.
```PostgreSQL
WITH platform_cte AS (
	SELECT
		game_id,
		platform,
		year,
		COUNT(platform) AS no_platforms,
		MAX(year) AS last_platform_yr
	FROM game_platforms
	GROUP BY
		game_id,
		platform,
		year
)
SELECT
	g.id,
	g.game,
	cte.no_platforms,
	cte.platform AS last_platform
FROM video_games g
JOIN platforms_cte cte
	ON g.id = cte.game_id
	AND cte.last_platform_yr = cte.year;
```

The query above will return only a single row, following the granularity that we expected, avoiding duplicated data and duplicated calculations, reducing the result size to the minimum required number of records.

![[Pasted image 20250709163738.png]]