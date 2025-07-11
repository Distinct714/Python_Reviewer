# SLICING SYNTAX

# Index operator [] refers to the process of accessing a specific element in a sequence, such as a string or list, 
# using its position or index number. 

# Remember range and index is different from each other. Watch out their parenthesis and squared brackets.

# In negative indexing, it always start at -1 in the end of an item or element.
shape = "Rectangle" 
print(shape[1])
print(shape[-5], "\n")


# Slicing allows you to select specified characters or subset of a lst and extract it in a sequence.
# syntax [start:end:step] - start index (inclusive), end index (exclusive) and step size (optional).
color1 = [
    "Red", 
    "Orange", 
    "Yellow", 
    "Green", 
    "Blue"
]

slice = slice(1, 3)
print(color1[slice], "\n")

# Remember, the index of 1 in [1:3] start at 0 while 3 start on normal sequence not including 0.
# This means that the first item or element has index 0.

# When slicing, you can omit either the starting index or stopping index in both list and string.
color2 = ["Red", "Orange", "Yellow", "Green", "Blue"]
print(color2[:2], "\n")   # omitting starting index
print(color2[1:], "\n")   # omitting stopping index

# Search here
color_guy = "VioletGuy"

print(color_guy[::3])          # Counting index in by 3
print(color_guy[5::])          # Eliminate the first character based on slicing position.
print(color_guy[::-1], "\n")   # Reverse string

color5 = "Violet is a dark color."
print(color5[1:20:3], "\n")

# You can also combined both positive and negative indexing when applying slice syntax.
# Remember, all step index in the end of an elements automatically removes it when this was applied.
numbers = [100,200, 300, 400, 500]
print(numbers[1:-1], "\n")

# CHANGE ITEM VALUE
color7 = ["Red", "Orange", "Yellow", "Green", "Blue"]
color7[1:3] = ["Pink", "Gold"]
print(color7, "\n")



