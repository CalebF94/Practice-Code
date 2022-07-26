# Write a program (function!) that takes a list and returns a new list that contains all the elements of
# the first list minus all the duplicates.
#
# Extras:
#
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.


def List_Remove_Dups_Sets(list1, list2):
    out_list = [item for item in set(list1) if item in list2]
    return out_list


def List_Remove_Dups_Loops(list1, list2):
    out_list = []
    for item in list1:
        if item in list2 and item not in out_list:
            out_list.append(item)
    return out_list


a = [1, 1, 2, 2, 3, 5, 7, 8, 5]
b = [2, 3, 4, 8]

print(List_Remove_Dups_Sets(a, b))
print(List_Remove_Dups_Loops(a, b))