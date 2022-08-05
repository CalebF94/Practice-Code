'''
Video 10: Functions Math
abs(number)
divmod()
'''

# modular division
print(15 % 4)

# divmod() gives integer division and remainder
print(f'divmod(15, 4): {divmod(15, 4)}')

# powers 3**3
a = pow(3, 3)
print(a)


'''
Functions: Type Conversions

'''
#chr(ascii number)
#chr(0x####)

print(ord('A')) # returns ascii for string



'''
Iterables and Iteraters
'''
a = [True, True, True]
b = [True, False, True]
c = [False, False, False]

print(any(a))
print(any(b))
print(any(c))

print(all(a))
print(all(b))
print(all(c))

d = [1,5,43,5,4,2,6,7]
print(reversed(d)) # doesn't print out actuall reversed list

# python only does the work when needed
e = reversed(d)
print(list(e))

f = sorted(d)
print(f)

'''
Enumerate
'''
players = ['Mike', 'bob', 'john', 'hank']

for count, player in enumerate(players):
    print(count, player)


'''
Zip
USeful when you have multiple lists that need to be combined together
'''
country = ["Canada", 'UK', 'Egypt']
continent = ['America', 'Europe', 'Africa']

# without zip function to combine the lists in list of tuples you would use a loop
merged = []
for i in range(0, len(country)):
    merged.append((country[i], continent[i]))

print(merged)

# with the zip function
merged = zip(country, continent)
print(merged) # gives address
print(list(merged)) # gives values


## print function

for i in range(0, 10):
    print(i, end=" ") # will separate with space

'''
Variables, scopes, and references
'''
#vars() states variables dependent on scope
a=1

def function():
    b = 2
    print(vars())

print(vars())