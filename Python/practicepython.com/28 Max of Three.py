# Implement a function that takes as input three variables, and returns the largest of the three. Do this without using
# the Python max() function!
#
# The goal of this exercise is to think about some internals that Python normally takes care of for us.
# All you need is some variables and if statements!

def max_of_list(number_list):
    maximum = number_list[0]

    for item in number_list:
        if item > maximum:
            maximum = item
    return maximum


print(max_of_list([1, 2, 3, 4, 10, 2, 3, 5, 6]))
