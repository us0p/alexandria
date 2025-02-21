# There are two distinguishable kinds of errors:
# Sintax errors - parsing errors
# Exceptions - errors detected during execution.

# Exceptions come in different types (ZeroDivisionError, NameError, etc).

# To handle exceptions in python we use a try..except block:

while True:
    try:
        x = int(input("Please enter a number: "))
    except ValueError:
        print("Oops! That's not a valid number. Try again...")
    except (RuntimeError, TypeError) as err:
        raise NameError
    else:
        print(f"Your number is {x}")
        print(f"The float representation of your number if {float(x)}")
        break
    finally:
        print("finally block executed")

# A try statement may have more than one except clause, to specify handlers 
# for different exceptions. At most one handler will be executed. An except
# clause may name multiple exceptions as a parenthesized tuple.

# The try … except statement has an optional else clause, which, when 
# present, must follow all except clauses. It is useful for code that must 
# be executed if the try clause does not raise an exception.

# The use of the else clause is better than adding additional code to the 
# try clause because it avoids accidentally catching an exception that 
# wasn’t raised by the code being protected by the try … except statement.

# If an unhandled exception occurs inside an except section, it will attach
# the new exception to the exception being handled, this indicates that an
# exception is a direct consequence of another.
# You can specify that a expection is the direct cause of another by using
# a "from" clause with "raise:
# raise RuntimeError from exc, where "exc" is the exception variable name.

# The try statement has another optional clause "finally" which is intended 
# to define clean-up actions that must be executed under all circumstances.
# If a finally clause is present, the finally clause will execute as the 
# last task before the try statement completes. The finally clause runs 
# whether or not the try statement produces an exception. 

# Important characteristics of the finally statement:
# If an exception occurs during execution of the try clause, the exception 
# may be handled by an except clause. If the exception is not handled by 
# an except clause, the exception is re-raised after the finally clause 
# has been executed.

# An exception could occur during execution of an except or else clause. 
# Again, the exception is re-raised after the finally clause has been 
# executed.

# If the finally clause executes a break, continue or return statement, 
# exceptions are not re-raised.

# If the try statement reaches a break, continue or return statement, the 
# finally clause will execute just prior to the break, continue or return 
# statement’s execution.

# If a finally clause includes a return statement, the returned value will 
# be the one from the finally clause’s return statement, not the value from 
# the try clause’s return statement.

# A class in an except clause matches exceptions which are instances of the 
# class itself or one of its derived classes (but not the other way around, 
# an except clause listing a derived class does not match instances of 
# its base classes).

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

# prints(B, C, D)
# if except B was the first, except C and D would be unreacheable as they
# are derived classes of B. All exceptions would match the base class B, 
# which in this case, would be the first block.
print("\nderived classes:")
for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
