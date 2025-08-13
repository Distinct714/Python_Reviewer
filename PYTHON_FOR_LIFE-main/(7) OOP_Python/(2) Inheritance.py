# INHERITANCE

# Inheritance allows us to define a class (child class) that inherits all the methods and properties from another class (parent class).
# Inheritance is where we define many attributes and functions inside of class.
# It means creating another class and inheriting all of those attributes inside of it.
# It allows to inherit functionality from an existing class into a new class.

# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.
# It also inherits all the attributes and methods of the parent class.

# To create a class that inherits the functionality from another class, send the parent class as a parameter 
# when creating the child class:

# PARENT CLASS 

# Any class can be a parent class, so the syntax is the same as creating any other class.
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    return self.firstname, self.lastname

# CHILD CLASS

# When you add the __init__() function to the child class, it will no longer inherit the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)


# OBJECT

x = Student("Josh", "Bote")
x.printname()

y = x.firstname
print(y)

z = x.lastname
print(z)

# OR YOU CAN DO THIS INSTEAD

# The super() function is used to give access to methods and properties of a parent or sibling class.

# It returns an object that represents the parent class.

# If you want to inherit the same attributes in another class without copying it, use this.

class Parent:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)

x = Child("Hello, and welcome!")

x.printmessage()