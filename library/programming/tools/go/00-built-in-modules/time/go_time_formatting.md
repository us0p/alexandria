In Go, time formatting uses a reference time:
```go
"Mon Jan 2 15:04:05 MST 2006"
```

When you want to format or parse dates, you take that layout and rearrange it into the shape you need.

For example formatting a date into `RFC3339` standard:
```go
"2006-01-02T15:04:05Z07:00"
```

Here's the summary of the components of a layout string. Each element shows by example the formatting of an element of the reference time.

**Only these values are recognized**.

| year | month   | day of week | day of month | day of year | hour | minute | second | am/pm |
| ---- | ------- | ----------- | ------------ | ----------- | ---- | ------ | ------ | ----- |
| 2006 | Jan     | Mon         | 2            | __2         | 15   | 4      | 5      | PM    |
| 06   | January | Monday      | _2           | 002         | 3    | 04     | 05     |       |
|      | 01      |             | 02           |             | 03   |        |        |       |
|      | 1       |             |              |             |      |        |        |       |
Numeric time zone offsets format as follows:
```go
"-0700"     ±hhmm
"-07:00"    ±hh:mm
"-07"       ±hh
"-070000"   ±hhmmss
"-07:00:00" ±hh:mm:ss
```

Replacing the sign in the format with a Z triggers the ISO 8601 behavior of printing Z instead of an offset for the UTC zone. Thus:

```go
"Z0700"      Z or ±hhmm
"Z07:00"     Z or ±hh:mm
"Z07"        Z or ±hh
"Z070000"    Z or ±hhmmss
"Z07:00:00"  Z or ±hh:mm:ss
```

Within the format string, the underscores in "_2" and "__2" represent spaces that may be replaced by digits if the following number has multiple digits, for compatibility with fixed-width Unix time formats. A leading zero represents a zero-padded value.

The formats `__2` and `002` are space-padded and zero-padded three-character day of year; there is no unpadded day of year format.

A comma or decimal point followed by one or more zeros represents a fractional second, printed to the given number of decimal places.

A comma or decimal point followed by one or more nines represents a fractional second, printed to the given number of decimal places, with trailing zeros removed.

For example "15:04:05,000" or "15:04:05.000" formats or parses with millisecond precision.