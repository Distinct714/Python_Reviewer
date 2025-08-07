# STATIC METHOD

# Unlike class attributes, instance attributes are not shared by objects. 
# Every object has its own copy of the instance attribute (In case of class attributes all object refer to single copy). 
# To list the attributes of an instance/object, we have two functions:- 1.

# vars()  This function displays the attribute of an instance in the form of an dictionary.

# dir()   This function displays more attributes than vars function,as it is not limited to instance. 
#         It displays the class attributes as well. It also displays the attributes of its ancestor classes.

class Sample:
    def __init__(self):
        self.name = "None"
        self.salary = 4000

    def show(self):
        print(self.name)
        print(self.salary)

sample_info = Sample()
print("Dictionary form :", vars(sample_info))
print(dir(sample_info))

# A static method does not receive an implicit first argument. 
# A static method is also a method that is bound to the class and not the object of the class. 
# This method can’t access or modify the class state. It is present in a class because it makes sense for the method to be present in class.


class MyClass:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def get_max_value(x, y):
        return max(x, y)

# Create an instance of MyClass
obj = MyClass(10)

print(MyClass.get_max_value(20, 30))  

print(obj.get_max_value(20, 30)) 


# Below is the complete Implementation:
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person("Joshua", 20)
person2 = Person.fromBirthYear("Joshua", 2004)

print(person1.age)
print(person2.age)


print(Person.isAdult(22))
