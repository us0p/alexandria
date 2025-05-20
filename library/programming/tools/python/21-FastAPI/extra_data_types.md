Some additional data types you can use:
- `UUID`: will be represented as `str` in requests and responses.
- `datetime.datetime`: will be represented as a `str` in `ISO 8601` format.
- `datetime.date`: will be represented as `str` in `ISO 8601` format.
- `datetime.time`: will be represented as `str` in `ISO 8601` format.
- `datetime.timedelta`: will be represented as a `float` of total seconds.
- `frozenset`: treated the same as `set` in requests and responses:
	- In requests, a list will be read, converting it to a `set`.
	- In responses, the `set` will be converted to a `list`.
- `bytes`: Treated as `str`, generated schema will specify that it's a `str` with `binary` "format".