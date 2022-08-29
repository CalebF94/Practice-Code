#####################################
# Video 5) File Locations and paths #
# #####################################
"""
So far we've only used files that are in our path, but typically it's not quite
    this simple. Often we'll want to read and write to a location not in the
    local path

File paths are broken up into three major parts:
    1) Path: where the file is located
        - Gives the location of the file in computer
        - RELATIVE PATHS
            - start in the current directory, starting with a directory or file
              name
            - .. goes up a folder level
        - ABSOLUTE PATHS
            - Give the full explicit path to a file. will start with a drive letter

        - the os module contains a function that will create an appropriate path based
             on the user's operating system
                - os.path.join
                - os.sep: adds a beginning slash

    2) filename: name of the file
    3) extension: .txt, .pdf etc
"""

# os package example
import os
folder_path = os.path.join('Users', 'Fred', 'Downloads')
print(folder_path)