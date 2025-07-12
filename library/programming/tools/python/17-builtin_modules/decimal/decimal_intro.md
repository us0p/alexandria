This module provides support for fast correctly rounded decimal floating-point arithmetic:
- Decimals numbers can be represented exactly.
- The exactness carries over into arithmetic. For this reason, decimal is preferred in accounting applications which have strict equality invariants.
- Both binary and decimal floating point are implemented in terms of published standards. While the built-in float type exposes only a modest portion of its capabilities, the decimal module exposes all required parts of the standard. The programmer has full control over rounding and signal handling.

Decimal floating-point objects share many properties with the other built-in numeric types such as `float` and `int`:
- Math operations and special methods apply.
- Can be copied.
- Can be pickled.
- Can be printed.
- Can be used as dictionary keys.
- Can be used as set elements.
- Can be compared.
- Can be sorted.
- Can be coerced to another type (such as `float` or `int`)
## Example
```python
from decimal import *

# Returns information about the context used to create decimal numbers.
# If necessary you can set new values for precision, rouding, or enabled traps.
getcontext()

# Decimal instances can be constructed frmo integers, strings, floats, or tuples.

Decimal(10) # Decimal('10')
Decimal('3.14') # Decimal('3.14')
Decimal(3.14) # Decimal('3.140000000000000124344978758017532527446746826171875')
Decimal('NaN') # Decimal('NaN')
Decimal('-Infinity') # Decimal('-Infinity')
```

>The significance of a new Decimal is determined solely by the number of digits input. Context precision and rounding only come into play during arithmetic operations.

```python
from decimal import getcontext, Decimal

getcontext().prec = 6
a = Decimal('3.0') # Decimal('3.0')
b = Decimal('3.1415926535') # Decimal('3.1415926535')
c = Decimal('2.7182818285') # Decimal('2.7182818285')
d = b + c # Decimal('5.85987')
```

>If the internal limits of the C version are exceeded, constructing a decimal raises `InvalidOperation`.
## Context
Encapsulates settings that govern the behavior of arithmetic with `Decimal` numbers.

Includes:
- `prec`: Precision.
- `rounding`: [Rounding mode](#Rounding%20modes).
- `Emin`, `Emax`: Minimum and maximum exponent allowed.
- `capitals`: Whether `E` or `e` is used in scientific notation.
- `flags`: Status flags raised during operations. It's a dictionary of exceptional conditions that happened. Keys are set when a condition happens, but do not raise an exception unless the corresponding **trap** is set.
- `traps`: If a trap for a condition is set to `True`, Python raises an exception when that condition occurs. You can customize which exceptions you want to raise or just log.
```python
from decimal import getcontext, ROUND_CEILING, Decimal
 
ctx = getcontext()

ctx.prec = 8 # sets precision to 8
ctx.rounding = ROUND_CEILING # will always round positive numbers up.

ctx.traps[DivisionByZero] = False

ctx.clear_flags() # clear the dictionary of flags.
Decimal('1') / Decimal('0') # Result is infinity.
ctx.flags[DivisionByZero] # is True but doesn't raises as trap is not set.
```

Each thread has a context specific to it that you can access with `getcontext()`.
## `quantize`
Return a value equal to the provided value after rounding and with the same precision of the second operand.

If the exponent of the second operand is larger than that of the first, then rounding my be necessary.
```python
from decimal import Decimal

Decimal('1.41421356').quantize(Decimal('1.000')) # Decimal('1.414')
```
## Rounding modes
`ROUND_CEILING`: Round towards `Infinity`. Always round up if there's any remainder, but only if the number is positive:
```python
from decimal import Decimal, ROUND_CEILING

Decimal('2.1').quantize(Decimal('1'), rounding=ROUND_CEILING)  # -> 3
Decimal('-2.1').quantize(Decimal('1'), rounding=ROUND_CEILING) # -> -2
```

`ROUND_DOWN`: Round towards zero. Truncates the number by ignoring the decimal part.
```python
from decimal import Decimal, ROUND_DOWN

Decimal('2.9').quantize(Decimal('1'), rounding=ROUND_DOWN)  # -> 2
Decimal('-2.9').quantize(Decimal('1'), rounding=ROUND_DOWN) # -> -2
```

`ROUND_FLOOR`: Round toward `-Infinity`. Always round down if there's any remainder, but only if the number is negative.
```python
from decimal import Decimal, ROUND_FLOOR

Decimal('2.17').quantize(Decimal('0.1'), rounding=ROUND_FLOOR)  # -> 2.1
Decimal('-2.15').quantize(Decimal('0.1'), rounding=ROUND_FLOOR) # -> -2.2
```

`ROUND_HALF_DOWN`: Round to nearest with ties going towards zero.
```python
from decimal import Decimal, ROUND_HALF_DOWN

Decimal('2.17').quantize(Decimal('0.1'), rounding=ROUND_HALF_DOWN)  # -> 2.2
Decimal('-2.15').quantize(Decimal('0.1'), rounding=ROUND_HALF_DOWN) # -> -2.1
```

`ROUND_HALF_EVEN`: Round to nearest value. If equidistant (like 5), rounds to the **nearest even number**.
```python
from decimal import Decimal, ROUND_HALF_EVEN

Decimal('2.5').quantize(Decimal('1'), rounding=ROUND_HALF_EVEN)  # -> 2
Decimal('3.5').quantize(Decimal('1'), rounding=ROUND_HALF_EVEN)  # -> 4
```

`ROUND_HALF_UP`: Round to nearest with ties going away from zero.
```python
from decimal import Decimal, ROUND_HALF_UP

Decimal('2.5').quantize(Decimal('1'), rounding=ROUND_HALF_UP)  # -> 3
Decimal('-2.5').quantize(Decimal('1'), rounding=ROUND_HALF_UP) # -> -3
```

`ROUND_ROUND_UP`: Round away from zero, regardless of sign. Any non-zero fractional part causes the number to round up.
```python
from decimal import Decimal, ROUND_UP

Decimal('2.1').quantize(Decimal('1'), rounding=ROUND_UP)  # -> 3
Decimal('-2.1').quantize(Decimal('1'), rounding=ROUND_UP) # -> -3
```

`ROUND_05UP`: Round away from zero if last digit after rounding towards zero would have been 0 or 5; otherwise round towards zero.
```python
from decimal import Decimal, ROUND_05UP

Decimal('1.250').quantize(Decimal('1.00'), rounding=ROUND_05UP)  # -> 1.26 (last digit is 5, rounds up)
Decimal('1.251').quantize(Decimal('1.00'), rounding=ROUND_05UP)  # -> 1.25 (last digit is not 0 or 5)
Decimal('1.240').quantize(Decimal('1.00'), rounding=ROUND_05UP)  # -> 1.25 (0 triggers rounding up)
```
