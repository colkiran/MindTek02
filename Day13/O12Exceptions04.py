"""
traceback
type error
message

interpreter will call a method called except_hook() with three args
    a. the exception class - TypeError, ValueError
    b. Exception value - Unsupported opperands.....
    c. traceback object - traceback
traceback object - A traceback object in Python is an object that encapsulates the call stack at a particular point in the program's execution, typically when an exception has occurred. It provides a way to trace the sequence of function calls that led to the exception, aiding in debugging and error analysis. Traceback objects are created and managed by the Python interpreter and can be accessed and manipulated using the traceback module.

"""
import sys
import traceback

def format_traceback(exc_type, exc_val, exc_traceback):
    print("Something went wrong....")
    print(exc_type)
    print(exc_val)
    print(exc_traceback)

sys.excepthook = format_traceback

def fun():
    print(1 + "hello")


fun()

