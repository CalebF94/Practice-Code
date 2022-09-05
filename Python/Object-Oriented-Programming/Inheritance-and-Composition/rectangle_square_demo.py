class Rectangle:
    def __init__(self, length, height):
        self._length = length
        self._height = height

    @property # allows to call w/o parenthesis
    def area(self):
        return self._length * self._height

    def resize(self, new_length, new_height):
        self._length = new_length
        self._height = new_height


class Square(Rectangle):
    def __init__(self, side_size):
        super().__init__(side_size, side_size)


rectangle = Rectangle(2, 4)
#raises exception if the following is false
assert rectangle.area == 8

square = Square(2)
assert square.area == 4

rectangle.resize(3,5)
assert rectangle.area == 15

# we're making a Square into a Rectangle
square.resize(3,5)
print(f'Square area: {square.area}')

print('OK')