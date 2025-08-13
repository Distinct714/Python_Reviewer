# SYS MODULE

# .getsizeof is a function that returns the size of an object in bytes.

import sys
# object
my_list = [1, 3, 5, 7, 9]
my_tuple = ("Jollibee", "Mcdonalds", "KFC")

print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

# explore