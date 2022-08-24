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