# Write a function that takes an ordered list of numbers (a list where the elements are in order from
# smallest to largest) and another number. The function decides whether or not the given number is
# inside the list and returns (then prints) an appropriate boolean.
#
# Extras:
# Use binary search.

def split_list(ordered_list, lower_limit, upper_limit):

def find_number_in_list(ordered_list, num_to_find):
    is_found = False
    length_list = len(ordered_list)

    while not is_found:
        search_ind = length_list/2
        search_num = ordered_list[search_ind]
        if search_num == num_to_find:
            print(f"{num_to_find} is in element {search_ind}")
            is_found = True
        else:
            if num_to_find > search_num:

