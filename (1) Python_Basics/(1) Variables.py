# START WITH COMMENT

# COMMENT   It starts with (#) hashtag that helps explain or document your code.
#           This was ignored by python in order to prevent the program from being executed during testing code.
#           This will serve as guide to your progress of code.

'''
You can also use this format or multiline/triple quotes when writing more notes in multiple lines.
However, it is recommended to use hashtag instead the format above.
'''

# print()   This function is used to send or print out a values (object) or any data and requires the use of parenthesis.
#           It was also used to output variables that will be displ ayed on the screen.

print("Hello, World!")

# Creating basic shape through print function.
print("   /|")
print("  / |")
print(" /  |")
print("/___|", "\n")

print("*" * 1)
print("*" * 2)
print("*" * 3)                          
print("*" * 4)
print("*" * 5)
print("*" * 6, "\n")
# Use for loop instead of this.

# The help() displays documentation about various Python objects including modules, functions, classes, and keywords.
print(help(ascii))


# WHAT IS VARIABLES?

# VARIABLES     These are containers for storing and labeling data, values or information.
#               It has a name and value connected to each other with the equal sign.
#               It can store different data types.

# Python has no command for declaring a variable.
# It means you don't need to declare the data types to a variable.
# A variable is created the moment you first assign a value to it.
# It has a specific name that use to assign a values inside of it.
# Remember, you cannot combine string and integer at the same time.

# Use the + operator to concatenate or combine two strings or values together.

character_shape = "triangle"
shape_sides = "three"
character_fact = "real"

print("This shape is called " + character_shape + ".")
print("It has " + shape_sides + " sides.")
print("Everywhere in this " + character_fact + " world has a triangle shape such as pyramid.\n")
# Use f-string instead of this because they are readable, easier to write and less prone to errors.

# You can also assign the same value to multiple variables in one line like this:
x = y = z = "Virtual World"
print(x, y, z)
print(y)
print(z, "\n")

# Or this which returns as tuple:
x = y = z = "Virtual World", "Real World", "No World"
print(x)
print(y)
print(z, "\n")


# type()        This function can be applied to get the data type of variable or any object.

x = 3
y = "Triangle"

print(type(x))
print(type(y), "\n")


# TYPE CONVERSION (CASTING)

# If you want to specify the data type of a variable or convert into another type, this can be done with CASTING.

x = str(3)
y = int(5)
z = float(7)

print(x, y, z, "\n")

# If you want to access the value stored in variable, call the variable name.


# RULES FOR PYTHON VARIABLES

# 1. Variable names are case-sensitive.
# 2. A variable name must start with a letter or the underscore character.
# 3. A variable name cannot start with a number.
# 4. A variable name can only contain alphanumeric characters and underscores (A-z, 0-9, and _ ).
# 5. A variable name cannot be any of the Python functions or keywords.


# MULTI_WORDS VARIABLE NAMES

# Camel Case    - Each word, except the first, starts with a capital letter:
myVariableName = "Joshua"

# Pascal Case   - Each word starts with a capital letter:
MyVariableName = "Joshua"

# Snake Case    - Each word is separated by an underscore character:
my_variable_name = "Joshua"

# Constants     - These are variables whose values are intended to remain unchanged throughout a program. 
#               - They are typically defined using uppercase letters to signify their fixed nature, often with words separated by underscores.
MAX_CONNECTIONS = 1000
TIMEOUT = 15
