# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.
#
# For example, say I type the string:
#
#   My name is Michele
# Then I would see the string:
#
#   Michele is name My
# shown back to me.

def Reverse_Word_Order():
    long_string = input("Type a sentence >>")
    out_list = long_string.split()
    return " ".join(out_list[::-1])


print(Reverse_Word_Order())

