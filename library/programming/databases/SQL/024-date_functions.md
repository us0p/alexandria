# Date Functions
Those functions are used as utilities for fields of with types related to `DATE` and `TIME`.

The functions bellows are available on PostgreSQL, you should check your database documentation for support of those functions.
## EXTRACT
Can be used to extract pieces of a date by intervals
```SQL
SELECT date_birth,
       EXTRACT('year'   FROM date_birth) year,
       EXTRACT('month'  FROM date_birth) month,
       EXTRACT('day'    FROM date_birth) day,
       EXTRACT('hour'   FROM date_birth) hour,
       EXTRACT('minute' FROM date_birth) minute,
       EXTRACT('second' FROM date_birth) second,
       EXTRACT('decade' FROM date_birth) decade,
       EXTRACT('dow'    FROM date_birth) day_of_week
FROM person;
```
## DATE TRUNC
Allows the rounding of dates to the nearest unit of measurement. It rounds a date to whatever precision you specify. The value displayed is the first value in that period. So when you `DATE_TRUNC` by year, any value in that year will be listed as January 1st of that year.

Note that the alias should be specific defined with `AS`.
```SQL
-- Consider date_birth as: 1998-10-05 17:31:59
SELECT date_birth,
       DATE_TRUNC('year'   , date_birth) AS year,   -- 1998-01-01 00:00:00
       DATE_TRUNC('month'  , date_birth) AS month,  -- 1998-10-01 00:00:00
	   DATE_TRUNC('week'   , date_birth) AS week,   -- 1998-10-05 00:00:00
       DATE_TRUNC('day'    , date_birth) AS day,    -- 1998-10-05 00:00:00
       DATE_TRUNC('hour'   , date_birth) AS hour,   -- 1998-10-05 17:00:00
       DATE_TRUNC('minute' , date_birth) AS minute, -- 1998-10-05 17:31:00
       DATE_TRUNC('second' , date_birth) AS second, -- 1998-10-05 17:31:59
       DATE_TRUNC('decade' , date_birth) AS decade  -- 1990-01-01 00:00:00
FROM person;
```
## Getting current date and time
You can instruct your query to pull the local date and time at the time the query is run:
```SQL
SELECT 
	CURRENT_DATE AS date, -- yyyy-mm-dd 00:00:00
    CURRENT_TIME as time, -- hh:mm:ss
    CURRENT_TIMESTAMP AS timestamp, -- yyyy-mm-dd hh:mm:ss
    LOCALTIME AS localtime, -- same as time but following the localtime (config)
    LOCALTIMESTAMP AS localtimestamp, -- same as timestamp but following the localtime (config)
    NOW() as now -- yyyy-mm-dd hh:mm:ss
```

>Remember that those functions are available in PostgreSQL, check you database provider for their availability.
## Different time zones
You can make a time appear in a different time zone using `AT TIME ZONE`
```SQL
SELECT
	CURRENT_TIME AS time,
	CURRENT_TIME AT TIME ZONE 'PST' AS time_pst
```


>Note that timestamps can be stored with or without timezone metadata.

- For a list of PostgreSQL time zones, [click here](https://www.postgresql.org/docs/7.2/timezones.html)
- More about `AT TIME ZONE` [here](https://www.postgresql.org/docs/9.2/functions-datetime.html#FUNCTIONS-DATETIME-ZONECONVERT)