# COURSE: A BEGINNER"S GUIDE TO PIP

#############################################
# Scripts, Modules, Packages, and Libraries #
#############################################
"""
Terminology
    - script: a python file that contains commands in logical order. The program
        needs to actually do something not just contain code. A script is intended
        to run directly.

    - Modules: Are intended to be imported to other files. Defines classes,
        functions, variables, and other members for use in scripts that import
        them. They don't do anything on their own

    - Packages: a collection of related modules. Can be an individual module, but
        is usually a collection of them.

    - Standard Library: Collection of modules and packages that come bundled with
        installation of Python. Examples: dateutil, email, json
"""

####################################
# Why Can't Python Find my Modules #
####################################
"""
- Almost every Python installer comes bundled with a version PIP 
- Each PIP installer installs packages to a specific location on disk
    - usually site-packages are somewhere nearby
- This means that invoking PIP for the wrong version of Python will result in 
    packages being installed in an undesired location

A fix to this is to use virtual environments
VIRTUAL ENVIRONMENTS
    - Isolated container with a Python interpreter, PIP executable, and site
        packages directory
    - Many virtual environments can be "Activated' which temporarily tricks the
        shell into thinking that the only Python and PIP executables are the
        ones that exist in the virtual environment
    - Common practice is to use a different virtual environment for each Python
        package
    - Many ways to create virtual environments:
        - Venv, virtualenv, per, pipenv
"""
####################################
# What is a Package Manager        #
####################################
"""
Software often relies on other software to function properly
    - This "other software is called a dependency
    - if a dependency changes, it could break the software that depends on it

Package Manager
    - A tool that manages software and their dependencies
    - using a package manager will install the correct version of all it's 
        dependencies
    - It keeps track of all the packages installed, as well as their dependencies

"""

#####################################
# Getting Started with PIP and PyPI #
#####################################
"""
Python's package manager is called PIP
    - Allows us to install external packages not included in the standard library

PyPI
    - Python package index 
    - pypi.com to browse for new packages
    - 

To see a list of all possible arguments you can pass to pip
    - pip help


The package we'll be using is called requests. To install from terminal use:
    pip install requests

To update pip to latest version use the command:
    python -m pip install --upgrade pip

To list all of the packages we have installed:
    pip list

to show more info about any package use pip show:
    pip show requests

Now we should be able to use the requests package
"""
import requests

url = 'https://www.goolge.com'
response = requests.get(url)
print(f'Response returned: {response.status_code}, {response.reason}')
print(response.text[:200])

# To run this small script use the command
# python "A Beginner's Guide to Pip.py"