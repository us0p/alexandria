# RegEXP
It's a way of describing a set of strings.

A regexp is defined inside a pair of slashes `//`.

>When a regexp is enclosed in slashes, such as `/foo/`, we call it a regexp constant.
## Escape Sequences
Escape sequences are character sequences beginning with a backslash `\`. It means that the next character should be taken literally, even if it would normally be a regexp operator.

```regexp
/a\+b/
```

Matches the three characters `a+b`.

The following list presents escape sequences and what they represent.
- `\b`: Backspace
- `\r`: Carriage return
- `\t`: Horizontal TAB
- `\v`: Vertical TAB
## Metacharacters
You'll find a list of metacharacters bellow and their utility.
- `\`: Suppresses the special meaning of a character when matching.
- `^`: Matches the beginning of a string. This metacharacter is known as an **anchor**. It's important to realize that it **doesn't match the beginning of a line (the point right after a newline character)**.
- `$`: Matches the end of a string. It's also known as an **anchor** and **does not match the end of a line (the point right before a new line character)**.
- `.`: Matches any single character, including the new line character.
- `[...]`: This is called a *bracket expression*. It matches any one of the characters that are enclosed in the square brackets. For example, `[MVX]` matches any one of the characters `M`, `V`, or `X` in a string.
	- `[0-9]`: Matches any single character that sorts between the two characters, based upon the system's native character set. In this example `[0-9]` is equivalent to `[0123456789]`.
- `[^...]`: This is a *complemented bracket expression*. It matches **any** characters except those in the square brackets.
- `|`: this is the *alternation operator* and it's used to specify alternatives. It has the **lowest precedence** of all the operators. For example `^P|[aeiouy]` matches any string that starts with `P` or contains (anywhere within it) a lowercase English vowel.
- `(...)`: Used for grouping, as in arithmetic. For example `@(samp|code)\{[^}]+\}` matches both `@code{foo}` and `@samp{bar}`. The left or opening parenthesis is always a metacharacter; to match one literally, precede it with a backslash. However, the right or closing parenthesis is only special when paired with a left parenthesis.
- `*`: Matches the preceding expression 0 or more times. It's classified as a **greedy** operator as it takes the maximum amount of character as possible. For example consider the following expression `ph*` and the two strings `p` and `phhhhhhhhhhooey`. The `*` is going to match both strings and in the last one, it's going to take all the `h`s.
- `+`: Similar to `*`, except that the preceding expression must be matched at least once.
- `?`: Similar to `*`, except that the preceding expression can be matched either once or not at all.
- `{n}, {n,}, {n,m}`: If there is one number in the braces, the preceding regexp is repeated `n` times. If there are two numbers separated by a comma, the preceding regexp is repeated `n` to `m` times. If there is one number followed by a comma, then the preceding regexp is repeated at least `n` times:
	- `wh{3}y`: Matches `whhhy`, but not `why` or `whhhhy`.
	- `wh{3,5}y`: Matches `whhhy`, `whhhhy`, or `whhhhhy` only.
	- `wh{2,}y`: Matches `whhy`, `whhhy`, and so on.

>The `*`, `+`, `?` as well as the braces `{` and `}`, have the highest precedence, followed by concatenation, and finally by `|`. As in arithmetic, parentheses can change how operators are grouped.
#### Character Classes
Is a special notation for describing lists of characters that have a specific attribute, but **the actual characters can vary from country to country and/or from character set to character set.**

| Class        | Meaning                                                                                                   |
| ------------ | --------------------------------------------------------------------------------------------------------- |
| `[:alnum:]`  | Alphanumeric characters                                                                                   |
| `[:alpha:]`  | Alphabetic characters                                                                                     |
| `[:blank:]`  | Space and TAB charaacters                                                                                 |
| `[:cntrl:]`  | Control characters                                                                                        |
| `[:digit:]`  | Numeric characters                                                                                        |
| `[:graph:]`  | Characters that are both printable and visible (a space is printable but not visible)                     |
| `[:lower:]`  | Lowercase alphabetic characters                                                                           |
| `[:print:]`  | Printable characters (characters that are not control ccharacters)                                        |
| `[:punct:]`  | Punctuation characters (characters that are not letters, digits, control characters, or space characters) |
| `[:space:]`  | Space characters (these are: space, TAB, newline, carriage return, formfeed and vertical tab)             |
| `[:upper:]`  | Uppercase alphabetic characters                                                                           |
| `[:xdigit:]` | Characters that are hexadecimal digits                                                                    |

If you want to match alphanumeric characters you can use `/[A-Za-z0-9]/` or with *character classes* `/[[:alnum:]]/`.
#### Equivalence classes
Locale-specific names for a list of characters that are equal. The name is enclosed between `[=` and `=]`. For example, the name `e` might be used to represent all of `e`, `ê`, `è`, and `é`. In this case, `/[[=e=]]/` is a regexp that matches any of `e`, `ê`, `è`, and `é`.