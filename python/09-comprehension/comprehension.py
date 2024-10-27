# List comprehension
# produces a list from 0-9.
l = [x for x in range(10)] 

# produces a list of squares from 0 to 9.
sqr = [x ** 2 for x in range(10)] 

# produces a list of squares from 0 to 9 only for even numbers.
even_sqr = [x ** 2 for x in range(10) if x % 2 == 0]

# produces a list by concatenating x with y. Loops at the the right are
# like inner loops from loops at the left.
alphabet = ['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
excell_columns = [x + y for x in alphabet for y in alphabet[1:]]

# Dict comprehension
# a dict mapping letter to positions
d = {chr(k + 65):k+1 for k in range(26)} 

# Set comprehension
# the folowing set: {0, 1}
s = {x % 2 for x in range(10)} 

# Note that comprehensios are faster than loops.
