# Implement the same exercise as exercise 1 (create a program that asks the user to enter their name and their age.
# Printout a message addressed to them that tells them the year that they will turn 100 years old). except don't
# explicictly write out the year. Use the built-in Python datetime library to make the code you write work during every
# year, not, just the one we are currently in.

import datetime

name = input("What is your name? ")
age = int(input("How old are you? "))

datetime.date.today().year - age + 100
print(f'{name} will turn 100 in the year {datetime.date.today().year - age + 100}')
