# LAMBDA

# A lambda function is a small anonymous function that is defined without a name. 
# It can take any number of arguments, but can only have one expression.
# This function is shorter and only in one line.
# The argument is located before the expression. (lambda arguments: expression)
# Use lambda functions when an anonymous function is required for a short period of time.

# Addition with Lambda
add = lambda nums : nums + 10
print(add(5))      # nums = 5

# This function will perform the same as shown above, but it's defined without a name.
def add_func(nums):
    return nums + 10
add_func(10)

# Multiple Arguments in Lambda
compute = (lambda x, y, z: x * y * z)
compute(5, 10, 15)

# SAMPLE
sale_price = 29.99

# Define a lambda function called add_tax
add_tax = lambda x: x * 1.2

# Call the lambda function
print(add_tax(sale_price))

print((lambda x: x * 1.2)(sale_price))


# sorted() function returns a sorted list of the specified iterable object.
# You can specify in either ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.
# However, you cannot sort a list that contains BOTH string values AND numeric values.
numbers = [(5, 8), (10,-1), (30, -20),(25, 15)]

arrange_nums = sorted(numbers)
print(arrange_nums)


# Sorting with specified index using lambda with key function. 
# In tuple, the first set of elements are counted as o and 1 index since it has two elements inside the tuple. 
# Same in other sets of elements.
arrange_nums2 = sorted(numbers, key = lambda x: x[1])
print(arrange_nums2)

# This function will return the same result, but it's defined without a name.
def arrange(x):
    return x[1]

# Sorting tuple in descending order using reverse:
arrange_nums3 = sorted(numbers, reverse = True, key = lambda x: x[0])
print(arrange_nums3)

# map() function executes a specified function for each element in an iterable like list, tuple, etc.
# The item is sent to the function as a parameter. map(func, seq)

sales_prices = [29.99, 9.95, 14.50, 39.75, 60.00]

# Create add_taxes to add 20% to each item in sales_prices
add_taxes = map(lambda x: x * 1.20, sales_prices)

# Use add_taxes to return a new list with updated values
print(list(add_taxes))

# Convert the map into a list, for readability:
list_numbers = [1, 3, 5, 7, 9]
result = map(lambda x: x*2, list_numbers)
print(list(result))

# However, this is not recommended, use the simple syntax as shown below:
z = [x*3 for x in list_numbers]
print(z)

# filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.
# filter(function, iterable)
list_nums = [11, 14, 17, 20, 23]
result2 = filter(lambda y: y % 2 == 0, list_nums)
print(list(result2))

# reduce()

# zip
