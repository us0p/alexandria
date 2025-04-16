# `argparse`
The `argparse` module makes it easy to write user-friendly command-line interfaces.

It defines what arguments it requires, and `argparse` will figure out how to parse those out of `sys.argv`. The `argparse` module also automatically generates help and usage messages. The module will also issue errors when users give the program invalid arguments.

The `argparse` module’s support for command-line interfaces is built around an instance of `argparse.ArgumentParser`. It is a container for argument specifications and has options that apply to the parser as whole:
```python
parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
```
The `ArgumentParser.add_argument()` method attaches individual argument specifications to the parser. It supports positional arguments, options that accept values, and on/off flags:

```python
# Positional argument with a help message
parser.add_argument('filename', help="The name of the file")

# Changing default str type to int.
parser.add_argument('num', type=int) 

# Optional parameter that takes a value
parser.add_argument('-c', '--count')

# When the option is provided, will store True, stores False otherwise.
parser.add_argument('-v', '--verbose',
                    action='store_true')

# Providing a set of choices for an input
parser.add_argument('--choice', type=int, choices=[0,1,3])

# Counting the number of occurrences of the flag, starts at None
# e.g.: -o == 1, -oo == 2, --ocurrences == 1, --ocurrences --ocurrences == 2
parser.add_argument('-o', '--ocurrences', action="count")

# Providing default value
parser.add_argument('--age', type=int, default=26)
```

You can use `--` to tell `argparse` that everything after that is a positional argument.
e.g.: `-f` would fail as there's no option in the previous example, but `-- -f` would assign `-f` as the file name.

The `ArgumentParser.parse_args()` method runs the parser and places the extracted data in a `argparse.Namespace` object:

```python
args = parser.parse_args()
print(args.filename, args.count, args.verbose)
```