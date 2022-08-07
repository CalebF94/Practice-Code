"""
Operators and Expressions
This is an RP tutorial/Article. There is no video series associated with the notes
"""

'''Arithmetic Operators'''
# Operators: Special symbols that designate some sort of computation should be performed
# values that an operator acts on are called operands

a = 10 # operand
b = 20
print(a + b)

print(-b) #Unary Negation
print(b/a) # Division. Always gives float
print(b//3) # Floor division. rounds to next smallest whole number. Truncates mantissa
print(b//-3) # rounds down -6.333 goes to -7

# Comparison Operators
# typical of other languages
x = 1.1
y = 2.2
z = x + y
print(f'z==3.3: {z == 3.3}') # carful with float comparisons

# Logical Operators: True and False
# Typical of other languages

"""Evaluation of Non-Boolean Values in Boolean Context"""
# The following are considered False in Boolean Context
    # Any value numerically zero
    # An Empty String
    # Object of a built-composit data type which is empty (dict, list, dict, set)
    # special value denoted by the Python keyword None

'''Short circuiting on chained and and or expressions'''
a = 0
b = 1
# this causes an error
#b/a > 0

# one way to avoid this error is to take advantage of the short circuit
print(a != 0 and a/b > 0) # evaluation stops after a != 0

'''Selecting a Default Value'''
#suppose you want to assign a variable s, but if string is empty you want to assign a default value
string = 'foo bar'
s = string or '<default_value>'
print(s)

# with default value
string = ''
s = string or '<default_value>'
print(s)


'''Bitwise Operators
There's another tutorial that I will read for further details
'''
# compares bit by bit. if both bits are 1 => 1
print('0b{:04b}'.format(0b1100 & 0b1010))
# or
print('0b{:04b}'.format(0b1100 | 0b1010))
# xor
print('0b{:04b}'.format(0b1100 ^ 0b1010))
# each bit shifted right n place
print('0b{:04b}'.format(0b1100 >> 2))
# each bit shifted left n place
print('0b{:04b}'.format(0b0011 << 2))
