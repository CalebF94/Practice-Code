"""

WHEN TO USE STATIC METHODS
------------------------------
Static methods have one big limitation: They don't have access to the class or the
object instance. However this shows that a static method is independent of the
things around it.

In the example below we use a static method to calculate the area of a pizza.
While this is a round about way to complete this task, it demonstrates the static
method can also be called without an instance of Pizza being instantiated


"""
import math


class Pizza:
    def __init__(self, radius, ingredients):
        self.ingredients = ingredients
        self.radius = radius

    def __repr__(self):
        return f'Pizza({self.ingredients})'

    def area(self):
        return self._circle_area(self.radius)

    @staticmethod
    def _circle_area(r):
        return r ** 2 * math.pi


# calling the area function
print(Pizza(4.5, ['cheese']).area())

# calling the _circle_area() static method on the class itself
print(Pizza._circle_area(4.5))