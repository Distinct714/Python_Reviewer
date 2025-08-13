# ORDERED DICTIONARY

# This is similar to regular dictionary, but they remembered the order that the items were inserted or created.

from collections import OrderedDict

shapes = OrderedDict()

# Inside the square brackets are the keys with assigned values.
shapes["Triangle"] = 3
shapes["Square"] = 4
shapes["Heptagon"] = 5
shapes["Hexagon"] = 6

print(shapes)