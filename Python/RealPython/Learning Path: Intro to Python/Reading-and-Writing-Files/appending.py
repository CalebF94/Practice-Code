################################
# Video 4) Appending to a file #
################################
"""
Opening a file in append mode with a allows adding of new content
    to the end of the existing file

The same methods can be used in append mode as write mode

"""

with open('text_file.txt', 'a') as file:
    content = 'A new ending for my text file!\n'
    file.write(content)