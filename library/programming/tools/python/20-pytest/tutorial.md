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
### How to `monkeypatch/mock` modules and environments
The `monkeypatch` fixture helps you to safely set/delete attribute, dictionary item or environment variable, or to modify `sys.path` for importing.

All modifications will be undone after the requesting test function or fixture has finished. The `raising` parameter determines if a `KeyErro` or `AttributeErro` will be raised if the target of the set/deletion operation does not exist.

The `monkeypatch` fixture provides these helper methods for safely patching and mocking functionality in tests:
- `monkeypatch.setatt(obj, name, value, raising=True)`
- `monkeypatch.delattr(obj, name, raising=True)`
- `monkeypatch.setitem(mapping, name, value)`
- `monkeypatch.delitem(obj, name, raising=True)`
- `monkeypatch.setenv(name, value, prepend=None)`
- `monkeypatch.delenv(name, raising=True)`
- `monkeypatch.syspath_prepend(path)`
- `monkeypatch.chdir(path)`
- `monkeypatch.context()`

For usage examples refer to the documentation [here](https://docs.pytest.org/en/stable/how-to/monkeypatch.html)
## Capturing `stdout/stderr` output
During test execution any output sent to `stdout` and `stderr` is captured. In addition, `stdin` is set to a "null" object which will fail on attempts to read from it.

By default capturing is done by intercepting writes to low level file descriptors.
### Accessing captured output from a test function
The `capsys`, `capsysbinary`, `capfd` and `capfdbinary` fixtures allow access to `stdout`/`stderr` output created during test execution.
```python
def test_myoutput(capsys):
	print("hello")
	sys.stderr.write("world\n")
	captured = capsys.readouterr()
	assert captured.out == "hello\n"
	assert captured.err == "world\n"
	print("next")
	captured = capsys.readouterr()
	assert captured.out == "next\n"
```

The `readouterr()` call snapshots the output so far - and capturing will be continued. After the test function finishes the original streams will be restored.

The return value of `readouterr()` is a `namedtuple` with two attributes, `out` and `err`.
## CLI
`-s` is used to display print statements in the test.
`-m` used to run tests based on a given mark.