

# Arbitrary arguments allow functions to accept any number of arguments

# ARBITRARY POSITIONAL ARGUMENTS

# *args allows you to provide any number of arguments without the need to create a list before calling the function each time.
# If you do not know how many arguments that will be passed into your function, add * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly.
# This operator informs Python that the argument is an iterable and should be unpacked to receive its values as individual arguments.

# Similar to previous lesson, the * asterik operator is used to gather multiple elements or values where one variable holds a list.
# It means combining all positional arguments and converting these arguments to a single iterable. (tuple)

# If the number of variables is less than the number of values in tuple, you can add * to the variable name and each elements or values 
# will be assigned to the variable as a list or specified element only.
# The output in a variable with asterisk in values will turn to list with brackets.


# SAMPLE 1
def my_food(*foods):
  print(f"{foods[2]} tastes good.")

my_food("Cake", "Bread", "Doughnut")

# SAMPLE 2
def total(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print(total(1, 2, 3, 4, 5))


# Define a function called concat
def concat(*args):
  
  # Create an empty string
  result = ""
  
  # Iterate over the Python args tuple
  for arg in args:
    result += " " + arg
  return result

# Call the function
print(concat("Python", "is", "great!"))


# ARBITRARY KEYWORD ARGUMENTS

# **kwargs is used to unpack dictionaries into arguments and receives arguments in the form of dictionary.
# If you do not know how many keyword arguments that will be passed into your function, 
# add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly

# You can also send arguments with the key = value syntax.
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

display_info(name = "Joshua", age = "20", country = "Philippines")


# Define a function called concat
def concat(**kwargs):
  
  # Create an empty string
  result = ""
  
  # Iterate over the Python kwargs
  for kwarg in kwargs.values():
    result += " " + kwarg
  return result

# Call the function
print(concat(start="Python", middle="is", end="great!"))    