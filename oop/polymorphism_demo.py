import math

class Shape:
    """Base class for shapes."""
    def area(self):
        """Method to be overridden by subclasses."""
        raise NotImplementedError("This method should be overridden by subclasses")

class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        """Override the area method to calculate the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    """Circle class inheriting from Shape."""
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """Override the area method to calculate the area of the circle."""
        return math.pi * (self.radius ** 2)

