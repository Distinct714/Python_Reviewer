# INTRODUCTION TO HANDLING ERRORS

# Error is a code that violate one or more rules and cause our program to terminate.
# Programs stop working when the code contain errors.

# Try & Except block will allow the program to try out piece of code.

# The try block lets you test a block of code for errors. The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.
# This can be useful to close objects and clean up resources.

# SAMPLE
def snake_case(text):
  # Check the data type
  if isinstance(text, str):
    clean_text = text.replace(" ", "_")
    clean_text = clean_text.lower()
  else:
    # Return a TypeError error if the wrong data type was used
     raise TypeError("The snake_case() function expects a string as an argument, please check the data type provided.")
  
snake_case("User Name 187")


# Since the try block raises an error, the except block will be executed.
# Without the try-except function, the program will crash and raise an error.

# Bugs are mistakes that may interrupt execution but can cause incorrect behavior.
# It often caused by logical errors which can leads to unexpected results.

# Exceptions are specific errors that occur during execution and disrupt the program's flow.
try:
   a = 5 + "15"
   print(a)
except Exception as e:
   print(e)
  
finally:
  print("Nothing goes wrong!")
  
# raise keyword is used to throw (or raise) an exception if a condition occurs.
# This will produce error and avoid executing subsequent code.
# When a method encounters an exception and does not know how to handle it, use raise exceptions

# Assert statement can be used instead of if-else statement as short ones.
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero.")

# or:
x = -10

assert(x <= 0), "No numbers below zero."
