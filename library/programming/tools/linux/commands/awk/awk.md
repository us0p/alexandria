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
#### Including other files into your program (`gawk` only)
The `@include` directive can be used to read external `awk` source files. It can be used in conjunction with the `AWKPATH` environment variable.

>Source files may also be included using the `-i` option.

```awk
# test1
BEGIN {
	print "This is script test1."
}

# test2
@include "test1"
BEGIN {
	print "This is script test2."
}

# test3
# The file name can, of course, be a pathname
@include "../test2"
BEGIN {
	print "This is script test3."
}

$ gawk -f test3
-| This is script test1.
-| This is script test2.
-| This is script test3.
```

>The rules for finding a source file described in [AWKPATH](#The%20AWKPATH%20ENV%20in%20gawk) also apply to files loaded with `@include`.
#### Reading Input Files
If you specify input files, `awk` reads them in order, processing all the data from one before going on to the next.

The input is read in units called **records**, and is processed by the rules of your program one record at a time. By default, each record is one line. Each record is automatically split into chunks called **fields**.
##### How Input is Split into Records
The records and fields received from your program are kept track on a variable called `FNR`, which is reset to zero every time a new file is started.
###### Record Splitting with `awk`
Records are separated by a character called the *record separator* (`RS`). By default, the record separator is the newline character.

To use a different character for the record separator, simply assign that character to the predefined variable `RS`.

You can change the value of `RS` in the [BEGIN](awk.md#BEGIN) section, in which case it **must** be enclosed in double quotes.

```bash
awk 'BEGIN { RS = "u" } { print $0 }' file-input
```

Another way to change it is on the [command-line](awk.md#Command-Line), using the variable-assignment feature:

```bash
awk '{print $0 }' RS="u" file-input
```

Reaching the end of an input file terminates the current input record, even if the last character in the file is not the character in `RS`.
###### Record Splitting with `gawk`
The value of `RS` is not limited to a one-character string. If it contains more than one character, it's treated as a regular expression.

In general, each record ends at the next string that matches the regular expression. The next record starts at the end of the matching string.

When `RS` is a single character, `RT` contains the same single character. However, when `RS` is a regular expression, `RT` contains the actual input text that matched the regular expression.

If the input file ends without any text matching `RS`, `gawk` sets `RT` to the null string.

```bash
echo record 1 AAAA record 2 BBBB record 3 |
gawk 'BEGIN { RS = "\n|( *[[:upper:]]+ *)" }
			{ print "Record =", $0, "and RT = [" RT "]" }'
```

```text
-| Record = record 1 and RT = [ AAAA ]
-| Record = record 2 and RT = [ BBBB ]
-| Record = record 3 and RT = [ 
-| ]
```

> The use of `RS` as a regular expression and the `RT` variable are `gawk` extensions, they are not available in compatibility mode.
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
#### Naming Standard Input
You may wish to read one file, read standard input coming from a pipe, and then read another file.

The way to name the standard input, is to use a single, standalone dash `-`.

```bash
some_command | awk -f myprog.awk file1 - file2
```

Here, awk first reads `file1`, then it reads the output of `some_command`, and finally it reads `file2`.

You can never use `-` with the `-f` option to read program source code from standard input.
#### The `AWKPATH` ENV in `gawk`
with gawk, if the file name supplied to the -f or -i options does not contain a directory separator ‘/’, then gawk searches a list of directories (called the search path) one by one, looking for a file with the specified name.

The search path is a string consisting of directory names separated by colons.13 gawk gets its search path from the AWKPATH environment variable. If that variable does not exist, or if it has an empty value, gawk uses a default path

The default value for `AWKPATH` is `.:/usr/local/share/awk`. Since `.` is included at the beginning, gawk searches first in the current directory and then in `/usr/local/share/awk`
#### Exit Status
- `gawk` exits with the numeric value given to `exit statement`.
- If there were no problems, exits with `0`.
- If an error occurs, gawk exits with 1.
- If gawk exits because of a fatal error, the status is 2.
### RegEXP
In `awk` the two operators `~` and `!~` perform regular expression comparisons. Expressions using these operators can be used as patterns, or `if`, `while`, `for`, and `do` statements.

This example matches, all input records with the uppercase letter `J` somewhere in the first field.
```bash
awk '$1 ~ /J/' input-file

# Same functionality
awk '{ if ($1 ~ /J/) print }' input-file
```

The right hand side of a `~` or `!~` operator need not be a regexp constant. It may be any expression. The expression is evaluated and converted to a string if necessary, the contents of the string are then used as the regexp. A regexp computed in this way is called a *dynamic regexp*.

>Always prefer to use regexp constants instead of string constants. In string constants you need to duplicate your escape sequences as string constants are processed twice.

>For complete portability, do not use a backslash before any character not shown in the previous list or that is not an operator.
#### Controlling character interpretation via command-line
- **No options** (default): `gawk` provides all the facilities of POSIX regexps and the GNU operators.
- `--posix`: Match only POSIX regexps, GNU operators are not special (e.g., `\w` matches a literal `w`).
- `--traditional`: Match traditional Unix awk regexps. GNU operators are not special. POSIX [character classes](regexp_intro.md#Character%20Classes) are available.
#### Case Sensitivity in Matching
You can perform case-insensitive match at a particular point in the program by converting the data to a single case, using the `tolower()` or `toupper` functions:

```bash
awk `tolower($1) ~ /foo/ { ... }`
```

This converts the first field to lowercase before matching against it.

Another method, specific to `gawk`, is to set the variable `IGNORECASE` to a nonzero value. When set, all regexp string operations ignore case.

`IGNORECASE` can be set on the command line or in a `BEGIN` rule. Setting `IGNORECASE` from the command line is a way to make a program case insensitive without having to edit it.

>The value of `IGNORECASE` has no effect in `gawk` in its compatibility mode.