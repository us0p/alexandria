# clean is often used as a target that removes the output of other targets,
# but it is not a special word in Make. You can run make and make clean on
# this to create and delete some_file:

some_file.sh:
	touch some_file.sh

clean:
	rm -f some_file.sh

# Note that clean is doing two new things here:
# It's a target that is not first (the default), and not a prerequisite. That means it'll never run unless you explicitly call make clean
# It's not intended to be a filename. If you happen to have a file named clean, this target won't runt.
