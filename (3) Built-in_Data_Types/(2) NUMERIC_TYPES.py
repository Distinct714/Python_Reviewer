# NUMERIC DATA TYPES


# int function      - Converts the specified or assigned value into an integer number. 
#                   - Decimal Numbers doesnt work in this kind of data type.
#                   - It can be a whole number and positive or negative, without decimals, of unlimited length.

# float function    - Convert any value into a decimal or fractional number.
#                   - It converts integers or real numbers into floating-point numbers.
#                   - It can be a number and positive or negative, containing one or more decimals.
#                   - It can also be scientific numbers with an "e" to indicate the power of 10.


# Sample Built of Basic Calculations

#Addition
print("Addition")
num1 = input("Enter a number: ")
num2 = input("Enter another number:")
result = float(num1) + float(num2)

print(str(result))

# Subtraction
print("Subtraction")
num1 = input("Enter a number: ")
num2 = input("Enter another number:")
result = float(num1) - float(num2)

print(str(result))

# Multiplication
print("Multiplication")
num1 = input("Enter a number: ")
num2 = input("Enter another number:")
result = float(num1) * float(num2)

print(str(result))

# Division
print("Division")
num1 = input("Enter a number: ")
num2 = input("Enter another number:")
result = float(num1) / float(num2)

print(str(result))


# Additionally, the complex function is mix with numeric characters and "j" to a variable.
# The j stands as imaginary part of character or number.
name = 2004j
print(name)

# You cannot convert complex numbers into another number type.
