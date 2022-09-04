"""
*INHERITANCE IN PYTHON


"""

class MyClass:
    pass

c = MyClass()

"""
dir() function returns a list of the members(attributes and methods)
that make up the class

dir(c) has a bunch of methods even though we didn't make any. These are dunder methods
Many of these methods are being inherited from the Object class. Compare the dir() for 
c and o

All classes inherit from the Object class implicitly. Python uses these methods to manage
our classes/objects
"""
print("dif() function output")
o = object()
print(dir(c))
print(dir(o))
print('\n\n\n')

"""
Exception objects and inheritance

exception can be made with the raise statement. All exceptions must inherit from 
BaseException. Base exception is not designed to be inherited from directly, but we can 
inherit from Exception.

Exception has method for outputting a message
"""

print("MyError Output")


class MyError(Exception):  # MyError is inheriting from Exception
    def __init__(self, message):
        super().__init__(message)  # passing the message to the parent


raise MyError("Something went wrong")

