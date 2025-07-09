# STRING FORMATS

# The format() method formats the specified value(s) and insert them inside the string's placeholder.
# The format() method returns the formatted string. Syntax: string.format(value1, value2...)

# The placeholder is defined using colon : and curly brackets {} without the f-string.
# The placeholders can be identified using named indexes {argument}, numbered indexes {0}, or even empty placeholders {}.

name, age = "Joshua", "20"

# Empty Placeholder
print("My name is {} and I am {} years old.".format(name, age))

# Positional Argument (Index)
print("My name is {1} and I am {0} years old.".format(name, age))

# Keyword Argument
print("My name is {name} and I am {age} years old.".format(name="Arish", age="18"))


# FORMATTING TYPES (OPTIONAL METHOD)

# Left aligns the result (within the available space)
txt = "We have {:<8} chickens."
print(txt.format(49))

# Right aligns the result (within the available space)
txt = "We have {:>8} chickens."
print(txt.format(49))

# Center aligns the result (within the available space)
txt = "We have {:^8} chickens."
print(txt.format(49))

# Places the sign to the left most position
txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))

# Use a plus sign to indicate if the result is positive or negative
txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))

# Use a minus sign for negative values only
txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))

# Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3, 7))

# Use a comma as a thousand separator
txt = "The universe is {:,} years old."
print(txt.format(13800000000))

# Use a underscore as a thousand separator
txt = "The universe is {:_} years old."
print(txt.format(13800000000))


# Scientific format, with a lower case e and upper case E
txt = "We have {:e} chickens."
print(txt.format(5))

txt = "We have {:E} chickens."
print(txt.format(5))

# Use "f" to convert a number into a fixed point number, default with 6 decimals, 
# but use a period followed by a number to specify the number of decimals:
txt = "The price is {:.2f} dollars."
print(txt.format(45))

txt = "The price is {:f} dollars."
print(txt.format(45))

#Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:
x = float('inf')

txt = "The price is {:F} dollars."
print(txt.format(x))

txt = "The price is {:f} dollars."
print(txt.format(x))


# Use "%" to convert the number into a percentage format:
txt = "You scored {:%}"
print(txt.format(0.25))

txt = "You scored {:.0%}"
print(txt.format(0.25))


# CONVERSION

# Binary format
txt = "The binary version of {0} is {0:b}"
print(txt.format(5))

# Decimal format
txt = "The decimal version is {:d}."
print(txt.format(0b101))

# Use "o" to convert the number into octal format:
txt = "The octal version of {0} is {0:o}"
print(txt.format(10))

# Use "x" to convert the number into Hex format:
txt = "The Hexadecimal version of {0} is {0:x}"
print(txt.format(255))

# Use "X" to convert the number into upper-case Hex format:
txt = "The Hexadecimal version of {0} is {0:X}"
print(txt.format(255))
