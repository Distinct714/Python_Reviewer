
# DUNDER METHODS

class Fruit:
    
    #  __init__ method for initialization is invoked without any call, when an instance of a class is created.
    def __init__(self, fruit):
        self.fruit = fruit 
        
    # __repr__ method in Python defines how an object is presented as a string.
    def __repr__(self):
        return 'Object: {}'.format(self.fruit)
    
    # # __add__ method in Python defines how the objects of a class will be added together. It is also known as overloaded addition operator.
    def __add__(self, other):
        return self.fruit + other.fruit

# Driver Code (Main Program)
if __name__ == '__main__':
    
    # object creation
    fruit1 = Fruit("Apple")
    fruit2 = Fruit("Banana")
    
    # concatenate fruit object and a fruit
    print(f"{fruit1 + fruit2} is the best.")


# ANOTHER SAMPLE

class Lamp:

    # INITIALIZING ATTRIBUTES
    def __init__(self, brand, power_status) -> None:
        self.brand = brand
        self.power_status = power_status
        self.turned_on = False

    # CREATING METHODS
    def turn_on(self):
        if self.turned_on:
            print(f"Your {self.brand} lamp is already turned on.")
        else:
            self.turned_on = True
            print(f"Your {self.brand} lamp is now turned on.")

    def turn_off(self):
        if self.turned_on:
            self.turned_on = False
            print(f"Your {self.brand} lamp is now turned off.")
        else:
            
            print(f"Your {self.brand} lamp is already turned off.")    
    
    def run(self, seconds):
        if self.turned_on:
            print(f"Running {self.brand} lamp for {seconds} seconds")
        else:
            print("Something wrong! Check your Lamp!")

    # DUNDER METHODS
    def __add__(self, other):
        return f"{self.brand} + {other.brand}"
    
    # # The __str__() function controls what should be returned when the class object is represented as a string.
    # If the __str__() function is not set, the string representation of the object is returned:
    def __str__(self) -> str:
        return f"{self.brand} with rating: {self.power_status}"
    
    def __repr__(self) -> str:
        return f"Lamp Info: (brand: '{self.brand})' | power_status: '{self.power_status}'"


# OBJECT METHODS SAMPLE
thing = Lamp("Sumeru", "B")
thing.turn_on()
thing.turn_on()
thing.run(20)
thing.turn_off()
thing.turn_off()

thing2 = Lamp("Fontaine", "A")
thing2.turn_on()
thing2.turn_off()
thing2.run(1)

# This implements behavior for the + operator (addition).
print(thing + thing2)

# This defines behavior for when str() is called on an instance of your class.
# Without __str__, it will return the memory address of the class only.
print(thing)
print(thing2)

# This get called by built-int repr() method to return a machine readable representation of a type.
print(repr(thing))


# Explore more about magic method for OOP Python