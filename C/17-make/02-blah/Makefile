# The first time you run this, blah will be created.
# The second time you'll see: make: 'blah' is up to date.

#blah:
#	cc blah.c -o blah

# If we modify blah.c and then run make, nothing gets recompiled.

# To solve this, we add a prerequisite to our rule's target:
blah: blah.c
	cc blah.c -o blah.sh

# Running make again will cause Make to decided if it should run the
# blah target.
# It will only run if blah doesn't exist, or blah.c is newer than blah.

# What it's attempting to do is decide if the prerequisites of blah have
# changed since blah was last compiled. That is, if blah.c is modified, running
# make should recompile the file. and conversely, if blah.c has not changed, then
# it should not be recompiled.

# To make this happen, it uses the filesystem timestamps as a proxy to determine if
# something has changed.
