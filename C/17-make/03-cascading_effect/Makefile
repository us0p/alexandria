# Running this file:
# Make selects the target blah, because the first target is the default target
# blah requires blah.o, so make searches for the blah.o target
# blah.o requires blah.c, so make searches for the blah.c target
# blah.c has no dependencies, so the echo command is run
# The cc -c command is then run, because all of the blah.o dependencies are finished
# The top cc command is run, because all the blah dependencies are finished
# That's it: blah is a compiled c program

blah.sh: blah.o
	cc blah.o -o blah.sh # Runs third

blah.o: blah.c
	cc -c blah.c -o blah.o # Runs second

blah.c:
	echo "int main() { return 0; }" > blah.c # Runs first

## If you delete blah.c, all three targets will be rerun. If you edit it (and thus 
## change the timestamp to newer than blah.o), the first two targets will run. If you 
## run touch blah.o (and thus change the timestamp to newer than blah), then only the 
## first target will run. If you change nothing, none of the targets will run.
