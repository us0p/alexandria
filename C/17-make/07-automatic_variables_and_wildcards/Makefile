all: three four print
	# Outputs "all", since this is the target name
	echo $@

	# Outputs all prerequisites newer than the target
	echo $?

	# Outputs all prerequisites
	echo $^

# Wildcard:
# * -> searches your filesystem for matching filenames.
# * -> may be used in the target, prerequisites, or in the wildcard fn.

print: $(wildcard *.c)
	ls -la $?

thing_wrong := *.o

# When * matches no files, it's left as it is (unless run in the wildcard fn).
# Always wrap it in the wildcard fn:
thing_right := $(wildcard *.o)

# Fails, because $(thing_wrong) is the string "*.o"
# one: $(thing_wrong)

# Stays as *.o if there are no files that match this patter
# two: *.o
# 	echo "two"

# Works as you would exptect! In this case, it does nothing.
three: $(thing_right)
	echo "three"

# Same as rule three
four: $(wildcard *.o)
	echo "four"

# % -> When used in "matching" mode, it matches one or more characters in a string. This match is called the stem.
# % -> When used in "replacing" mode, it takes the stem that was matched and replaces that in a string.
# % -> is most used in rule definitions and in some specific functions.
