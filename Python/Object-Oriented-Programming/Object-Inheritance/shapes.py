# simple class
# class Square:
#     # This is the class constructor. There's 1 parameter length that needs to be
#     # be supplied when instantiating a square
#     def __init__(self, length):
#         self.length = length
#
#     # Below are methods for the Square Class
#     def area(self):
#         return self.length * self.length
#
#     def perimeter(self):
#         return 4 * self.length


# We also want to create a rectangle
class Rectangle:
    # a rectangle has two attributes
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Again create perimeter and area methods
    def what_am_i(self):
        return "Rectangle"

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# It's better for the Square class to inharate from the Rectangle class

# notation for inheriting from Rectangle. If we don't change anything the Square
# class will be the same as the Rectangle class
class Square(Rectangle):
    # here we are overwriting the constructor
    def __init__(self, length):
            super().__init__(length, length)
            #super allows us to access the parents methods
            # in this case we're changing the __init__function
            # that's it Python will automatically change all references of width
            # to length


    def what_am_i(self):
        return "Square"


class Cube(Square):
    # same parameters as square so we don't need to redefine __init__. Cubes
    # will be instantiated with only one parameter, like a square, but
    # cube has two methods that aren't in its parent

    def what_am_i(self):
        return "Cube"

    # adding methods that only belong to Cube
    def surface_area(self):
        face_area = self.area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length


# Classes for multiple inheritance
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

    def what_am_i(self):
        return 'Triangle'


# the RightPyramid is going to inherit from triangle and squares
class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def what_am_i(self):
        return 'Right Pyramid'
