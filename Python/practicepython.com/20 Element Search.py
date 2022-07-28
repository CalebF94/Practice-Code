# Write a function that takes an ordered list of numbers (a list where the elements are in order from
# smallest to largest) and another number. The function decides whether or not the given number is
# inside the list and returns (then prints) an appropriate boolean.
#
# Extras:
# Use binary search.
import math
import random


def find_number_in_list(ordered_list, num_to_find):
    is_found = False
    upper_index = len(ordered_list)-1
    lower_index = 0
    temp_index = -1

    while not is_found:
        check_index = math.floor((upper_index+lower_index)/2)
        if ordered_list[check_index] == num_to_find:
            print(f"{num_to_find} is located at element {check_index}")
            is_found = True
        elif ordered_list[check_index] > num_to_find:
            # if not match, shift upper limit down
            temp_index = upper_index
            upper_index = check_index
            if temp_index == upper_index:
                print(f"{num_to_find} is not in list")
                break
        else:
            # if not match, shift lower limit up
            temp_index = lower_index
            lower_index = check_index
            if temp_index == lower_index:
                print(f"{num_to_find} is not in list")
                break
    return is_found


ord_list = sorted(random.choices(range(1, 100), k=70))
num = random.randint(1, 200)

print(find_number_in_list(ord_list, num))


