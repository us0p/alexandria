# WITH statement
Used to wrap the execution of a block with methods defined by a [context manager](context_manager.md).
```python
# Commong syntax
with A() as a:
	pass

# With more than one item, the context managers are processed as if multiple with statements were nested.
with A() as a, B() as b:
	pass

# The statement above is equivalent to:
with A() as a:
	with B() as b:
		pass

# Can also be written as:
with (
	A() as a,
	B() as b,
):
	pass
```