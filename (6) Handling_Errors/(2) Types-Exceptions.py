
# SEVERAL TYPES OR BUILT-IN OF EXCEPTIONS

# Exception Handling allows you to prevent program failure by processing potential exceptions in the way you need.

# A traceback can be thought as report providing information including what type of error occurred and where it occurred.


# NameError exception is raised when an unknown variable is used or when the variable is not defined.

try:
    address = "Think this as not included here."
    name = "Joshua"
    print(address)
except NameError:
    print("The variable is unknown")


# SyntaxError exception is raised when a syntax mistake in the code is encountered.
# This could be missing commas, parenthesis etc.

# IndentationError exception is raised when indentation is not correct.

# IndexError is raised when accessing an element using an index that is outside its valid range.

# TypeError exception is raised when a function is called on a value of an incorrect data type.

# ("Hello" + 10)

# ValueError exception is raised when a function receives a value of a correct type but the value itself is not within acceptable range.

# float("Hello")

# KeyError exception is raised when a key does not exist in a dictionary.


try:
    food = ["Burger", "Pizza", "Fries"]
    food.remove(7)
    print(food)
except:
    print("Out of range")


# ZeroDIvisionError is raised when the second operator in a division is zero

# Using Multiple Except Block:
try:
    number1 = int(input("Enter First Random Number: "))
    number2 = int(input("Enter Second Random Number"))
    print(number1 / number2)

except ZeroDivisionError as error:
    print(error)

except ValueError:
    print("Invalid Number")


# ModuleNotFoundError is raised when a module does not exist.

# FileNotFoundError is raised when a file or directory does not exist.

# KeyError is raised when a key does not exist in the dictionary.


# Creating Exceptions in class with function:

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
       

def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too big!")
    
    if x < 50:
        raise ValueTooSmallError("Value is too small!")

try:
    test_value(101)

except ValueTooHighError or ValueTooSmallError as e:
    print(e)


# Explore more here