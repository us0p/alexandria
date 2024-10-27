# Dunder (Double Underscore) Methods
# Are the special methods that start and end with the double underscores. 
# Dunder methods are not meant to be invoked directly by you, but the 
# invocation happens internally from the class on a certain action. For 
# example, when you add two numbers using the + operator, internally, the 
# __add__() method will be called. 

num=10
res = num.__add__(5) 
print(res)

# __str__() -> It is overridden to return a printable string representation
#              of any user defined class.

# You can get a table with a list of available dunder methods and their
# description at:
# https://www.tutorialsteacher.com/python/magic-methods-in-python
