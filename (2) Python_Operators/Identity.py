# IDENTITY OPERATORS

# These operators compare the memory addresses of objects.

# "is" operator returns True if both variables are equal or same.
# It is also tests for object identity.

# "is not" operator returns True if both variables are not equal or same object.

x = ["Joshua", "Sean"]
y = ["Joshua", "Sean"]
z = x

# Even though x and y variable store the same elements or items, the memory address of objects is different and will return False.
print(x is y)
print(x is z)
print(y is not z)
