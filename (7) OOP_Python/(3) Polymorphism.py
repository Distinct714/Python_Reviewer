# POLYMORPHISM

# The word "polymorphism" means "many forms".
# In programming, it refers to methods/functions/operators with the same name that can be executed on many objects or classes.
# It is often used in Class methods, where we can have multiple classes with the same method name.

# Polymorphism allows methods to have the same name but behave differently based on the object’s context. 
# It can be achieved through method overriding or overloading.

# Creating a parent class:
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("It can move!\n")

  def stop(self):
    print("You stop it!")
 
# The pass statement is a placeholder that does nothing.
# It is used when a statement is syntactically required but no code needs to run.
# Commonly used when defining empty functions, classes or loops during development.

# Creating child classes where it inherits the Vehicle methods, but can override them: 
class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("It can sail!\n")

class Plane(Vehicle):
  def move(self):
    print("It can fly!\n")


# Creating each object
car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

# Recall nested loop
for x in (car1, boat1, plane1):
  print(f"The brand is {x.brand}.")
  print(f"The model is {x.model}.")
  x.move()

# Child classes inherits the properties and methods from the parent class.

# In the example above you can see that the Car class is empty, but it inherits brand, model, and move() from Vehicle.

# The Boat and Plane classes also inherit brand, model, and move() from Vehicle, but they both override the move() method.

# Because of polymorphism, we can execute the same method for all classes.


# Types of Polymorphism

# 1. Compile-Time Polymorphism: This type of polymorphism is determined during the compilation of the program. 
#                               It allows methods or operators with the same name to behave differently based on their input parameters or usage. 
#                               It is commonly referred to as method or operator overloading.

# 2. Run-Time Polymorphism: This type of polymorphism is determined during the execution of the program. 
#                           It occurs when a subclass provides a specific implementation for a method already defined in its parent class, 
#                           commonly known as method overriding.

# Parent Class
class Dog:
    def sound(self):
        print("Dog Sound:")  # Default implementation

# Run-Time Polymorphism: Method Overriding
class Labrador(Dog):
    def sound(self):
        print("Labrador woofs")  # Overriding parent method

class Beagle(Dog):
    def sound(self):
        print("Beagle Barks")    # Overriding parent method

# Compile-Time Polymorphism: Method Overloading Mimic
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c  # Supports multiple ways to call add()

# Run-Time Polymorphism
dogs = [Dog(), Labrador(), Beagle()]
for dog in dogs:
    dog.sound()  # Calls the appropriate method based on the object type


# Compile-Time Polymorphism (Mimicked using default arguments)
calc = Calculator()
print(calc.add(5, 10))      # Two arguments
print(calc.add(5, 10, 15))  # Three arguments

# Explanation:

# 1. Run-Time Polymorphism:
# Demonstrated using method overriding in the Dog class and its subclasses (Labrador and Beagle).
# The correct sound method is invoked at runtime based on the actual type of the object in the list.

# 2. Compile-Time Polymorphism:
# Python does not natively support method overloading. Instead, we use a single method (add) with default arguments to handle varying numbers of parameters.
# Different behaviors (adding two or three numbers) are achieved based on how the method is called.


# ANOTHER SAMPLE

class Character:

    def __init__(self, name, element):
      self.name = name
      self.element = element

    def describe(self):
      print(f"{self.name} is a {self.element} character.")

class Weapon:
    def __init__(self, weapon):
      self.weapon = weapon
      print(weapon)

# MULTIPLE CLASSES
class Polearm(Weapon):
    def kind(self):
      print("You got a sharp spear!")

class Claymore(Weapon):
    def kind(self):
      print("You got a big sword!")

class Sword(Weapon):
    def kind(self):
      print("You got a dull shord!")

class Bow(Weapon):
    def kind(self):
      print("You got an arrow!!")

class Catalyst(Weapon):
    def kind(self):
      print("You got a magic!")

# Output
genshin_character = Character("Ganyu", "Cryo")
x = genshin_character.name, genshin_character.element
print(x)
genshin_character.describe()

y = Bow("Amos Bow")
y.kind()


