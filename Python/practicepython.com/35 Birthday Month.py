# This exercise is Part 3 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 2, and Part 4
#
# In the previous exercise we saved information about famous scientists’ names and birthdays to disk. In this exercise,
# load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday
# in each month.
import json
from collections import Counter

month_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

with open('birthday_dictionary.json', 'r') as f:
    birthdays_dict = json.load(f)

birthday_months = [month_dict[int(birthdays.split("/")[0])] for birthdays in birthdays_dict.values()]

print(Counter(birthday_months))
