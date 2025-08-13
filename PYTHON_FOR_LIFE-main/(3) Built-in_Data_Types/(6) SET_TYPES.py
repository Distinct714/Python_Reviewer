# SET TYPES

# A set is a collection that store multiple items in a single variable which is unordered, 
# unchangeable, unindexed and doesn't allow duplicate elements or values.
# Sets are written with curly brackets. This doesn't support indexing or slicing.
name = {"Josh","Seph","Sean","Gerald"}
print(name)

# This is unordered collection of UNIQUE elements, meaning it cannot contain any duplicate items. 
# When you assign elements to a set, Python automatically removes any duplicates. 
numbers = {1, 2, 3, 4, 1, 2, 5, 6, 3, 4}
print(numbers)

# This will return as empty set or set() as an output.
empty = set()
print(empty)

# The output below will separate each characters and return as a set.
word = set("Python")
print(word)


# SET METHODS

# .copy is a method that copy all the elements of a set in unordered.
name = {"Josh","Seph","Sean","Gerald"}
print(name.copy())

# .clear is a method that removes all elements and returns None.
name2 = name.clear()
print(name2)

# .add is a method that adds element to the set.
add_numbers = set()
print(add_numbers)

add_numbers.add(5)
add_numbers.add(10)
add_numbers.add(15)

# .discard is a method that removes the specified element or item in a set.
# If the element is not available in a set, this will not raise an error unlike .remove function in list and tuple.
add_numbers.discard(10)
print(add_numbers)

# .pop() is a method of removing a certain element inside of set.
second_numbers = {1, 2, 3, 4}
print(second_numbers.pop())


# SETS SIMILAR IN MATHEMATICS

# Several Ways to Join Two or More Sets in Python:

odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8}
primes = {2, 3, 5, 7}

# .union is a method that combines all elements from both two sets without duplication.
u = odds.union(evens)
print(u)

# .intersection is a method that returns or keeps ONLY the duplicates in both sets.
# It will return a new set that only contains the items that are present in both sets.
i = odds.intersection(primes)
print(i)


setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

# .difference is a method that removes similar elements and returns the first assigned set.
d = setB.difference(setA)
print(d)

# .symmetric_difference is a method that returns a set that contains all items from both set, but not the items that are present in both sets.
# It means all duplicate elements in both sets are not included as an output.
diff = setA.symmetric_difference(setB)
print(diff)


# .update is a method that update the set with the union of this set and others.
setC = {1, 2, 3, 7, 8, 9}
setD = {1, 2, 3}
setE = {4, 5, 6}

setC.update(setD)
print(setC)

# .issubset returns True if all items in the set exists in the specified set, otherwise it returns False. (sub)
subset = setD.issubset(setC)
print(subset)

# .issuperset returns True if all items in the specified set exists in the original set, otherwise it returns False. (all)
# It returns whether this set contains another set or not
subset2 = setD.issuperset(setC)
print(subset2)

# .isdisjoint checks whether two sets have any similar or common elements.  
# If no common elements exist, it returns True ; otherwise, it returns False.
subset2 = setE.isdisjoint(setD)
print(subset2)


# OPERATORS FOR JOINING TWO OR MORE SETS

set1 = {1, 3, 5}
set2 = {1, 2, 3}
set3 = {"pen", "eraser"}
set4 = {"pencil", "ballpen", "pen"}

# | operator is for union (vertical bar)
myset1 = set1 | set2 | set3 |set4
print(myset1)

# & operator is for intersection (ampersand)
myset2 = set1 & set2
print(myset2)

# - operator is for difference (minus sign)
myset3 = set3 - set4
print(myset3)

# ^ operator is for symmetric_difference (caret or raise sign)
myset4 = set1 ^ set2
print(myset4)

# All of these operators only allows you to join sets with sets, and not with other data types like you can with the other methods.


# FROZENSET

# The different of frozen set to normal set is the combination of parenthesis and curly brackets.
# Frozenset is a immutable version of a normal set.
# It means you cannot do the above method as this will run as error.

name3 = frozenset({"Josh","Seph","Sean","Gerald"})
print(name3)
