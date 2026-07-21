"""
#8. (Property Decorator with Validation)

Create a class named Student.
Requirements
Use the __init__() constructor.
Create these private instance variables:
- __name
- __age

Use @property for the name.
Use @name.setter to update the name.

Use @property for the age.
Use @age.setter to update the age only if age is between 5 and 100.

If the age is invalid, print:
"Invalid age"

Create one Student object.
Display the name and age.
Update both name and age using property setters.
Try setting an invalid age.
Display the final values.
"""

class Student():
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new_age):
        if 5 <= new_age <= 100: 
            self.__age = new_age
        else:
            print("Invalid age")
    
student1 = Student("Mayur Jadhav", 21)
student2 = Student("Suraj Lohar", 22)

print(f"Name: {student1.name}")
print(f"Age: {student1.age}")
print(f"Name: {student2.name}")
print(f"Age: {student2.age}")

student1.name = "Vishwas Vedpathak"
student1.age = 21

student2.name = "Varun Mane"
student2.age = 22

print(f"Name: {student1.name}")
print(f"Age: {student1.age}")
print(f"Name: {student2.name}")
print(f"Age: {student2.age}")

student1.name = "Janhavi Murate"
print(f"Name: {student1.name}")
student1.age = 4
print(f"Age: {student1.age}")
'''
Name: Mayur Jadhav
Age: 21
Name: Suraj Lohar
Age: 22
Name: Vishwas Vedpathak
Age: 21
Name: Varun Mane
Age: 22
Name: Janhavi Murate
Invalid age
Age: 21
'''


"""
@property with Multiple Private Members

- Use @property to create a getter for a private member.
- Use @property_name.setter to create a setter.
- Validation can be added inside the setter.
- The property is accessed like a normal attribute, without ().

Example:
    student.name
    student.name = "Mayur"

    student.age
    student.age = 21
"""
