#A Makefile consists of a set of rules: A rule generally looks like this:
#targets: prerequisites
#	command
#	command
#	command
#
# The targets are file names, separed by spaces. Typically, there is only one per rule.
# The commands are a series of steps typically used to make the target(s). These need to start with a tab character, not spaces.
# The prerequisites are also file names, separated by spaces. These files need to exist before the commands for the target are run. Also called dependencies

hello:
	echo "Hello, World"
	echo "This line will always print, because the file hello does not exist."

# In this example:
# We have a target called hello;
# The target has two commands;
# This target has no prerequisites;
#
# As long as the hello file doesn't exist, the commands will run. If hello does exist, no commands will run.

# If you simply run make, since there's no target supplied as an argument to the make command, the first target
# is run.
