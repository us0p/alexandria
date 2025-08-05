# Fixtures for function tests
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

- Fixtures can be made global by defining them in a `conftest.py` file.
- Fixtures can requests other fixtures.
- A test/fixture can request more than one fixture at a time.

Global fixture can be used anywhere, even within class based tests. In this case, the method should receive the name of the fixture as parameter just like function based tests.
## Fixture duplication
Fixtures can also be requested more than once during the same test.
```python
import pytest

@pytest.fixture
def first_entry():
	return 'a'

@pytest.fixture
def order():
	return []

@pytest.fixture
def append_first(order, first_entry):
	return order.append(first_entry)

def test_string_only(append_first, order, first_entry):
	assert order == [first_entry]
```
If a **requested** fixture was executed once for every time it was **requested** during a test, then this test would fail because both `append_first` and `test_string_only` would see `order` as an empty list, but since the return value of `order` was cached (along with any side effects executing it may have had) after the first time it was called, both the test and `append_first` were referencing the same object, and the test saw the effect `append_first` had on that object.
## Auto-use
Are fixtures that are automatically requested by every test.
```python
# ...

@pytest.fixture(autouse=True)
def append_first(order, first_entry):
	return order.append(first_entry)

def test_string_only(order, first_entry):
	assert order == [first_entry]

def test_string_and_int(order, first_entry):
	order.append(2)
	assert order == [first_entry, 2]
```
In this example, the `append_first` fixture is an auto-use fixture. Because it happens automatically, both tests are affected by it, even though neither test **requested** it.
## Fixture scopes
Fixtures are created when first requested by a test, and are destroyed based on their `scope`
- `function`: default, fixture is destroyed at the end of the test.
- `class`: destroyed during teardown of the last test in the class.
- `module`: destroyed during teardown of the last test in the module.
- `package`: destroyed during teardown of the last test in the package where the fixture is defined, including sub-packages and sub-directories within it.
- `session`: destroyed at the end of the test session.
## Teardown with `yield` (recommended)
This fixtures `yield` instead of `return`. Any teardown code for that fixture is placed after the `yield`.

Once pytest figures out a linear order for the fixtures, it will run each one up until it returns or yields, and then move on to the next fixture in the list to do the same thing.

Once the test is finished, pytest will go back down the list of fixtures, but in the _reverse order_, taking each one that yielded, and running the code inside it that was _after_ the `yield` statement.
```python
class CostlyObject:
	# Instantiates a costly object
	...

@pytest.fixture
def create_costly_obj():
	co = CostlyObject()
	yield co
	co.destroy() # clean up resources

# ...
```
### Handling errors for yield fixture
If a yield fixture raises an exception before yielding, pytest won’t try to run the teardown code after that yield fixture’s `yield` statement. But, for every fixture that has already run successfully for that test, pytest will still attempt to tear them down as it normally would.
#### Safe fixture structure
The safest and simplest fixture structure requires limiting fixtures to only making one state-changing action each, and then bundling them together with their teardown code

The chance that a state-changing operation can fail but still modify state is negligible, as most of these operations tend to be transaction-based (at least at the level of testing where state could be left behind). So if we make sure that any successful state-changing action gets torn down by moving it to a separate fixture function and separating it from other, potentially failing state-changing actions, then our tests will stand the best chance at leaving the test environment the way they found it.

What matter is that no matter which one runs first, if the one raises an exception while the other would not have, neither will have left anything behind.