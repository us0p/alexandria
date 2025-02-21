# Raising exceptions:

# raise -> allows to force a specified exception to occur.

# raise NameError("Hi there!") -> Instantiate NameError with an argument.
# raise ValueError -> The class is instantiated with no arguments.

# re-raising an exception:
# try:
#     raise NameError("Hi there!")
# except NameError:
#     print("An exception flew by!")
#     raise

# BaseException is the common base class of all exceptions. 
# One of its subclasses, Exception, is the base class of all the non-fatal 
# exceptions. 
# Exceptions which are not subclasses of Exception are not typically 
# handled, because they are used to indicate that the program should 
# terminate. 
# They include SystemExit which is raised by sys.exit() and 
# KeyboardInterrupt which is raised when a user wishes to interrupt the 
# program.
# Programmers are encouraged to derive new exceptions from the Exception 
# class or one of its subclasses, and not from BaseException.
# It’s recommended to only subclass one exception type at a time to avoid 
# any possible conflicts between how the bases handle the args attribute,
# as well as due to possible memory layout incompatibilities.

# For BaseException, Exception and its subclasses, if str() is called on an
# instance of this class, the representation of the arguments to the
# instace are returned, or the empty string when there where no arguments.

# The following attributes are present in all of instances of BaseException:
# args -> The tuple of arguments given to the exception constructor.
# add_note(note: str) -> Add the string note to the exception’s notes which
#                        appear in the standard traceback after the 
#                        exception string.
# __notes__ -> A list of the notes of this exception, which were added with
#              add_note(). This attribute is created when add_note() is 
#              called.


# Raising Multiple exceptions:
# To raise multiple exceptions at once, we use the builtin ExceptionGroup,
# that wraps a list of exception INSTANCES so that they can be raised
# together.
# ExceptionGroup is an exception itself, so it can be caught like any other
# exception.
def f():
    raise ExceptionGroup(
            "exception group name",
            [
                OSError(1),
                SystemError(2),
                ExceptionGroup(
                    "exception groups can be embedded",
                    [
                        OSError(3), # wont be handled again as it's repeated
                        RecursionError(4)
                    ]
                )
            
            ]
    )

# by using "except*" instead of "except", we can selectively handle only the
# exceptions in the group that match a certain type.
try:
    f()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")

# Enriching Exceptions with Notes.
# When an exception is created in order to be raised, it is usually 
# initialized with information that describes the error that has occurred. 
# There are cases where it is useful to add information after the exception
# was caught. For this purpose, exceptions have a method add_note(note) that 
# accepts a string and adds it to the exception’s notes list. The standard 
# traceback rendering includes all notes, in the order they were added, 
# after the exception.

# try:
#     raise TypeError('bad type')
# except Exception as e:
#     e.add_note('Add some information')
#     e.add_note('Add some more information')
#     raise
