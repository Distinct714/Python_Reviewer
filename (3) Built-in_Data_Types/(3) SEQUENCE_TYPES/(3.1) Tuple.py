
# TUPLES

# The tuple is a type of data structure similar to list but fixed data.
# It is a collection of elements that is ordered and immutable.
# It is created with a set of parenthesis.
# Additionally, this cannot be change or modified once you create a tuple to assigned a new value.

# Sometimes, working with a tuple can be more efficient and faster than a list, especially when working on large data.

# Correct Output

coordinates = [(6, 9), (3, 5), (8, 2)]

print(coordinates[0], "\n")


# Sample of Invalid Output

# coordinates = (6, 9)
# coordinates[0] = 7

# print(coordinates[0])


# Using a built-in function to create a tuple and access it, where the elements inside of tuple is under a list.

fast_foods = tuple(["Jollibee", "Mcdonalds", "KFC"])

print(fast_foods, "\n")

# Using "for" loop over the tuple in one line of statement.
for i in fast_foods: print(i)
print("\n")

# You can convert list to tuple and vice versa.


# UNPACKING - extracting a collection of values in a list, tuple etc.

world = ("Virtual World", "Real World", "No World")
x, y, z = world
print(x)
print(y)
print(z)

print("\n")


# PACKING - assigning value to a tuple

# If the number of variables is less than the number of values in tuple, you can add * to the variable name and the values 
# will be assigned to the variable as a list.
# The output in a variable with asterisk in values will turn to list with brackets.

# The * asterik operator is used to gather multiple elements where the variable holds a list.

# SAMPLE 1
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

print("\n")

# SAMPLE 2
burger_ingredients = ("White", "Grilled", "Cheddar")
(Buns, Beef, Cheese) = burger_ingredients

print(Buns, Beef, Cheese)

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x, "\n")

# Make sure the number of variables matches the number of values, or else you will get an error.

