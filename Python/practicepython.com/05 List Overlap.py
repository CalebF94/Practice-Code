
'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are
common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
'''
import random

a = random.choices(range(0, 100), k=random.randint(0, 100))
b = random.choices(range(0, 100), k=random.randint(0, 100))

combined = list(set(a).intersection(set(b)))
print(combined)



# def list_overlap(list1, list2):
#     out_list = []
#     for item in list1:
#         if item not in list2 and item not in out_list:
#             out_list.append(item)
#     return out_list
#
#
# print(list_overlap(a, b))


