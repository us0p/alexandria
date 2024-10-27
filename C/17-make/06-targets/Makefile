# The all target
# An all target is the first rule listed, it will run by default
# if make is called without specifying a target:

all: one two three four five

one:
	touch one
two:
	touch two
three:
	touch three
# When there are multiple targets for a rule, the commands will be
# run for each target. $@ is an automatic variable that contains the
# target name.
four five:
	echo $@

clean:
	rm -f one two three
