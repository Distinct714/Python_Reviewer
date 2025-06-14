
# CLASS INITIALIZE

# The __init__ initialize double underscore is used in Python classes.
# All classes have a function called __init__, which is always executed when the class is being initiated.

# It is called automatically when an object is created from a class and allows us to 
# initialize the attributes of the object.

# Use the __init__ function to assign values to object properties, or other operations
# that are necessary to do when the object is being created.
# The __init__ function is called automatically every time the class is being used to create a new object.

# Attributes are the properties that define an object's individuality within a class.

class Pizza:
    
    def __init__(self, meat, cheese, sauce, vegetable): 
        # Left: Assign for Actual object name / Right comes from parameters
        # This map out what attributes of the class should have in object.
        self.meat = meat
        self.cheese = cheese
        self.sauce = sauce
        self.vegetable = vegetable

# Methods in objects are functions that belong to the object.
# It is a functions inside a class or a member of class. These are actions that an object perform within class.
# Objects can also contain methods. 

    def topping(self):
        if self.cheese == "swiss":
            return True
        else:
            return False
        
# class definitions cannot be empty, but if you for some reason have a class definition with no content, 
# put in the pass statement to avoid getting an error.

    def nothing():
        pass
