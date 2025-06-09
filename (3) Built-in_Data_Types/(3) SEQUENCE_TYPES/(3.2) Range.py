
# RANGE

# The range() function returns a sequence of numbers starting from 0 (index) by default, 
# and increments or add by 1 (by default), and stops before a specified number.
# Its function only accept positive integer.

# Inside the range where we give a specified number to return a sequence is called argument.
num = range(5)
print(num)

# Note that range(7) is not the values of 0 to 7, but the values 0 to 6.
for i in range(7):
     print(i)

# Adding values in empty list
nums = []
# This is gonna start at 1, not zero. Range is different from index or slicing syntax.
for x in range(1, 21):
     nums.append(x)

print(nums)

# Syntax: range(start, end, step) - step is index
for i in range(1, 10, 3):
     print(i)
     if i == 4:
          break

# Converting range into list:
nums2 = list(range(0, 100))
print(nums2)

