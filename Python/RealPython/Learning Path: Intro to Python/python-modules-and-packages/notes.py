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
# def importer():
#     from mod import printy
#     printy("Hello Everyone")
#
#
# importer()


# it's safer to import modules inside a try statement
# try:
#     #non existent module
#     import foo
# except ImportError:
#     print('module not found')

#########################
# 5) The dir() function #
#########################
"""
- The dir() function returns a list of defined names in a namespace
- Without arguments, it produces an alphabetically sorted list of names in the 
    current local symbol table
    
"""
# print(dir())
#
# spam = [1, 2, 3, 4]
# print(dir())
#
# import mod
# print(dir())

"""
- When given the name of a module as an argument, dir() lists the names defined
    in the module
"""
# import mod
# print(dir())
#
# print(dir(mod))
#

#####################################
# 6) Executing a Module as a Script #
#####################################
"""
- you can run a module as a script. It might output anything, but it is essentially
    a python script 
- To run a script that is within the same directory type:  mod.py

- I modified the mod.py script include some print statements. Now if we import 
    the module we get output printed on the screen
    
- What if you don't want a module to generate output when imported?
    - When a .py file is imported the dunder variable __name__ is set to the 
        name of the module
    - When a .py file is run as a standalone script, __name__ is set to the 
        string __main__
        
    - A new module called fact.py was created with an if statement for the 
        __name__ variable
"""
import fact

#########################
# 7) Reloading a Module #
#########################
"""
A module is only loaded once per session
    - This works fine for function and class definitions 
    - But modules can contain executable statements as well
        - Usually for initialization
        - These statements will only be executed the first time a module is imported
"""
# import importlib
# # you can use the a function called reload() from the importlib module
# import mod
# importlib.reload(mod)

######################
# 8) Python Packages #
######################
"""
Python packages are useful when there are many modules to import
- Packages allow for a hirarchical structuring of the module namespace using
    dot notation
- Created a new directory inside the project that contains two
    modules
"""
# import pkg.mod1, pkg.mod2
# pkg.mod1.load_data()
# x = pkg.mod2.Location()

#############################
# 9) Package Initialization #
#############################
"""
The _init__.py file
- If a file named _init__.py is present in the package directory, it is invoked
    when the package or a module in the package is imported
- In our example it would be place at the same location as mod1 and mod2
    - We included  a print statement and a global variable
"""
# import pkg
# print(pkg.alist)

"""
the global variable can be accessed in mod1 or mod2 if we import pkg inside those
modules. Note that importing a single module will run _init__.py

The _init__.py file can also be used to automatically import all the other modules
    simply add an import statement for the other modules
"""
# import pkg
# pkg.mod1.load_data()
# pkg.mod2.clean_data()

##################################
# 10) Importing * From a Package #
##################################
"""
Created 3 more modules inside the pkg directory. I also renamed the __init__.py
file to _init__.py b/c tutorial wanted to delete it, but I wanted to keep it
"""

# print(dir())
# from pkg.mod3 import *
# print(dir()) # Message and merge_data are now included

"""
If we only did from pkg import * nothing would be added to dir().

Now we need to recreate the __init__.py with a list named __all__
- this __all__ list controls what is imported when import * is specified
    - for a package, when __all__ is not defined, import * does not import anything
    - for a module, when __all__ is not defined, import * imports everything
        except names starting with an underscore
"""
# from pkg import *
# print(dir()) #now all of the modules got imported

###################
# 11) Subpackages #
###################
"""
Packages can contain nested subpackages to arbitrary depth
    - pkg >> sub_pkg1
    - pkg >> sub_pkg2
    
You can create a package within a package

Relative subpackages
    - .. evaluates to the parent package
        - allows to call a sub package inside another sub package
            that is contained within the same parent package
    - ..sub_pkg
"""

