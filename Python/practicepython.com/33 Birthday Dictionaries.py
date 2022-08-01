# This exercise is Part 1 of 4 of the birthday data exercise series. The other exercises are: Part 2, Part 3, and Part 4
#
# For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based
# on their name. Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the
# user to enter a name, and return the birthday of that person back to them.

birthday_dict = {
    "Caleb Fornshell": "07/03/1994",
    "Alex Fornshell": "02/03/1994",
    "Aaron Fornshell": "01/25/1986",
    "Lindsay Fornshell": "11/22/1983",
    "Kim Fornshell": "05/31/1962",
    "Don Fornshell": "11/02/1958"
}


def birthday_lookup():
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    for keys in birthday_dict.keys():
        print(keys)

    name = input(">>> Whose birthday do you want to look up? \n")
    if name in birthday_dict:
        print(f">>> {name}'s birthday is on {birthday_dict[name]}")
    else:
        print("That person doesn't exist in our database")


birthday_lookup()
