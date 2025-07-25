# BOOLEAN TYPE

# Booleans represent one of two values: True or False.
# It can also applied to comparison and conditional statements.

# Almost any value is evaluated to True if it has some sort of content.
# Any string and number present is True. Any list, tuple, set, and dictionary present are also True.
# In other words, every empty values, such as (), [], {}, "", the number 0, and the value None result False.

# The bool() function allows you to identify any value, and give you True or False in return.
comparison_num = 5 < 4
print(bool(comparison_num))

# Another Sample
a = True
b = False
print(bool(a and b))

# Python also has many built-in functions that return a boolean value, like the isinstance() function, 
# which can be used to determine if an object is of a certain data type. (variable, data types)
x = 200
print(isinstance(x, int))
