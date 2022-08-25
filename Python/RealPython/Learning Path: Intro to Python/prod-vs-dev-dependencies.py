##########################################
# Production vs development dependencies #
##########################################
"""
Not every package you install will be a dependency
    - Example: testing packages
    - Typically just create a new requirements file:
        - requirements_dev.txt
        - add dev dependencies to file

In the production environment you'll want to lock the version
of each package to ensure no unexpected changes happen when a package
gets updated
    - can copy a file using: cp file.text new_file.txt
        - cp requirements.txt requirements_locked.txt
    - Simply change >= to == in the requirements file
    - Possibly create a new file called requirement_lock.txt

To see files in venv use:
    - ls | grep "^req" (doesn't work in windows)


To uninstall packages:
    - run the show command
    - pip show packagename. this will show details
    - use pip uninstall package name to remove package
        - add -y to skip the confirmation

"""