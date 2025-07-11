# PYTHON ITERATOR

# An iterator is an object that contains a countable number of values.
# It is an object that can be iterated upon, meaning that you can traverse through all the values.

# iter() is a method used to create iterator to an iterable objects.
name = ['jay garrick', 'barry allen', 'wally west', 'bart allen']
iteration = iter(name)

# next() is a method used to produce next values.
print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))

# There are four collection data types in the Python programming language:

# 1. List is a collection which is ordered and changeable. Allows duplicate members.

# 2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# 3. Set is a collection which is unordered, unchangeable, and unindexed. No duplicate members.

# 4. Dictionary is a collection which is ordered and changeable. No duplicate members.


# Lists, tuples, dictionaries, and sets are all iterable objects. 
# They are iterable containers which you can get an iterator from.
# Even strings are iterable objects, and can return an iterator.

# Create an iterator for range(3): small_value
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))

# Loop over range(3) and print the values

for num in range(3):
    print(num)

# Create an iterator for range(10 ** 100): googol
googol = iter(range(10**100))

# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
