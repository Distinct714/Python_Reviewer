
# OBJECT ORIENTED PROGRAMMING PYTHON

# The classes and object function are useful in Python programming and it helps make your program more organized and more powerful.

# The class is a blueprint for creating objects, defining their characteristics and behavior.
# A class is a collection of objects. 
# A class defines a set of attributes and methods that the created objects (instances) can have.

# The word "self" refers to the actual object or instance of a class.
# The self parameter is a reference to the current instance of the class. 
# It allows us to access the attributes and methods of the object that belong to the class.

# Object (Instance, Actual Information) is a bundle of related attributes (variables) and methods (functions).
# An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data.

# SAMPLE ONE
class Dog:
    def bark(self):
        return "Awoof!"

y = Dog()
print(y.bark())

# SAMPLE TWO
class Computation:
    def addition(self, x, y):
        return x + y

compute = Computation()
print(compute.addition(3, 5))

# Attributes are the variables that belong to a class.
# Attributes are always public and can be accessed using the dot (.)

# MODIFYING ATTRIBUTES

class Person:
    def __init__(self, name, age):
        # Instance attribute
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self): 
        return self.age
    
    def set_name(self, name):
        self.name = name
        print(f"You name is now {name}")

    def set_age(self, age):
        self.age = age
        print(f"You age is set to {age}")

a = Person("Joshua", 20)

a.set_age(45)
print(a.get_age())

a.set_name("Arish")
print(a.get_name())