###################################################
# 1) Python Modules and Packages: An Introduction #
###################################################
"""
Modular programming:
    - The process of breaking a large unwieldly task into smaller chunks
    - Advantages include:
        1) simplicity
        2) maintainability
        3) reusability
        4) scoping
"""

#######################
# 2) Writing a Module #
#######################
"""
Three different styles of modules in python:
    1) A module written in Python itself (this video)
    2) A module written in C and loaded dynamically at run-time
    3) A built in module is intrinsically contained in the interpreter
    
The notes from this video reference mod.py. This file contains some variables a
simple function and a simple class.

We can import the objects inside mod.py using an import statement. Then we can
call the objects inside the module
"""
# import mod
# print(mod.a)
# print(mod.s)
# mod.printy("What is Up")


#############################
# 3) The Module Search Path #
#############################
"""
Where can you import a module from?
    - The interpreter searches for the file
        1) in the current directory
        2) in the PYTHONPATH environment variable list of directories
        3) The directories configured as part of your Python installation
        
    - To see the list of directories the terminal shows what directory your in
    - The interpreter starts in that same directory, and you can access files that
        are in that same directory
        
    - You can use the sys module to find a list of directories you can import from
"""
# import sys
# print(sys.path)#

"""
Where should you put your module file:
    - To ensure your module is found place the file in:
        1) The same directory as the input script or the current directory
        2) Modify PYTHONPATH environment variable to contain the directory where
            it is located. Or in one of the directories already in the PYHTONPATH
        3) In one of the directories configured as part of your Python installation

The other runtime solution is to modify the sys.path list at run time. It should 
look somethin like sys.path.append(f'C:filepath'). Remember this only works for 
the current session
"""
# I saved a copy of the mod  file in the directory below. called modtest.py
# sys.path.append(r'C:\Users\Caleb\PycharmProjects\PracticePythonProblems')
# print(sys.path) # added directory at end
# import modtest # ignore the error
# print(modtest.s)

"""
You can also see the location of a module using a dunder method __file__
This also works with preinstalled modules
"""
# print(modtest.__file__)
# import re
# print(re.__file__)

###########################
# 4) The Import Statement #
###########################
"""
What form can the import statement take
1) The simplest form
    - import <module_name>, <module_name2>
    - module contents not directly accessible to the caller. Need to use dot 
        notation. A new namespace is created

2) Individual objects from the module can be imported
    - from <module_name> import <name(s)>
    - the individual objects are directly accessible to the caller
    - Dot notation is not needed. Object imported into the caller's symbol table
        - Need to be careful if objects with the same name are in both namespaces
        
3) It is possible to import everythin from a module at once
    - from <module_names> import *
    - places all the names of objects into the local symbol table
        - the exception is objects beginning with an underscore
        - not usually recommended unless you know all names will not conflict
        
4) Individual objects can be imported with alternate names
    - from <module> import <name> as <alt_name>
    
5) Import the entire module under an alternate name
    - import <module> as <alt name
    
6) Import modules from inside a function
"""

#2
# from mod import s, printy
# printy("Hello all")

#3
# from mod import *
# printy("Words words words")

#4
# from mod import s as string, a as alist
# print(alist)
# print(string)

#5
# import pandas as pd

#6
def importer():
    from mod import printy
    printy("Hello Everyone")


importer()


# it's safer to import modules inside a try statement
try:
    #non existent module
    import foo
except ImportError:
    print('module not found')