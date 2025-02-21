# Iterators
# Is an object which implements the iterator protocol, which consists of 
# the methods __iter__() which defines the iterator and __next__() which
# produces the next element.
# This protocol is used to allow an object to be iterated upon.

# Iterable
# Is an object that one can iterate over. It generates an iterator when
# passed to iter() method.
# The object must implement __iter__() to create the iterator, or a
# __getitem__() method with sequential indexes starting with 0.

# Iterable in Python cannot save the state of the iteration, each element
# in an iterable is produced by its __getitem_() method which treats every
# element separatedely.
# In iterators the state of the current iteration gets saved, which is then
# used to produce the next element.

# Iterator vs Iterable
# Strings, Lists, Tuples, Dictionaries, and Sets are iterable objects.

# The for loop is used to iterate over iterators.
# When provided with an iterable, the for loop creates an iterator with
# iter and executes the next() method for each loop. 

# Raising an StopIteration is how you prevent a iterator from going on
# forever.
