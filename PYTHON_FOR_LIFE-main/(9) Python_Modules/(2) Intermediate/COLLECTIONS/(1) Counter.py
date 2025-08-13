# COLLECTIONS

# This module implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers, 
# dict, list, set, and tuple. This offers a variety of advanced sdata structure.

# Counter is a containers that stores the elements as dictionary keys and their counts as dictionary keys.

from collections import Counter

# The output counts the same character from highest to lowest values. Watch out for the letter case!
numbers = "Philippines"
my_numbers = Counter(numbers)
print(my_numbers)

# This counts all similar keys and puts as value in dictionary which arranged in order.
print(my_numbers.items())

# In output, this removes duplicate keys and display all keys.
print(my_numbers.keys())

# This displays the values only based on the arrangement of given keys.
print(my_numbers.values())

# This displays the highest values depending on the assigned index.
print(my_numbers.most_common(2))

# Print out all present keys including the duplicates.
print(list(my_numbers.elements()))

