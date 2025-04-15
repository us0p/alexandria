Provide time related functions.

An explanation of some terminology and conventions in order:
- The epoch is the point where the time starts. It is January 1, 1970, 00:00:00 (UTC) on all platforms.
- The term seconds since the epoch refers to the total number of elapsed seconds since the epoch, typically excluding leap seconds. Leap seconds are excluded from this total on all POSIX-compliant platforms.
- The functions in this module may not handle dates and times before the epoch or far in the future. The cut-off point in the future is determined by the C library; for 32-bit systems, it is typically in 2038.
- DST is Daylight Saving Time, an adjustment of the timezone by (usually) one hour during part of the year. DST rules are magic (determined by local law) and can change from year to year. The C library has a table containing the local rules (often it is read from a system file for flexibility) and is the only source of True Wisdom in this respect.
- The precision of the various real-time functions may be less than suggested by the units in which their value or argument is expressed. E.g. on most Unix systems, the clock “ticks” only 50 or 100 times a second.
- On the other hand, the precision of `time()` and `sleep()` is better than their Unix equivalents: times are expressed as floating-point numbers.
- `time()`: Returns the most accurate time available (using Unix `gettimeofday()` where available).
- `sleep()` will accept a time with a nonzero fraction (Unix `select()` is used to implement this, where available).

Use the following functions to convert between time representations:
 
| From                        | To                          | Use                 |
| --------------------------- | --------------------------- | ------------------- |
| seconds since the epoch     | `struct_time` in UTC        | `gmtime()`          |
| seconds since the epoch     | `struct_time` in local time | `localtime()`       |
| `struct_time` in UTC        | seconds since the epoch     | `calendar.timegm()` |
| `struct_time` in local time | seconds since the epoch     | `mktime()`          |
## `time.struct_time`
It's an object with a named tuple interface. The following values are present:
```python
from time import gmtime

struct_time = gmtime(0)

assert(struct_time[0] == struct_time.tm_year) # 1997
assert(struct_time[1] == struct_time.tm_mon) # range [1, 12]
assert(struct_time[2] == struct_time.tm_mday) # range [1, 31]
assert(struct_time[3] == struct_time.tm_hour) # range [0, 23]
assert(struct_time[4] == struct_time.tm_min) # range [0, 59]
assert(struct_time[5] == struct_time.tm_sec) # range [0, 61]
assert(struct_time[6] == struct_time.tm_wday) # range [0, 6]; Monday is 0
assert(struct_time[7] == struct_time.tm_yday) # range [1, 366]
assert(struct_time[8] == struct_time.tm_isdst) # 0 -> off, 1 -> on, -1 -> unknwon
assert(struct_time.tm_zone == "GMT") # abbreviation of timezone name
assert(struct_time.tm_gmtoff == 0) # offset east of UTC in seconds
```
## `time.strftime`
Convert a tuple or `time.struct_time` to a string as specific by the format argument.

Some `date` and `datetime` functions use the format representation of `time.strftime` to indicate how the time should be formatted. 

You can find the table with all format options [here](https://docs.python.org/3/library/time.html#time.strftime)

```python
from time import strftime

print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime(0)))
# 'Thu, 01 Jan 1970 00:00:00 +0000'
```