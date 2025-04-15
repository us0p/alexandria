# match
It's used for pattern matching.

It match a subject value against predefined patterns.

Name bindings made during a successful pattern match outlive the executed block and can be used after the match statement.
Do not rely on variables remaining unchanged after a failed `match`.
## Guards
The logical flow of a case block with a guard follows:
- Check that the pattern in the case block succeeded. If the pattern failed, the guard is not evaluated and the next case block is checked. 
- If the pattern succeeded, evaluate the guard.
## Irrefutable Case Blocks
An irrefutable case block is a match-all case block. A match statement may have at most one irrefutable case block, and it must be last.

A case block is considered irrefutable if it has no guard and its pattern is irrefutable. A pattern is considered irrefutable if we can prove from its syntax alone that it will always succeed.

```python
flag = False
match (100, 200):
	case (100, 300): # Mismatch: 200 != 300
		print("case 1")
	case [100, 300]: # Mismatch: 200 != 300
		print("case 1")
	case (100, 200) if flag: # Successful match, but guard fails
		print("case 2")
	case (100, y): # Matches and binds y to 200
		print(f"case 3, y: {y}")
	case 100 | 300: # Matches 100 OR 300, Only the last subpattern can be irrefutable
		print("100 or 300")
	case 100 as one_hundred: # can be irrefutable if subject is irrefutable
		print(one_hundred)
	case _: # Wild card pattern, matches anything
		print("case 4, i match anything!")
```

>Added in version 3.10
