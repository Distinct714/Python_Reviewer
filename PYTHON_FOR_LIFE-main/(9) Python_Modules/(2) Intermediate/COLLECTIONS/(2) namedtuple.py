# NAMEDTUPLE

# This is easy to create and lightweight object similar to the struct. 

from collections import namedtuple

coordinates = namedtuple("Point", "x,y")
my_coordinates = coordinates(1, 9)
print(my_coordinates)
print(my_coordinates.x, my_coordinates.y)