Date/Time function that returns the Julian day number - a continuous count of days since **noon Universal Time (UT)** on **January 1,4713 B.C** on the Julian calendar.

Commonly used for date arithmetic and date comparisons.
## What is Julian day
- It's a floating-point number.
- The integer part represents the day.
- The fractional part represents the time of day

```sqlite
julianday('YYYY-MM-DD HH:MM:SS')
julianday('now')
julianday('YYYY-MM-DD')
julianday(datetime_column)


-- example
select julianday('2025-07-16') -- 2460495.5
select julianday('2025-07-16') - julianday('2025-07-01') -- 15.0
```