Enumerations are created either by using class or function-call syntax:
```python
from enum import Enum

class Color(Enum):
	RED = 1
	GREEN = 2
	BLUE = 3


Color = Enum('Color', [('RED', 1), ('GREEN', 2), ('BLUE', 3)])
```

>Even though we can use class syntax to create Enums, Enums are not normal Python classes.
## Nomenclature
- The class `Color` is an enumeration.
- The "attributes" are **enumeration member (or members)** and are functionally constants.

>Member values can be anything. If the exact value is unimportant you may use `auto` instances and an appropriate value will be chosen for you. Note that mutable/unhashable values, such as `dict`, `lists` or a mutable `dataclass`, can be used, they will have a quadratic performance impact during creation.
## Example
```python
from enum import Enum # Base class for all enum enumerations.

class Color(Enum):
	RED = 1
	GREEN = 2
	BLUE = 3

## Accessing member name:
print(Color.BLUE.name) # 'BLUE'

## Accessing member value:
print(Color.BLUE.value) # 3
```