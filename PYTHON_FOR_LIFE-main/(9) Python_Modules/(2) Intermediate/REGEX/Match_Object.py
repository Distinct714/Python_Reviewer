# A Match Object is an object containing information about the search and the result.
# If there is no match, the value None will be returned, instead of the Match Object.

# The Match object has properties and methods used to retrieve information about the search, and the result:

# .span() returns a tuple containing the start-, and end positions of the match.
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

# .string returns the string passed into the function
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

# .group() returns the part of the string where there was a match
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())