# PYTHON MODULES

# A module considered to be the same as a code library. (Single Python File)
# It is a Python Script, meaning a file contains a set of functions or attributes you want to include in your application.

# When using a function from a module, create the variable name first then follow this format: module_name.function_name.
# You can name the module file whatever you like, but it must have the file extension .py
# You can create an alias when you import a module, by using the "as" keyword

# Having a modules in our Python help us avoid writing code that is already exists.
# WARNING: Using help() will return a large output and contains a lot of information we don't need.

# BUILT-IN MODULES

# PLATFORM
import platform

x = platform.system()
print(x)

# There is a built-in function to list all the function names (or variable names) in a module, which is dir().
# The dir() function can be used on all modules, also the ones you create yourself.

import platform

x = dir(platform)
print(x)

# You can choose to import only parts from a module, by using the from keyword.
# When importing using the from keyword, do not use the module name when referring to elements in the module. 
# The correct format is person1["age"], not mymodule.person1["age"]

# OS

# os is a popular module used for interpreting and interacting with your operating system.

import os

#
print(type(os))

# The chdir() is used to change directory
print(os.chdir(""))

# The getcwd() retrieves the current working directory
print(os.getcwd())

# The environ is an attribute used to get the information about our local environment
print(os.environ)

# Importing a whole module can require a lot of memory
# This will reduced by importing a specific function or attributes from the module using this format. [ from module import any]
# No need to input the name of module here.