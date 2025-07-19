# FUNCTIONS

# Functions is a collection or block of codes that perform a specific tasks, which only runs when it is called.
# It is defined using the def keyword followed by a function name and parenthesis.
# Outside of the def function without indentation no longer inside its function.

# Take note that using special characters such as ! $ etc. as variable or value will affect the other function of codes.

# PURPOSE OF USING FUNCTION:
# 1. Code Reusability - Write once, use multiple times.
# 2. Modularity - Break complex code into smaller, manageable parts.
# 3. Better Readability - Makes code easier to understand.
# 4. Easier Debugging - Fixing errors in one function is easier than fixing them in multiple places.

def HelloUser():
    print("Hello, User")
HelloUser()
HelloUser()
HelloUser()

# SCOPE

# A variable is only available from inside the region it is created. This is called scope.

# Variables that are created outside of a def function are known as global variables.
# To create global variable inside a function, you can use the "global" keyword.
# Global variables are available from within any scope, global and local.

# If you create a variable with the same name inside a function, this variable will be local, and 
# can only be used inside the function. 
# The global variable with the same name will remain as global and with the original value.
greeting = "Hello, User"

def greet():
    global greeting
    greeting = "Hello, Joshua"
greet()

print(greeting)

# The nonlocal keyword is used to work with variables inside nested functions.
# This makes the variable belong to the outer function.
def hi():
  x = "User"
  def hi2():
    nonlocal x
    x = "Hello" # This will be the output.
  hi2()
  return x

print(hi())

# Parameters is a piece of information we give to function.
# It is the variables listed inside the parentheses in the function beside function name. (Variables)

# Inside the parenthesis of a function caller is called arguments.
# An argument is the assigned value in a parameters that is sent to the function when it is called. (Values)
# They are specified after the function name, inside the parentheses. 
# You can add as many arguments as you want, just separate them with a comma.


# SAMPLE 1
def HelloUser(name, age, job):
    print(f"Hello, {name}, You are now {age}, You want {job}")

HelloUser("Joshua.", "19.", "IT Manager.")

# SAMPLE 2
def numbers(a, b=5):
    return a * b
numbers(4)

# This shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:
def HelloUser(name = "Joseph"):
    print(f"Hello, {name}")

HelloUser("Gerald")
HelloUser() # This one
HelloUser("Joshua")

# You can send any data types of argument to a function (string, number, list, dictionary etc.), and 
# it will be treated as the same data type inside the function.

# The return function allows to return the value back to the caller of function.
def value(num):
    return num * num * num
print(value(2))

# Function definitions cannot be empty, but if you for some reason have a function definition with no content, 
# put in the pass statement to avoid getting an error.
def nothing():
    pass


# Higher-Order Functions is a functions that operate other functions that take another function as an argument or return a function

# Functions can take other functions as arguments.
def welcome(food):
    return f"Welcome, {food}"

def process_food(food, func):
    return func(food)

print(process_food("Bread", welcome))


# TWO TYPES OF ARGUMENTS:

# POSITIONAL ARGUMENT - The argument should align to the parameter or provide arguments in order, separated by a commas.
#                     - This requires less code to execute function and keep a consistent order to arguments

# KEYWORD-ONLY ARGUMENT - This provide arguments by assigning values to keywords.
#                       - This improves interpretation and easy to keep track of which argument you use.


# COLLECTIONS USING FUNCTION
def convert_data_structure(data, data_type = "list"):
  if data_type == "tuple":
    data = tuple(data)
  elif data_type == "set":
    data = set(data)
  else:
    data = list(data)
  return data

x = convert_data_structure({"a", 1, "b", 2, "c", 3}, data_type="list")
print(x)
