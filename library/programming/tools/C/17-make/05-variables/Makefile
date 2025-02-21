# Variables can only be strings.

files := file1 file2

some_file: $(files)
	echo "Look at this variable: " $(files)
	echo "You can look at it like this too: " ${files}
	touch some_file

file1:
	touch file1

file2:
	touch file2

clean:
	rm -rf file1 file2 some_file

# Single or double quotes habe no meaning to Make. They are simply characters
# that are assigned to the variable.
# a := one two # a is set to the string "one two"
# b := 'one two' # Not recommended. b is set to the string "'one two'"
