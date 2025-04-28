# `pytest`
Testing framework what auto-discover tests, rich assertion introspection and support to parameterized and fixture-based testing.

Rich assertion introspection means that whenever a test fails we'll have a clear message of what failed and why.
## Defining tests
Your tests can be defined anywhere within files that start with `test_*` or end with `*_test.py`.
## Testing errors
You can use `pytest.raises` to assert that a function raises an exception.

It's a context manager and will pass the tests if any code raises the provided exception at any time within the context.
```python
import pytest

def test_divide_by_zero():
	with pytest.raises(ZeroDivisionError):
		10 / 0
```
## Class based tests
Every class that starts with `Test*` will be executed.

`pytest` supports the definition of the following methods as fixtures.
- `setup_module` module function that will be called once before all the functions.
- `teardown_module` module function will be called once after all the functions.
- `setup_class` class method that will be called once before all tests of a class.
- `teardown_class` class method that will be called once after all tests of a class.
- `setup_method` runs before each test.
- `teardown_method` runs after each test.
## Function based tests
Every function that starts with `test_*` will be executed.
### Fixtures for function tests
```python
import pytest

# Fixture definition
@pytest.fixture
def my_rectangle():
	return Rectangle(10, 20)

# Our functions can receive the fixture name as parameter
# This paremeter will be the return value of our fixture
def test_area(my_rectangle):
	assert my_rectangle.area() == 10 * 20

def test_perimeter(my_rectangle):
	assert my_rectangle.perimeter() == (10 * 2) * (20 * 2)
```

Fixtures can be made global by defining them in a `conftest.py` file.

Global fixture can be used anywhere, even within class based tests. In this case, the method should receive the name of the fixture as parameter just like function based tests.
## Mark
The mark mechanism provides a way to add metadata to your tests.
```python
import pytest


# This test will be skipped during execution and will be marked with an 's'
@pytest.mark.skip(reason="broken feature")
def test_sum_float():
	f = 0.1 + 0.2

	assert f == 0.3

# This tests will be run during execution and will be marked with a 'x'
# Use when the test is expected to fail but not because you're testing a failure condition.
@pytest.mark.xfail(reason="division by zero isn't possible")
def test_zero_division():
	1 / 0
```
### Mark parametrize
This mark allow us to provide a list of a set of arguments to our test function. The function will run one time for each element in the list. It's like table driven tests.
```python
import pytest

# This test will run 2 times. Each time with a differnt set of arguments.
@pytest.mark.parametrize("arg1, arg2, arg3", [(1, 2, 3), (3, 4, 7)])
def test_sum(arg1, arg2, arg3):
	arg_sum = arg1 + arg2
	assert arg_sum == arg3
```
## Mocking
Mocking in `pytest` mostly relies on the python [`unittest.mock package`](mock_introduction.md).
## CLI
`-s` is used to display print statements in the test.
`-m` used to run tests based on a given mark.