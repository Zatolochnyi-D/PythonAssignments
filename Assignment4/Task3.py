import math

class Shape:                                        # Base
    def calculate_perimeter(self):                  # Base
        raise NotImplementedError()
    
    def calculate_area(self):                       # Base
        raise NotImplementedError()

class Rectangle(Shape):                             # Child
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def calculate_perimeter(self):                  # Override
        return 2 * self.__a + 2 * self.__b    

    def calculate_area(self):                       # Override
        return self.__a * self.__b
    
class Circle(Shape):                                # Child
    def __init__(self, radius):
        self.__radius = radius

    def calculate_perimeter(self):                  # Override
        return 2 * math.pi * self.__radius
    
    def calculate_area(self):
        return math.pi * math.pow(self.__radius, 2) # Override
    
rect = Rectangle(2, 4)
print(rect.calculate_perimeter())    # Expected: 12
print(rect.calculate_area())         # Expected: 8 
circle = Circle(3)
print(circle.calculate_perimeter())  # Expected: 18.84955592153876
print(circle.calculate_area())       # Expected: 28.274333882308138
shape = Shape()
shape.calculate_area()               # Expected: NotImplementedError