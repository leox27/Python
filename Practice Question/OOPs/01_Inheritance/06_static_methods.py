"""
#6. (Static Methods)

Create a class named Calculator.

Requirements
Create these static methods:
- add(a, b)
- subtract(a, b)
- multiply(a, b)
- divide(a, b)

Each method should print the result.
Do not create any instance variables.
Do not use the __init__() constructor.
Call all the methods using the class name.
"""

class Calculator():
    
    @staticmethod
    def add(a, b):
        print(f"Addition is {a+b}")
    @staticmethod
    def subtract(a, b):
        print(f"Subtraction is {a-b}")
    @staticmethod
    def multiply(a, b):
        print(f"Multiplication is {a*b}")
    @staticmethod
    def divide(a, b):
        print(f"Division is {a/b}")
        
Calculator.add(11, 12)
Calculator.subtract(11, 12)
Calculator.multiply(11, 12)
Calculator.divide(11, 12)
'''
Addition is 23
Subtraction is -1
Multiplication is 132
Division is 0.9166666666666666
'''
