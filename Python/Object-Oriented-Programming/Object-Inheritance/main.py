# from shapes.py

from ObjectInheritance.shapes import *

#video 1
# square = Square(4)
#
# print(square.perimeter())
# print(square.area())
#
#
# rectangle = Rectangle(3, 4)
#
# print(rectangle.perimeter())
# print(rectangle.area())
# print(square.__class__)# stating class of the square object
# print(square.__class__.__base__)# returns what Square class is based on


# Video 2
cube = Cube(3)
print(cube.surface_area())
print(cube.volume())


# demonstrating calling a parent's function
print(cube.what_am_i())
print(super(Cube, cube).what_am_i())
print(super(Square, cube).what_am_i())
