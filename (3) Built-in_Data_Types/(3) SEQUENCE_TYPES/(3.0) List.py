
# LIST

# List are ordered, mutable and iterable collection of elements. It allows duplicate values.
# It can be stored different data types.
# Inside the square brackets contain the elements separated by a comma.

# However, strings in variables are immutable and cannot modified it just like below.

# color = "red"
# color[0] = "m"


# A list function is where you store and organize multiple values in a single variable in orderly.

# The sample below will print an empty list.
my_list = list()
print(my_list, "\n")


# In list, an arrays are used to store multiple values in one single variable.
# It is a special variable, which can hold more than one value at a time.
# However not all arrays need similar data types.

# SAMPLE OUTPUT
list_one = [4] * 5
list_two = [1, 3, 5, 7, 9]

# Concatenating lists which are similar to extend function.
def list_FirstValues():
    global list_one, list_two
    combined_list = list_one + list_two
    print(combined_list, "\n")
list_FirstValues()

# Separating two sets of list using comma.
def list_SecondValues():
    global list_one, list_two
    combined_list = list_one, list_two
    print(combined_list, "\n")
list_SecondValues()

# The difference between these two functions are the concatenation operator and comma.


# PYTHON COMPREHENSION

# List Comprehension are useful shorthands for such operations using a single line of statement.
# They are created using squared brackets.

color = ["Red", "Orange", "Yellow"]
new_color = [x.lower() for x in color]
print(new_color, "\n")

# Using i*i as expression and "for" loop over the list in one line of statement. This is called comprehension.
# Don't forget to include square brackets when there's an expression inside the function.

def iteration():
    global list_two
    x = [i*i for i in list_two]
    print(x, "\n")
iteration()

# You can also add a conditional statements here.

# This offers a shorter syntax when you want to create a new list based on the values of an existing list.
# newlist = [expression for item in iterable if condition == True]

color7 = ["Red", "Orange", "Yellow", "Green", "Blue", "Black"]
color_comprehension = [x if x != "black" else "gray" for x in color7]
print(color_comprehension, "\n")

# Squared Brackets can be used to access certain element (indexing) or add new elements in a list.

# To change the value of a specific item, refer to the index number
color = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo"]
color[4] = "Violet"

print(color, "\n")


# 11 LIST METHODS

# extend method adds the specified list elements (or any iterable) to the end of the current list.

numbers = [2, 4, 6, 8, 10]
color = ["Red", "Orange", "Yellow", "Green", "Blue"]

numbers.extend(color)
print(numbers, "\n")


# append method adds an element to the end of a list.

numbers = [2, 4, 6, 8, 10]
color = ["Red", "Orange", "Yellow", "Green", "Blue"]

color.append("Violet")
print(color, "\n")


# insert method adds new element with a specific position or index. (left of specified index)

color = ["Red", "Orange", "Yellow", "Green", "Blue"]

color.insert(1, "Pink")
print(color, "\n")


# remove method removes a specified value or element inside of a list.

color = ["Red", "Orange", "Yellow", "Green", "Blue"]

color.remove("Yellow")
print(color, "\n")


# clear method resets the whole list to get rid everything. It means removing all the elements inside the list.

numbers = [2, 4, 6, 8, 10]

numbers.clear()
print(numbers, "\n")


# pop method removes or pops an element off of the list.

color = ["Red", "Orange", "Yellow", "Green", "Blue"]

color.pop(2)
print(color, "\n")


# index method tells if the value is present inside a variable. The output will show the position of an element.

color = ["Red", "Orange", "Yellow", "Green", "Blue"]

print(color.index("Blue"), "\n")


# count method tell how many same values or not are present inside of a list.

color = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet", "Orange", "Brown", "Black", "Blue"]

print(color.count("Blue"), "\n")


# sort method arrange the values or elements either in ascending or alphabetical order.

color = ["Red", "Orange", "Yellow", "Green", "Blue"]

color.sort()
print(color, "\n")


# reverse method reverse the order of a list. (Descending)

numbers = [2, 4, 6, 8, 10]

numbers.reverse()
print(numbers, "\n")

# del keyword is used to delete objects. 
# In Python everything is an object, so the del keyword can also be used to delete variables, lists, or parts of a list etc.
del numbers[2]
print(numbers, "\n")


# copy method allows to copy the exact things or value presented in a list you've created.

color = ["Red", "Orange", "Yellow", "Green", "Blue"]
color2 = color.copy()

print(color2, "\n")

# You can also apply any python functions such as conditional statements, loops and so on.
