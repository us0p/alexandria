# datetime objects
```python
date = datetime.datetime(
        2025, # year
        1,    # month
        1,    # day
        0,    # hour?
        0,    # minute?
        0,    # second?
        0,    # microsecond?
        None, # tzinfo?
        0     # fold?
)
```

The arguments must be integers in the following ranges:
- `MINYEAR` <= year <= `MAXYEAR`
- 1 <= month <= 12
- 1 <= day <= number of days in the given month
- 0 <= hour < 24.
- 0 <= minute < 60.
- 0 <= second < 60.
- 0 <= second < 1000000.
- fold in [0, 1]

`fold` is used to disambiguate wall times during a repeated interval.
The values `0` and `1` represent, respectively, the earlier and later of the two moments.

A repeated interval occurs when clocks are rolled back at the end of daylight saving or when the UTC offset for the current timezone is decreased for political reasons.

Supported operations include:
- Sum and subtraction between `datetime` and `timedelta` objects.
- Equality comparison `==` and `!=` between `datetime` objects.
- Order comparison `<`, `>`, `<=`, and `>=` between `datetime` objects.

Notes about the operations:
- You can't perform subtraction between **aware** and **naive** `datetime` objects.
- `datetime` objects are equal if they represent the same date and time, taking into account the time zone.
- If `tzinfo` are different between the objects, they are first converted to **UTC datetimes** before the operation.
- **naive** and **aware* `datetime` objects are never equal.
- Order comparison between **naive** and **aware** `datetime` objects raises `TypeError`.
- Equality comparison between **aware** and **naive** `datetime` objects don't raise `TypeError`.

## Class Methods
```python
import datetime
from datetime import timezone

dt = datetime.datetime
t = datetime.time

# current local date and time without 'tzinfo'
local_now = dt.today()

# current local date and time, accepts 'tzinfo'
# preferred over today() and utcnow()
same_as_above = dt.now()
utc_now = dt.now(timezone.utc)

# local date and time corresponding to the POSIX timestamp
# may return instances with 'fold' set to 1.
from_timestamp = dt.fromtimestamp(t.time())
from_timestamp_with_tz = dt.fromtimestamp(t.time(), timezone.utc)

# converts the proleptic Gregorian ordinal to datetime
# 'hour', 'minute', 'second' and 'microsecond' are all 0, 'tzinfo' if None
# 1 <= ordinal <= datetime.max.toordinal()
from_ordinal = dt.fromordinal(dt.toordinal(utc_now))

# Combines a date and time objects into a datetime object.
# If tzinfo is provided, it's used in the 'tzinfo' attribute of the final object.
# Otherwise it uses 'tzinfo' of the time object.
# If date parameter is a datetime object, its time components and 'tzinfo' attributes are ignored
combined = dt.combine(utc_now.date(), utc_now.time(), utc_now.tzinfo)

# Converts any valid ISO 8601 date_string to a datetime object
from_iso_str = dt.fromisoformat(utc_now.toisoformat())

# Return a datetime corresponsind to the ISO calendar specified by year, week and day.
iso_calendar = utc_now.isocalendar()
from_iso_calendar = dt.fromisocalendar(
    iso_calendar.year,
    iso_calendar.week,
    iso_calendar.weekday
)

# Parses a date string according to format.
# Always include a year in your format.
from_date_string = dt.strptime("05/10/1998", "%d/%m/%Y")
```
## Instance methods
```python
import datetime
from datetime import timezone

dt = datetime.datetime

utc_now = dt.now(timezone.utc)

# Return a date object
date = utc_now.date()

# Return a time object with fold but without tzinfo
time_without_tz = utc_now.time()

# Return a time object with fold and tzinfo
time_with_tz = utc_now.timetz()

# Creates a new datetime object withe the same attributes of the parent replacing the provided attributes.
# tzinfo=None can be specified to create a naive object from an aware with no conversion of date and time data
updated_dt = utc_now.replace(year=1998)

# Replace the tzinfo in the datetime object, adjusting date and time so the result is the same UTC time as self, but in tz's local time.
# If called without arguments or tz=None the system local time zone is used.
# If the provided tz is equal to the oridinal object, no adjustment is performed.
today = dt.today()
updated_tz_dt = today.astimezone(timezone.utc)

# Returns a the offset of the UTC time.
offset = updated_tz_dt.utcoffset()

# Returns the name of the tz
tz_name = utc_now.tzname() # 'UTC'

# Returns a named tuple with all the information of the datetime object
time_tuple = utc_now.timetuple()

# If naive object, works exaclty as timetuple()
# If aware, object is normalized to UTC and then returns time tuple
# It's recommended to always use aware datetimes
utc_time_tuple = utc_now.utctimetuple()

# Returns the proleptic Gregorian ordinal of the date
ordinal = utc_now.toordinal()

# Return POSIX timestamp corresponding to the datetime instance.
# Return a float similar to time.time()
timestamp = utc_now.timestamp() # 1743100573.916258

# Return the day of the week as an integer, Monday is 0 and Sunday is 6
week_day = utc_now.weekday()

# Return the day of the week as an integer, Monday is 1 and Sunday is 7
week_day_iso = utc_now.isoweekday()

# Return a named tuple with three components: year, week and weekday
iso_calendar = utc_now.isocalendar()

# Return a string representing the date and time in ISO 8601 format
# The separator of date and time is default to 'T'
# The timespec specifies the number of additional components of time to include, default to 'auto'

# possible values for timespec are:
# 'auto': same as 'seconds' if microsecond is 0, 'microseconds' otherwise
# 'hours': include the hour
# 'minutes: include hour and minutes 
# 'seconds': include hour, minute and seconds
# 'milliseconds': include full time, but truncate fractional second to milliseconds
# 'microseconds': include full time in HH:MM:SS.ffffff format.
iso_format = utc_now.isoformat()        # 1998-10-05T10:57:35
iso_format_sep = utc_now.isoformat(' ') # 1998-10-05 10:57:35

# Return a string representing the date and time
# It doesn't include tz info
ctime = utc_now.ctime() # Mon Oct  5 10:57:35 1998

# Return a string representing date and time as per format string.
str_date = utc_now.strftime("%d/%m/%Y %H:%M") # 05/10/1998 10:57
```
