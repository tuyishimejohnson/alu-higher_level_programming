#!/usr/bin/python3
class Rectangle:
    """Defining a class with height and width"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new instance of the Rectangle class with the given width and height."""
    
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Deletes an instance of the Rectangle class."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        return 2 * (self.width + self.height) if self.width != 0 and self.height != 0 else 0

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """Returns a string representation of the rectangle to be able to recreate a new instance by using eval()."""
        return f"Rectangle({self.width}, {self.height})"
