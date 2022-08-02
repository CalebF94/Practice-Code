# In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in!
# Because it would take a long time for you to input the months of various scientists, you can use my scientist birthday
# JSON file. Just parse out the months (if you don’t know how, I suggest looking at the previous exercise or its
# solution) and draw your histogram.

import json
from bokeh.plotting import figure, show, output_file
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
birthday_counts = Counter(birthday_months)

# To plot using bokeh, need different lists for x and y axes
x_categories = [months for months in month_dict.values()]
# x = [months for months in birthday_counts.keys()]
# y = [counts for counts in birthday_counts.values()]

# This is a quicker way of getting x and y. I think this is some sort of pointer reference
x, y = list(zip(*birthday_counts.items()))

# making plot
p = figure(x_range=x_categories)
p.vbar(x=x, top=y, width=.9)
show(p)
