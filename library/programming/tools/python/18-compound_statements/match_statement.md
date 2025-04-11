# match
It's used for pattern matching.

It match a subject value against predefined patterns.

Name bindings made during a successful pattern match outlive the executed block and can be used after the match statement.
Do not rely on variables remaining unchanged after a failed `match`.

```python
flag = False
match (100, 200):
	case (100, 300): # Mismatch: 200 != 300
		print("case 1")
	case (100, 200) if flag: # Successful match, but guard fails
		print("case 2")
	case (100, y): # Matches and binds y to 200
		print(f"case 3, y: {y}")
	case _: # Pattern not attempted
		print("case 4, i match anything!")
```

>Added in version 3.10