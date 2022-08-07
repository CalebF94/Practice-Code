# Section String Manipulation

"""String Operators"""
# Some operators are the same as numeric operators
# + concatenate
s = 'spam'
t = 'egg'
u = 'bacon'
print(s+t+u)

# * returns copies of string
n = 2
print(s*n) # n has to be integer
print(s*-1) # returns []. There is a blank line in output

# in operator. True if first operand is in second
print(s in 'I saw spamalot')
print('I saw' not in 'I saw the holy grail')


"""Built in Sting Functions"""
# chr()
print(f"chr(97): {chr(97)}")
print(f"chr(129363): {chr(129363)}")

# ord() converts character to integer
print(f'ord("a"): {ord("a")}')
#print(f'ord("a"): {ord("ab")}') # has to be single character

# len() returns number of items in container
s = "I am a string"
print(f'len(s): {len(s)}')

#str() # converts expression to string


"""Sting Indexing"""
# zero based
# index of last character is len(string) - 1
s = 'mybacon'
print(s[0])
print(s[1])
# negative indexing
print(s[-1])# last letter
print(s[-len(s)]) # first letter