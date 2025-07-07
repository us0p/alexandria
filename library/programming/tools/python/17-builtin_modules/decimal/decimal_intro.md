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