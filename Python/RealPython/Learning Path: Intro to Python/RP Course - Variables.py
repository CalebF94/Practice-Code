'''
First two videos of course were very basic. Notes not needed.
Video 3 and 4 Object References
'''

'''
An objects value is what is assigned to that object
n=3 the value is 3

The identity of an object is where that object is located. This can be accessed using the id() function]
'''
n = 123456565
print(f'n = {n}')
print(f'id(n): {id(n)}')

# two objects can have the same value but different ids
m = 123456565
print(f'm==n: {m==n}')
print(f'id(n): {id(n)}')
print(f'id(m): {id(m)}')

'''

Video 4: Naming Conventions
    - Can be any length
    - Can be upper or lower case
        : There is a convention but it won't throw an error
        : UPPER CASE typically refers to constants
    - Use lowercase and underscores for proper convention naming
    - Digits are acceptable, but not at beginning
    - Can use unicode characters as well
'''


'''
PEP: Python Enhancement Proposal
Contains naming conventions and other official documentation
'''


'''
Reserved Keyword:

These are words not available for variable names
'''
help('keywords')
