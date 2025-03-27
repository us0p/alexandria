# Date and Times
In most relational databases dates are stored in the format `YYYY-MM-DD`. That is because it's common to store dates as strings and with that format, when ordering, strings get ordered in chronological order which would't be the case for `MM-DD-YYYY` or `DD-MM-YYYY` formats.
## Crazy rules for dates and times
If you have your dates stored as `date` or `time` (depending on the availability of types of your database) you can do arithmetic between the dates.
If your date is stored as a `string` you should probably cast it to some `date` compatible type.

In PostgreSQL, hen you perform arithmetic on dates, the results are often stored as `INTERVAL` data type.

Also in PostgreSQL you can introduce intervals using `INTERVAL` function as well:
```SQL
SELECT p.birth + INTERVAL '1 week' week_after_birth FROM person p;
```

The interval is defined using plain-English terms like '10 seconds' or '5 months'. Also note that in PostgreSQL adding or subtracting a `date` column and an `interval` column results in another `date` column as in the above query.

Selecting the current type:
```SQL
-- PostgreSQL
SELECT NOW() d FROM person;

-- SQLite
SELECT date('now') d,
	   datetime('now') dt,
	   time('now') t
FROM person;

-- SQLite variation
SELECT date() d,
       datetime() dt,
       time() t
FROM person;
```