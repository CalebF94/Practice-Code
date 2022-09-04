"""
*INTERFACES*

Interface:
    - is a description of a n objects features and behaviors
        - set of attributes and methods that make up a class
        - Not the implementation
    - Some OOP languages have actual mechanisms called interfaces. Python doesn't have this
      because it has multiple inheritance
    - Completely different than user interfaces

Liskov Substitution Principle:
    Anywhere our program expects an instance of the parent class, we can also provide an
    instance of the child class. This is because the child class has the same capabilities
    as the parent class
    - It's a good idea to follow this principle when ever possible

When creating interfaces name them as i<interfacename>
"""


class PayrollObject:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def calculate_payroll(self):
        return 12345