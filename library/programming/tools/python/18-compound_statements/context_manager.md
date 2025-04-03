# Context Manager
Is an object that defines the runtime context to be established when executing a [with statement](with_statement.md).

It handles the entry into, and the exit from, the desired runtime context for the execution of the block of code. 

Typical uses of context managers include saving and restoring various kinds of global state, locking and unlocking resources, closing opened files, etc.

The `object` class itself does not provide the context manager methods.

```python
# Implementation of the context manager protocol
class MyContext:
	def __enter__(self):
		pass

	def __exit__(self, exc_type, exc_value, traceback):
		pass
```
## Entering the context `__enter__`
It enters the runtime context related to this object.

The with statement will bind this method's return value to the target specified in the "as" of the statement, if any.

It returns this object or a object related to the context.
## Exiting the context `__exit__`
Exit the runtime related to this object. Arguments describe the exception that caused the context to be exited. If the context exited without an exception, all will be "None".

It return a Boolean flag indicating if any exception that occurred should be suppressed.

Returning a true value from this method will cause the with statement to suppress the exception. Otherwise the exception continues propagating after this method has finished executing. Exceptions that occur during execution of this method will replace any exception that occurred in the body of the with statement.

You should not reraise the passed-in exception. This is the caller's responsibility.

>[contextlib](https://docs.python.org/3/library/contextlib.html#module-contextlib) provides utilities for common tasks involving the `with` statement.