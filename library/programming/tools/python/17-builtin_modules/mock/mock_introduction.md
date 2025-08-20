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
## patching external libraries imports
When you import a function from a library like this:
```python
# main.py
import library

def some_fn():
	library.library_fn()
	# ...
```
You bind the name `library` in your current module's namespace to the module object.

This way you can patch any method of `library` used in your module.
```python
# test_main.py
from unittest.mock import patch

from main import some_fn

@patch("library.library_fn")
def test_some_fn(mock_lb_library_fn):
	# make assertions
```

This works because there's still a reference to the actual module object that contains `library_fn`.

What happens when you use `from library import library_fn` instead?

In this import format, you're copying the reference to `library.library_fn` into your current namespace under the name `library_fn`. In your module, `bar` is just a local name pointing to the original function object at the time of import.

**It's no longer tied to `library.library_fn`**.

Using `@patch("library.library_fn")` doesn't work because **your module has its own reference to the original function**.

`@patch` **replace attribute on modules or classes**. So patching only works if the code you are testing **accesses the function through the module attribute**.

To make it work, you need to **patch your module's reference**.
```python
# main.py
from library import library_fn

def some_fn():
	library_fn()
	# ...

# test_main.py
from unittest.mock import patch

import main

# references your module's reference to the object.
@patch('main.library_fn')
def test_some_fn(mock_lb_library_fn):
	# make assertions
```

>**Rule of thumb**: Patch where the function is looked up, not where it's defined.
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