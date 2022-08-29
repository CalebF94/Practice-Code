######################################
# Video 1) Opening and Closing Files #
######################################
"""
Files are opened with the open statement
    - file = open('text_file.txt')

Files should always be closed after use, using close:
    - file.close()
"""

file = open('text_file.txt')
file.close()

"""
There are better ways of ensuring a file gets properly closed

1) Using a try: finally: block:
    - file = open('file.txt')
      try:
        processing steps
      finally:
        file.close()
        
        
2) Using with:
    - with open('file_name.txt') as file:
        # processing steps here
    
    - File automatically closes when the indendation changes
"""

################################
# Video 2) Reading From a File #
################################

# The read method reads the contents of a file as a number of bytes
with open('text_file.txt') as file:
        content = file.read(10)
        print(content)

# the readline method reads a single line from the file
with open('text_file.txt') as file:
        content = file.readline()
        print(content)

# the readlines method reads the contents of a file as a list
# it keeps the new lines characters
with open('text_file.txt') as file:
        content = file.readlines()
        print(content)


# So far we've only used read mode, You can explicitly state read mode with an
# additional argument to open()
with open('text_file.txt', 'r') as file:
        content = file.readlines()
        print(content)


##############################
# Video 3) Writing to a file #
##############################
"""
Files can be opened for writing with 'w'
        - opening in write mode will overwrite any previous file
        - just replace the 'r' with 'w'
"""

with open('text_file.txt', 'w') as file:
        # doing nothing to the file
        print('wordes')
