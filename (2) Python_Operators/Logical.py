
# LOGICAL OPERATORS

# These are used to check if two or more conditional statements are True or False.

# AND function returns True if both statements or conditions are true.
# true and true = true
# false and true = false
# false and false = false

# OR function returns True if one of the statements or condition is true.
# true or true = true
# false or true = true
# false or false = false

# NOT function reverse the result, returns False if the result is true.


# CONDITIONAL STATEMENTS (SELECTION)

# Conditional statements, or if-else statements, allow programs to perform different actions based on the conditions.
# Having a conditional statements helps us to make a better decision and control the flow of execution in a program.

# The colon : is used to indicate the start of the function block

# 1. if statement       - A function where certain conditions considered as true.
#                       - Without else or elif, the output will not execute and will return nothing if the first condition is false.

# 2. elif statement     - A function when there is multiple conditions as an alternative or none of the first condition is True.

# 3. else statement     - A function where certain conditions becomes otherwise or false.


Present_Box = True
Is_Brown = False

if Present_Box and Is_Brown:
    print("You have brown box.")
    
elif Present_Box and not Is_Brown:
    print("Your box is not brown.")

elif not Present_Box and Is_Brown:
    print("Undefined") 

else:
    print("You don't have brown box.")


# There's also a times where else statement is not needed.

# if statements cannot be empty, but if you for some reason have an if statement with no content, 
# put in the pass statement to avoid getting an error.

a, b = 33, 200

if b > a:
  pass