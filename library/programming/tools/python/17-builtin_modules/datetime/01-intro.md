# Module: datetime
Suplies classes for manipulating dates and times.  
While date and time arithmetic is supported, the focus of the implementation is on efficient attribute extraction for output formatting and manipulation.

## Aware and Naive objects
Date and time objects my be categorized as "aware" or "naive" depending on whether or not they include time zone information.

An aware objecte represents a specific moment in time that is not open to interpretation.

A naive object does not contain enough information to uniquely locate itself relative to other date/time objects.

In datetime and time modules, an aware object can be created with the 'tzinfo' attribute.

datetime module supplies only the 'timezone' class. This class should be used with the 'tzinfo' attribute.

## Available types
- date: Idealized naive date.
- time: Idealized time, independent of any particular day, assumes that every day has exatcly 24*60*60 seconds.
- datetime: Combination of date and time
- timedelta: A duration expressing the difference between two datetime or date
- tzinfo: Abstract base class for time zone information objects.
- timezone: Implements 'tzinfo' for the UTC fixed offset.

>Objects of these types are immutable

## Determining if an object is aware or naive
`date` objects are always naive.

`datetime` object `d` is aware if both of the following hold:
- `d.tzinfo` is not `None`
- `d.tzinfo.utcoffset(d)` does not return `None`

`time` object `t` is aware if both of the following hold:
- `t.tzinfo` is not `None`
- `t.tzinfo.utcoffset(None)` does not return `None`

The distinction between aware and naive doesn't apply to `timedelta` objects.

