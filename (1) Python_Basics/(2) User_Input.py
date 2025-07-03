# GETTING INPUT FROM USER

# input()    This function ask or allow the users to type or input their data or information into the program.
#            Input function automatically convert into string. 
#            If you want to modify the variables into other data types, you can convert into integer, or float. This is called casting.

# SAMPLE ONE
name = input("Enter your Name: ")
print(f"Hello, {name}!")

age = int(input("Enter Your Age: "))
asking = input(f"Are you {age} years old?")

if age >= 18:
    if asking == "Yes" or "yes":
        print("Then, get some work!\n")
    else:
        print("Then, study now!\n")
else:
    print("Repeat the fill-up.\n")


# SAMPLE TWO
prompt = "Your data won\'t be stolen.\n"
prompt += "Enter your username: "
username = input(prompt)
print(f"Hello, {username}.")


# (F-STRING) Formatting String

# F-string      This is a preferred way of formatting strings and allows you to format selected parts of a string.
#               Note, we cannot combine strings and numbers in a variables. Instead, use f-string and {variable} like this:

name = "Joshua" # String
age = 19        # Integer

print(f"My name is {name}")
print(f"I am {age} years old")

# Inside the curly brackets {} is a placeholders for variables and other operations to format the value.

# Placeholder   This can contain variables, operations, functions, and modifiers to format the value.
#               It can be identified using named indexes {variable}, numbered indexes {0}, or even empty placeholders {}.

# Modifier      This is included by adding a colon : followed by a legal formatting type, like .2f, .3f and so on
#               which means fixed point number with 2 or more decimals like this:

name = "Joshua" # String
age = 19        # Integer

print(f"My name is {name}")
print(f"I am {age:.2f} years old")

# Explore more about formatting types in string_format.
