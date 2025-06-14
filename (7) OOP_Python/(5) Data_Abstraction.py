
# DATA ABSTRACTION

# Abstraction hides the internal implementation details while exposing only the necessary functionality. 
# It helps focus on “what to do” rather than “how to do it.”

# Types of Abstraction:

# 1. Partial Abstraction: Abstract class contains both abstract and concrete methods.
# 2. Full Abstraction: Abstract class contains only abstract methods (like interfaces).

from abc import ABC, abstractmethod

class Dog(ABC):  # Abstract Class
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):  # Abstract Method
        pass

    def display_name(self):  # Concrete Method
        print(f"Dog's Name: {self.name}")
 
class Labrador(Dog):  # Partial Abstraction
    def sound(self):
        print("Labrador Woof!")

class Beagle(Dog):    # Partial Abstraction
    def sound(self):
        print("Beagle Bark!")

# Example Usage
dogs = [Labrador("Buddy"), Beagle("Charlie")]
for dog in dogs:
    dog.display_name()  # Calls concrete method
    dog.sound()         # Calls implemented abstract method

# Abstraction ensures consistency in derived classes by enforcing the implementation of abstract methods.