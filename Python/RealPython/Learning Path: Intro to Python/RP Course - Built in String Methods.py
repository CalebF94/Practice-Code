"""
Built in String Methods
6 Videos
"""

"""
2.1: String Methods Overview
    Method is a specialized type of callable tightly associated with and object
    Invoked on a specific type of object
    Will cover case conversion, find and seek, classification, formatting
"""

"""
2.2 Case Conversion
    str.capitalize()
"""
print("\n\nCase Conversion")
s = 'egG BacOn SauSAGE loBSter'
print(f's: {s}')

# capitalizes all first letters, lowercases others. special chars not altered
print(f's.capitalize(s): {s.capitalize()}')

# lowercases all letters
print(f's.lower: {s.lower()}')

# swapcase(s) switches cases all letters
print(f's.swapcase(): {s.swapcase()}')

# s.title() Capitalizes first letter of each word
print(f's.title(): {s.title()}')
# can cause some wierd results with apostrophes and acronyms
s = "what's happened to ted's IBM stock?"
print(s)
print(f"s.title(): {s.title()}")
print(f"s.capitalize(): {s.capitalize()}")

# upper() Converts all letters to upper
print(f's.upper(): {s.upper()}')


"""
2.3: Find and Seek
    - Each method will have a start and end argument
"""
print("\n\nFind and Seek")
s = 'spam ham clam jam'
print(s)

# .count() counts the number of appearances of a substring
print(f's.count("am"): {s.count("am")}')

# can also only look at certain portion of string
print(f's.count("am", 0, 9): {s.count("am", 0, 9)}')


# .endswith() True if ends with specific string
s = "HamSausage"
print(s)
print(f's.endswith("age"): {s.endswith("age")}')
# only looks at substrings
print(f's.endswith("Sau", 0, 6): {s.endswith("Sau", 0, 6)}')

#.startswith() opposite to .endswith
print(f's.startswith("age"): {s.startswith("age")}')

#.find() returns the lowest index in s where substring is found
s='spam bacon egg sausage'
print(s)

print(f's.find("egg"): {s.find("egg")}')
# if something not found, returns -1
print(f's.find("lob"): {s.find("lob")}')


#.rfind() returns the highest index in s where substring is found
s='spam bacon egg sausage eggs'
print(s)

print(f's.find("egg"): {s.find("egg")}')
print(f's.rfind("egg"): {s.rfind("egg")}')
# if something not found, returns -1. .index() will throw error
print(f's.find("lob"): {s.find("lob")}')


"""
2.4: Character Classification
"""
print("\n\nCharacter Classification")
# str.isalnum() returns true if all chars are alpha numeric and not empty
s = "abc124"
print(s)
print(f's.isalnum(): {s.isalnum()}')

s = "abc$124"
print(s)
print(f's.isalnum(): {s.isalnum()}')

# isalpha() is similar except only looks for alphabetic
# isdigit() is similar except only looks for digit
# isidentifier() returns true if string is a valid name for variable, keyword, function, etc

print('spam32'.isidentifier())