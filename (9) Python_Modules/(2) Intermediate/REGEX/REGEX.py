# REGEX MODULE

# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

# findall is a function that returns a list containing all matches.
# The list contains the matches in the order they are found.
# If no matches are found, an empty list is returned:
import re

text = "The rain in Spain"
w = re.findall("ai", text)
print(w)

# search is a function that searches the string for a match and returns a Match object if there is a match anywhere in the string.
# If there is more than one match, only the first occurrence of the match will be returned.
# If no matches are found, the value None is returned
text2 = "The rain in Spain"
x = re.search("\s", text2)
print("The first white-space character is located in position:", x.start())


# split is a function that returns a list where the string has been split at each match.
# You can control the number of occurrences by specifying the maxsplit parameter
text3 = "The rain in Spain"
y = re.split("\s", text3, 1)
print(y)

# sub is a function that replaces one or many matches with a string or text of your choice.
# You can control the number of replacements by specifying the count parameter
text4 = "The rain in Spain"
z = re.sub("\s", "9", text4, 2)
print(z)


# RegEx Functions

txt = "No. 1: Raining in Manila"

# []	A set of characters
#Find all upper case characters alphabetically between "a" and "m":
a = re.findall("[A-Z]", txt)
print(a)


# \	    Signals a special sequence which can also be used to escape special characters
b = re.findall("\d", txt)
print(b)

# .	    Any character except newline character
c = re.findall("M....a", txt)
print(c)


# ^	    Starts with
d = re.findall("^hello", txt)
if d:
  print("Present")
else:
  print("Not Present")


# $	    Ends with
d = re.findall("Manila$", txt)
if d:
  print("Present")
else:
  print("Not Present")


# *	    Zero or more occurrences
e = re.findall("he.*o", txt)
print(e)


# +	    One or more occurrences
f = re.findall("R.+g", txt)
print(f)


# ?	    Zero or one occurrences
g = re.findall("R.?g", txt)
print(g)


# {}	Exactly the specified number of occurrences
h = re.findall("M.{2}a", txt)
print(h)


# |	    Either or
i = re.findall("Manila|Laguna", txt)
print(i)

if i:
  print("Yes, there is at least one match!")
else:
  print("No match")


# ()	Capture and group


# Special Sequences

# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
# \b	Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"

# r"ain\b"	

# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"

# r"ain\B"	

# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
# \D	Returns a match where the string DOES NOT contain digits	"\D"	
# \s	Returns a match where the string contains a white space character	"\s"	
# \S	Returns a match where the string DOES NOT contain a white space character	"\S"	
# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
# \W	Returns a match where the string DOES NOT contain any word characters	"\W"	
# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"


# A SET is a set of characters inside a pair of square brackets [] with a special meaning

# [arn]	Returns a match where one of the specified characters (a, r, or n) is present	
# [a-n]	Returns a match for any lower case character, alphabetically between a and n	
# [^arn]	Returns a match for any character EXCEPT a, r, and n	
# [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
# [0-9]	Returns a match for any digit between 0 and 9	
# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
# [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
# [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

