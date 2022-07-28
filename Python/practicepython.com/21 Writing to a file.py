# Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play
# with some different code, use the code from the solution), and instead of printing the results to
# a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.
#
# Extras:
#
# Ask the user to specify the name of the output file that will be saved.

# This is the best way to write to a file. It automatically closes the file when leaving the with block
with open("20 write file.txt", "w") as open_file:
    words = open_file.write("These words came from the console")