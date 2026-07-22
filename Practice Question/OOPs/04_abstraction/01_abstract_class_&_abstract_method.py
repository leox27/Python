"""
#1. (Abstraction - Abstract Class and Abstract Method)

Create an abstract class named Shape.
Requirements
Import ABC and abstractmethod from the abc module.
Create an abstract method named area().

Create a child class named Circle.
Implement the area() method in Circle.

Use the formula:
Area = 3.14 * radius * radius

Create a Circle object.
Call the area() method.
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):
    
    def __init__(self, radius):
        self.radius =radius
        
    def area(self):
        result = 3.14*self.radius*self.radius
        return round(result, 2)

circle1 = Circle(eval(input("Enter radius of the Circle: ")))

print(circle1.area())
'''
Enter radius of the Circle: 12
452.16
'''


"""
Abstract Class

- An abstract class acts as a blueprint for child classes.
- It inherits from ABC.
- It can contain abstract methods and normal methods.
- An abstract method is created using @abstractmethod.
- Child classes must implement all abstract methods.
- Normal methods are optional to override.
- We cannot create an object of an abstract class directly.

Example:
    class Shape(ABC):

        @abstractmethod
        def area(self):
            pass
"""
