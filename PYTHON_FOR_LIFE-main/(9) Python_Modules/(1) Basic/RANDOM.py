# RANDOM MODULE

# Python does not have a random() function to make a random number, 
# but Python has a built-in module called random that can be used to make random numbers.

import random

# randrange is a method returns a randomly selected element from the specified range.
print(random.randrange(1, 20))

# randint is a method returns an integer number selected element from the specified range.
nums = random.randint(1, 10)
print(nums)

# choice is a method returns a randomly selected element from the specified sequence.
# The sequence can be a string, a range, a list, a tuple or any other kind of sequence.
x = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"]
choice = random.choice(x)
print(choice)

# shuffle  is a method takes a sequence, like a list, and reorganize the order of the items. (Shaking Dice and roll)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(numbers)
print(numbers)

# random is a method that eturns a random float number between 0 and 1.
num = random.random()
print(num)

