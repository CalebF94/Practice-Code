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

"""
String Slicing
"""
# is s is string s[m:n] will return portion of s
# starting with position m
# up to not including position n
# returns n-m items
s = "mybacon"
print(f's[2:5]: {s[2:5]}')

# omitting first index starts at beginning
print(f's[:5]: {s[:5]}')

# omitting last extends to last of string
print(f's[2:]: {s[2:]}')

# s[:] returns the entire string. returns a reference to string
print(s[:])

# Negative Indexing
print(f's[-5:-1]: {s[-5:-1]}') #5th from end to 2nd to end
print(f's[-5:7]: {s[-5:7]}') #5th from end to end

# Specifying stride(Step)
print(f's[0:7:2]: {s[0:7:2]}') #start at beginning every other
print(f's[1:7:2]: {s[1:7:2]}') #5th from end to end
print(f's[-::2]: {s[::2]}') # Can leave slices empty

# Negative Stride
s = "123456789"
print(f's[::-1]: {s[::-1]}') # reverses the string
print(f's[::-2]: {s[::-2]}') # starts and end and takes every other element


"""
Interpolating Variables into a string
f-strings: bookmarked a more in depth course as well
"""
# no new information in this video

"""
Modifying stings
Strings are immutable
"""
# can't make assignment in a string
s = 'mybacon'
#This throws an error
#s[2]="f"

#workaround: use method to return modified string and reassign to
# same variable name
s = s.replace('b', 'f')
print(s)

