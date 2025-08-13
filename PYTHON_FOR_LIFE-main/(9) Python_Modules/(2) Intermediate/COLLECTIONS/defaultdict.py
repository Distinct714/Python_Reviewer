# DEFAULT DICTIONARY

# This is similar to the usual dictionary, but it will have a default value if the key has not been set yet.

from collections import defaultdict

# Inside the parenthesis, you can modify it as int, float, list etc.
num = defaultdict(int)

num["a"] = 1
num["b"] = 2

# This will return the value based on the specified key.
print(num["b"])

# This will return 0 as the default value.
print(num["c"])

nums = {}
nums["c"] = 3
nums["d"] = 4

# This will run as error.
print(nums["a"])