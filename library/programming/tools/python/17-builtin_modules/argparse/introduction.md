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
## Conflicting groups
Use `add_mutually_exclusive_group()` when you want to specify options that conflict with each other.

```python

group = parser.add_mutually_exclusive_group()
group.add("-l", "--left")
group.add("-r", "--right")
```
## Namespaces
`argparse.Namespace` is a simples class used by default by `parse_args()` to create an object holding attributes and return it.

This class is deliberately simple, just an `object` subclass with a readable string representation.
## Sub-commands
`add_subparser()` method is normally called with no arguments and returns a special action object. This object has a single method `add_parser()`, which takes a command name and any `ArgumentParser` constructor arguments, and returns an `ArgumentParser` object that can be modified as usual.

```python
# create the top-level parser
parser = argparse.ArgumentParser(prog='PROG')

parser.add_argument('--foo', action='store_true', help='foo help')
subparsers = parser.add_subparsers(help='subcommand help')

# create the parser for the "a" command
parser_a = subparsers.add_parser('a', help='a help')
parser_a.add_argument('bar', type=int, help='bar help')

# create the parser for the "b" command
parser_b = subparsers.add_parser('b', help='b help')
parser_b.add_argument('--baz', choices=('X', 'Y', 'Z'), help='baz help')
```

Note that the object returned by `parse_args()` will only contain attributes for the main parser and the `subparser` that was selected by the command line (and not any other `subparsers`). So in the example above, when the `a` command is specified, only the `foo` and `bar` attributes are present, and when the `b` command is specified, only the `foo` and `baz` attributes are present.
## `parser.set_defaults()`
Originally used to determine some additional attributes without any inspection of the command line to be added. 

Note that parser-level defaults always override argument-level defaults:

```python
parser = argparse.ArgumentParser()
parser.add_argument('--foo', default='bar')
parser.set_defaults(foo='spam')
parser.parse_args([]) # Namespace(foo='spam')
```

But it's great when used with `subparsers`. Defines which function should be executed when a determined `subparser` is invoked.

```python
# subcommand functions
def foo(args):
    print(args.x * args.y)

def bar(args):
    print('((%s))' % args.z)

# create the top-level parser
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(required=True)

# create the parser for the "foo" command
parser_foo = subparsers.add_parser('foo')
parser_foo.add_argument('-x', type=int, default=1)
parser_foo.add_argument('y', type=float)
parser_foo.set_defaults(func=foo)

# create the parser for the "bar" command
parser_bar = subparsers.add_parser('bar')
parser_bar.add_argument('z')
parser_bar.set_defaults(func=bar)

# parse the args and call whatever function was selected
args = parser.parse_args('foo 1 -x 2'.split())
args.func(args) # 2.0

# parse the args and call whatever function was selected
args = parser.parse_args('bar XYZYX'.split())
args.func(args) # ((XYZYX))
```