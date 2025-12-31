## AWK
The basic function of `awk` is to search files for lines (or other units of text) that contain certain patterns. When a line matches one of the patterns, `awk` performs specified actions on that line.

`awk` is an **interpreted language**. The `awk` **utility** reads your program and then processes your data according to the instructions in your program. The `awk` **utility** is thus termed an **interpreter**.

`awk` programs are **data driven** (you describe the data you want to work with and then what to do when you find it).

Programs in awk consist of pattern-action pairs.

When you run `awk`, you specify an **awk program** that tells **awk** what to do.

The program consists of a series of **rules**. Each rule specifies one pattern to search for and one action to perform upon finding the pattern.

A rule consists of a a **pattern** followed by an **action**. The action is enclosed in braces to separate it from the pattern. Newlines usually separate rules.

```awk
pattern { action }
pattern { action }
...
```
## How to run awk programs
If the program is short, it is easiest to include it in the command line:

```bash
awk 'program' input-file1 input-file2 ...
```

If the program is long, it is usually more convenient to put it in a file:

```bash
awk -f program-file input-file1 ...
```

>There are single quotes around the **program** so the shell won't interpret any awk characters as special shell characters. Because of this, quotes are only needed when defining the program on the command line.
### Built-In Rules
#### BEGIN
`awk` executes statements associated with BEGIN before reading any input.

```awk
awk 'BEGIN {print "Don\47t Panic!"}'
```
#### END
The code associated with END executes after all input has been read.

```bash
awk '{ if (length($0) > max) max = length($0) }
	 END { print max }' input-file
```
#### NF
`NF` or **Number of Fields** is used to get the last field of the record.
```shell
awk 'NF > 0' input-file
```
#### NR
`NR` or **Number of Row** is used to get the number of the current row in the input (1 based).
```bash
awk '{ print NR }' input-file
```
### Comments
A comment starts with `#` and continues to the end of the line.

```bash
awk 'BEGIN {print "Do not Panic!"}; #this program prints a nice message'
```
### AWK Programs
#### Rules
In an `awk` rule, either the pattern or the action can be omitted, but not both.

If the pattern is omitted, then the action is performed for every line. If the action is omitted, the default action is to print all lines that match the pattern.

If you leave the braces empty, you create an empty action that does nothing.

```bash
awk '{ }' input-file
```

Does nothing as the action is empty and there's no rules.
##### Multiple rules
The `awk` utility reads the input files one line at a time. For each line, awk tries the patterns of each rule. If several patterns match, then several actions execute in the order in which they appear in the awk program.

```awk
# Prints the line that contains 12
/12/ { print $0 }

# Prints the line that contains 21
/21/ { print $0 }
```

If a line contains `12` and `21` it's going to be printed two times.
#### Actions
	awk is a **line-oriented** language. Each rule's action has to begin on the same line as the pattern. To have it on separate lines you **must** use [Backslash Continuation](#Backslash%20continuation).

```bash
awk 'BEGIN {
	print \
		"hello, world"
}'
```
#### Variables
In `awk`, variables are automatically initialized to zero.

```bash
ls -l | awk '{ sum += $5 }; END { print sum }'
```

This command is going to sum the size of all the files in the current directory and print the total sum.

Note that `sum` is initialized to 0.
#### Line continuation
Most often, each line in an awk program is a separate statement or rule.

```bash
awk '/12/ { print $0 }
	 /21/ { print $0 }' input-file
```

However, `gawk` ignores newlines after any of the following symbols and keywords:
```
, { ? : || && do else
```

A newline at any other point is considered the end of the statement.
##### Backslash continuation
You can continue a line by ending the first line with a backslash. A backslash followed by a newline is allowed anywhere in the statement, even in the middle of a string or regular expressions.

```bash
awk '/This regular expression is too long, so continue it\
 on the next line/ { print $1 }'
```

>For maximum portability of your awk programs, it is best to split your lines in the middle of a regular expression or a string.

>Backslash Continuation and [Comments](#Comments) do not mix.
##### Semicolon continuation
You can put more than one statement on a single line. This is accomplished by separating the statements with a `;`.

```bash
awk '/12/ { print $0 } ; /21/ { print $0 }'
```
### Command-Line
Any additional arguments on the command line are normally treated as input files to be processed in the order specified. However, an argument that has the form `var=value`, assigns the value `value` to the variable `var`.

```bash
awk -f program.awk file1 count=1 file2
```

`file1` and `file2` are input files, `count=1` is a variable declaration.

If you need to process a file whose name looks like a variable assignment, precede the file name with `./`.

```bash
awk -f program.awk file1 ./count=1 file2
```

`file1`, `./count=1` and `file2` are all input files to this program.

>All the command-line arguments are made available to your `awk` program in the `ARGV` array. CMD options and the program text are omitted from `ARGV`. All other arguments, including variable assignments, are included. As each element of `ARGV` is processed, `gawk` sets `ARGID` to the index in `ARGV` of the current element.

The variables actually receive the given values after all previously specified files have been read. In particular, the values of variables assigned in this fashion are not available inside a `BEGIN` rule.

If you need those variables to be available for `BEGIN` consider using the `-v` option.