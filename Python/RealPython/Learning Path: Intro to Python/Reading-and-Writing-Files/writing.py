##############################
# Video 3) Writing to a file #
##############################
"""
Files can be opened for writing with 'w'
        - opening in write mode will overwrite any previous file
        - just replace the 'r' with 'w'

The write method is used to commit a single string to an open file
    - You can use the write method multiple times

The writelines method is used to commit multiple strings to an open file

You can even have multiple files open at the same time.
    - This allows you to read from one file and write to another
"""
# opening a file and overwriting content
with open('text_file.txt', 'w') as file:
    # doing nothing to the file
    print('file is opened')


# writing a line to the file
with open('text_file.txt', 'w') as file:
    content = 'Some text for my text file\r\n'
    file.write(content)

# writing multiple lines
with open('text_file.txt', 'w') as file:
    content = 'Some text for my text file\n'
    file.write(content)
    additional = "More text for my text file \n"
    file.write(additional)

# writelines() method
with open('text_file.txt', 'w') as file:
    content = ['line1\n', 'line2\n', 'line3\n']
    file.writelines(content)

# Multiple files
with open('moby_dick.txt', 'r', encoding='utf-8') as file_in, \
     open('moby_dick_caps.txt', 'w', encoding='utf-8') as file_out:
    content = file_in.readlines()
    for line in content:
        file_out.write(line.upper())