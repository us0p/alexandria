Is a library for testing in Python. It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.

Mock is designed for use with `unittest` and is based on the `action -> assertion` pattern instead of `record -> replay` used by many mocking frameworks.

## `Mock` and `MagicMock`
Are objects that create all attributes and methods as you access them and store details of how they have been used.

You can configure them, to specify return values or limit what attributes are available, and then make assertions about how they have been used

```python
from unittest.mock import MagicMock

thing = ProductionClass()
thing.method = MagicMock(return_value=3)
thing.method(3, 4, 5, key='value') # returns 3
thing.method.assert_called_with(3, 4, 5, key='value')
```

The `MagicMock` class is just a `Mock` variant that has all of the magic methods pre-created for you (well, all the useful ones anyway).

```python
mock = MagicMock()
mock.__str__.return_value = 'foobarbaz'
print(str(mock)) # prints 'foobarbaz'

mock.__str__.assert_called_with()
```
## `side_effect`
Allows you to perform side effects, including calling functions and raising exceptions when a mock is called.

```python
from unittest.mock import Mock

mock = Mock(side_effect=KeyError('foo'))
mock() # Raises KeyError: 'foo'

values = {'a': 1, 'b': 2, 'c': 3}
def side_effect(arg):
    return values[arg]

mock.side_effect = side_effect
(mock('a'), mock('b'), mock('c')) == (1, 2, 3)
```
## `spec`
Configures the mock to take its specification from another object. Attempting to access attributes or methods on the mock that don't exist on the spec will fail with an `AttributeError`.

```python
import requests

from unittest.mock import Mock

mock = Mock(spec=requests)

mock.asdf() # AttributeError
```
## `patch`
It's a decorator/context manager that makes it easy to mock classes or objects in a module under test. The object you specify will be replaced with a mock (or other object) during the test and restored when the test ends

```python
from unittest.mock import patch

@patch('module.ClassName2')
@patch('module.ClassName1')
def test(MockClass1, MockClass2):
    module.ClassName1()
    module.ClassName2()
    assert MockClass1 is module.ClassName1
    assert MockClass2 is module.ClassName2
    assert MockClass1.called
    assert MockClass2.called

# Using as a context manager
with patch.object(ProductionClass, 'method', return_value=None) as mock_method:
    thing = ProductionClass()
    thing.method(1, 2, 3)
```
## Auto-speccing
Ensures that the mock objects in your tests have the same API as the objects they are replacing. Functions and methods (including constructors) have the same call signature as the real object.

This ensures that your mocks will fail in the same way as your production code if they are used incorrectly

Auto-speccing can be done through the `autospec` argument to patch, or the `create_autospec()` function.

```python
from unittest.mock import create_autospec

def function(a, b, c):
    pass

mock_function = create_autospec(function, return_value='fishy')
mock_function(1, 2, 3) # returns 'fishy'

mock_function.assert_called_once_with(1, 2, 3)

mock_function('wrong arguments') # TypeError: Missing required argument: 'b'
```

On classes `create_autospec` copies the signature of the `__init__` method, and on callable objects, copies the signature of `__call__`.