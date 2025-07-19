# PYTHON DECORATORS

# Decorators are powerful feature in Python that allow you to modify the behavior of functions or classes without changing
# their source code directly or altering its original code.

def greet():
    return "Welcome!"

# takes the first function as an argument while defining 2nd function below
# Acts as a decorator
def uppercase():
    # Represent modified version of greet() function.
    def wrapper():
        orig_message = greet()
        modified_message = orig_message.upper()
        return modified_message
    return wrapper

greet_upper = uppercase(greet)
print(greet_upper())

# You can apply a decorator to a function using the @ sign.
# It improves the code readability and provides a clean separation between the function and its decoration.

def uppercase():
    def wrapper():
        orig_message = greet()
        modified_message = orig_message.upper()
        return modified_message
    return wrapper

@uppercase
def greet():
    return "Welcome!"

print(greet())

# The second sample is recommended.
