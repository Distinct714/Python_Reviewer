# CLASS ATTRIBUTES

# Class attributes belong to the class itself they will be shared by all the instances. 
# Such attributes are defined in the class body parts usually at the top, for legibility.

class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

# Creating an object in Python involves instantiating a class to create a new instance of that class. 
# This process is also referred to as object instantiation.


# CLASS AND INSTANCE VARIABLES

# In Python, variables defined in a class can be either class variables or instance variables, 
# and understanding the distinction between them is crucial for object-oriented programming.

# Class Variables are the variables that are shared across all instances of a class. 
# It is defined at the class level, outside any methods. 
# All objects of the class share the same value for a class variable unless explicitly overridden in an object.

# Instance Variables are variables that are unique to each instance (object) of a class. 
# These are defined within the __init__ method or other instance methods. 
# Each object maintains its own copy of instance variables, independent of other objects.

# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Access class and instance variables
print(dog1.species)  # (Class variable)
print(dog1.name)     # (Instance variable)
print(dog2.name)     # (Instance variable)

# Modify instance variables
dog1.name = "Max"
print(dog1.name)     # (Updated instance variable)

# Modify class variable
Dog.species = "Feline"
print(dog1.species)  # (Updated class variable)
print(dog2.species)  


# ANOTHER SAMPLE

class sampleclass:
    count = 0     # class attribute

    def increase(self):
        sampleclass.count += 1

# Calling increase() on an object
s1 = sampleclass()
s1.increase()        
print(s1.count)

# Calling increase on one more object
s2 = sampleclass()
s2.increase()
print(s2.count)

print(sampleclass.count)


# Class Method vs Static Method

# A class method takes class as the first parameter while a static method needs no specific parameters.
# A class method can access or modify the class state while a static method can’t access or modify it.
# In general, static methods know nothing about the class state. 
# They are utility-type methods that take some parameters and work upon those parameters. 
# On the other hand class methods must have class as a parameter.
# We use @classmethod decorator in Python to create a class method and we use @staticmethod decorator to create a static method in Python.

# When to use the class or static method?
# We generally use the class method to create factory methods. 
# Factory methods return class objects ( similar to a constructor ) for different use cases.

# We generally use static methods to create utility functions.
