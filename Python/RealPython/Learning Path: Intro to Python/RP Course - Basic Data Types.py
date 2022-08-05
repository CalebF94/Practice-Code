"""
Video 1) INTEGERS
Whole Numbers
Any length allowed up to computer limit
"""
a = 1
b = 10

# Can define a number in binary as well. Start number with 0b
c = 0b100101
print(c)

# Octal
c = 0o13424
print(f'Octal to dec: {c}')

# Hex
e = 0xabc124
print(f"hex to dec: {e}")
print(type(e))

# bin(), oct(), hex() to go to dec
num = 100
print(f'100 to bin: {bin(num)}')
print(f'100 to oct: {oct(num)}')
print(f'100 to hex: {hex(num)}')

'''
Video 2: Floats
Any decimal point number
Division always results in float even if result could be int
'''
print(type(4.1))

a = 2
b = 5
c = 6

print(f'Regular division 6/2: {c/a}')
print(f'Floor division 5//2: {b//a}')

# scientific notation
print(f'4e4: {4e4}')

'''
Video 3: Complex Numbers

'''
a = 2 +3j
print(type(a))

'''
Video 4: Stings
sequence of 0 or more characters
enclosed in single or double quotes
'''


'''
Video 5: Strings => Escape Sequences
You may need both single and double quotes inside a string
'''

# this code below throws an error
# s = "He said "I wasn't at school""

# use backslash to escape
s = "He said \"I wasn't at school today\""
print(s)

# New lines \n. \t for tabs
d = "This is line 1 \nTHis is line 2"
print(d)

'''
Video 6: Stings => Raw Strings
In raw strings escape characters are not interpreted
This may be needed for regular expressions b/c the backslash has special meaning
'''
# define a raw string
a = "Line 1\nLine2"
b = r"line 1\nLine2"
print(a)
print(b)


'''
Video 7: Triple Quoted Strings
Allow use of single and double quotes inside strings. Alternative to escape characters
Also useful for multiple lines
Most common use is for doc strings
'''
s = """This wouldn't "work" inside a normal string"""
print(s)

s = """This comment has line1
and this is line2"""
print(s)


'''
Video 8: Booleans
False = 0, True = any other value
'''
# Empty lists and dictionaries evaluate to false
l = []
d = {}

if l:
    print(f'l is True')
else:
    print(f'l is false')


'''
Video 9: COmposite data types
data types that are made up of other data types
1) Lists
2) Tuples
3) Set: Can only contain unique elements
4) Dictonary (dict): essentially a lookup table
'''
# defined with square brackets. mutable can be changed
l = [1, 2, 3]
print(l)
l[1] = 6
print(l)

# Tuple
t = (1, 2, 3, 4)
print(t)
#tuples are immutable once created the below line throws an error
# t[1] = 6

# sets. Created using set function
ls = [1,1,2,2,3,3,4,4,5]
set_list = set(ls)
print(f'set(ls): {set(ls)}')

# Dicts: Key and Value pairings
my_dict = dict()
my_dict['name'] = "Caleb"
my_dict['age'] = 28
print(my_dict)

# values in a dict
print(f'my_dict["age"] {my_dict["age"]}')

#get method is good incase you access a value that doesn't exist
print(my_dict.get('age'))
print(my_dict.get('phone', "That key doesn't exist"))

