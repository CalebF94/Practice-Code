###########################
# Using Requirement Files #
###########################
"""
Pip will always install the latest published version of a package

Sometimes you'll want to load a specific version of a package that you know works.
What we really want to do is make a specification including dependencies that are
needed to run the file

Dependency Files:
    - List out dependencies and can be read in by Pip and install all of them
    - Using the command 'pip freeze' will print the current dependencies to the
        stdout
    - However what we'll really want to do is redirect this to a dependency file
        - 'pip freeze > requirements.txt

    - can view file using 'cat requirements.txt'
    - If you change the == to ">=" then when pip reads requirement it will install
        the latest versions.
            - pip install --upgrade -r requirements.txt

    - What if one of the updates to a package breaks everything
        - We need a way to specify not to use that version
        - In requirements file add comma after version and use >,< to specify
            version

"""