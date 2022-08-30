########################
# Video 1) What is OOP #
########################
"""
OOP:
    - Programs are composed of many object
        - Entity or thing in your program
        - often a noun
    - These objects also have properties and behaviors
        - properties = attributes
        - behaviors = methods
"""

##############################
# Video 2) Classes in Python #
##############################
"""
- Classes are used to create objects
- Classes define a type
- The process of creating an object from a class is called instantiation
    - my_name = 'Austin
    - Created/instantiated variable called my_name of the type str
"""

################################################
# Video 3 and 4) Class and Instance Attributes #
################################################
"""
Thinking Object-Oriently
    - Planning a project is important
        - What classes will you define
        - How many objects will you create
        - How will these objects interact
        
To create a class begin with a keyword class followed by class name

Instance Attributes:
    - Properties are actually called attributes
    - instance attributes are unique to each object created
    
__init__:
    -the intitializer function for a class
    - function gets run when we instatiate an instance of the class
    - It provides the object with it's initial attribute values
    - similar to constructors in other languages
    
Class Attributes:
    - Properies that are the same for every instance
    - for a dog species = mammal
    - get defined outside of the __init__ function and we cant change it
    
Accessing an attribute is done using dot notation
"""

# class Dog:
#     species = 'mammal' # Class Attribute
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# # instantiating dog objects
# philo = Dog("Philo", 5)
# mikey = Dog("Mikey", 6)
#
# # Retrieving information stored in attributes
# print(f'{philo.name} is {philo.age} and {mikey.name} is {mikey.age}')
#
# # we can even change their attribute
# mikey.age = 7
# philo.species = 'mouse'
# print(f'{philo.name} is {philo.age} year old {philo.species}',
#       f'{mikey.name} is {mikey.age} year old {mikey.species}', sep='\n')

#############################################
# Video 5) Adding Methods to a Python Class #
#############################################
"""
Instance Method:
    - A function that belongs to a class
    - Our dog class needs a nice way to print itself
"""


class Dog:
    species = 'mammal' # Class Attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound): # sound will need to be proviced later
        return f'{self.name} says {sound}'

    def birthday(self):
        self.age += 1
        # every time method is called self.age increases by 1

mikey = Dog('Mikey', 6)

print(mikey.description())
print(mikey.speak("ruff, ruff"))
mikey.birthday()
print(mikey.description())


###################################################
# Video 6 and 7)  Introduction to OOP Inheritance #
###################################################
"""
Don't Repeat yourself (DRY)
    - Avoid copy and pasting code between classes
    
Object Inheritance
    - Child Class inherits every attribute and method from the parent object
    - additional methods can be added to child class
    - a change in the parent class will also change the child class
        - Changes only have to be made in one location
"""


class Person:
    description = 'General Person'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'My name is {self.name} and I am {self.age} years old')

    def eat(self, food):
        print(f'{self.name} eats {food}')

    def action(self):
        print(f'{self.name} jumps')


class Baby(Person): # This indicates that class Baby will inherate from Person
    description = 'Baby' # 'Overwriting' the Person class

    def speak(self):
        print('ba ba ba ba')

    def nap(self):
        print(f'{self.name} takes a nap')


person = Person('Steve', 20)
person.speak()
person.eat('Pasta')
person.action()

baby = Baby('Ian', 1)
baby.speak()
baby.eat('baby food')
baby.action()

print(person.description)
print(baby.description)


# baby is of type Baby, but it's also a Person
print(isinstance(baby, Person))
# person is not a baby
print(isinstance(person, Baby))