# (TEXT TYPES) STRING IS ARRAY

# String    - A piece of text data, which is a sequence of characters in quotes and immutable.
#           - Strings in python are surrounded by either single quotation marks, or double quotation marks.
#           - Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

# Strings are immutable, which means that you can’t change the characters in a string. 
# If you try to change a string, you’ll get an error.


# TEXT MANIPULATION

# If you want to modify the string variables, use .method (method refers to capitalize, upper, lower,etc.)
# .ismethod answered the true and false values in a certain variable. (Boolean Values)
# Remember to add () after the .method dot notation inside a parenthesis.


# CASE CONVERSION

phrase = "Joshua Restaurant"
print(f"{phrase.upper()} is really good")   # ---> The upper method returns the string in upper case.
print(phrase.isupper())

phrase = "Joshua Restaurant"
print(phrase.lower())                       # ---> The lower method returns the string in lower case.

phrase = "joshua restaurant now"            # ---> The title method capitalizes the first character of each word in the string.
print(phrase.title())  

phrase = "joshua restaurant now"            # ---> The capitalize method capitalizes the first character of first word in the string only.
print(phrase.capitalize())  

# Explore more beside here:
phrase = "Joshua Restaurant is the best!"
print(phrase.split())                       # ---> The split method splits the string into substrings if it finds 
                                            #      instances of the separator. (Print out as list)
phrase = " Joshua Restaurant "
print(phrase.strip())                       # ---> The strip method removes any whitespace from the beginning or the end.


# The len() length function used to return the length of each characters or items present in a variable.
# Remember the position of characters or index in a values start at 0.
phrase1 = "Joshua Restaurant is delicious"
print(len(phrase1))

# The index() is a method that identify the characters or items written in a string variable.
# It also helps to find if the certain value is present inside a variable.
phrase2 = "Joshua Restaurant is closed"
print(phrase2.index("is"))

# replace() is a method used to change or create a new values that you wish to replace a new one.
quote1: str = "Joshua Restaurant is really good"
print(quote1.replace("Joshua", "Gerald"))

# find() is a function that returns the index of the given value and checks or searches if the 
# character is present in a string. If the value is not present, it will return -1 instead.
quote2 = "Joshua Restaurant is delicious"
print(quote2.find("t"))

# join() is a function that joins the elements of an iterable using the string as a separator.
quote3 = "Joshua Restaurant is closed"
print(quote3.join("//"))

# removeprefix() function removes the prefix or the substring you want to remove from the start of the string and 
# returns the rest of the string. 
# If the prefix string is not found, then it returns the original string.
quote4 = "https//:None.com.vs"
new = quote4.removeprefix("https//:")
print(new)

# removesuffix() is a method that allows us to remove a specified suffix from a string.
new2 = quote4.removesuffix(".vs")
print(new2)
