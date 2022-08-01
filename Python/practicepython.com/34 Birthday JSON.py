# This exercise is Part 2 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 3, and Part 4
#
# In the previous exercise we created a dictionary of famous scientists’ birthdays. In this exercise, modify your
# program from Part 1 to load the birthday dictionary from a JSON file on disk, rather than having the dictionary
# defined in the program.
#
# Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file you
# have on disk with the scientist’s name. If you run the program multiple times and keep adding new names, your JSON
# file should keep getting bigger and bigger.
import json


def add_birthday():
    with open('birthday_dictionary.json', "r") as f:
        birthday_dict = json.load(f)

    new_name = input("Whose birthday do you want to add? ").title()
    if new_name not in birthday_dict.keys():
        new_birthday = input("When is this their birthday?")
        birthday_dict[new_name] = new_birthday
    else:
        print("{} already exists in the database".format(new_name))

    with open('birthday_dictionary.json', 'w') as f:
        json.dump(birthday_dict, f)


def print_birthday_dict():
    with open('birthday_dictionary.json', 'r') as f:
        birthday_dict = json.load(f)
    print(birthday_dict)


add_birthday()
