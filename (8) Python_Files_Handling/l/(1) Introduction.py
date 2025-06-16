# FILE HANDLING

# File handling is an important part of any web application.
# Python has several functions for creating, reading, updating, and deleting files.

# open() is a special function that allows to open a certain files, and the key function for working with files in Python.
# The open() function takes two parameters; filename, and mode.
# The file must be in the same directory. Make sure the file exists, or else you will get an error.

# The open() function returns a file object, which has a read() method for reading the content of the file.


# FOUR DIFFERENT METHODS OR MODES FOR OPENING A FILE:

# 1. "r" (read)     A mode that allows to read information inside the file.
#                   It returns error if the file does not exist.

# 2. "w" (write)    Another mode that allows to change or modified existing information.
#                   It opens a file for writing, creates the file if it does not exist.

# 3. "a" (append)   It allows you to append information onto the end of a file.
#                   Opens a file for appending, creates the file if it does not exist.
#                   This means you can't modify any information inside the file.

# 4. "x" (create)   Creates the specified file, returns an error if the file exists.


# close() is a function that allows to close the file and no longer be able to access the file.
# It is a good practice to always close the file when you are done with it
# You should always close your files. In some cases, due to buffering, changes made to a file may not show until you close the file.

# You can return one line by using the readline() method

content = open("C:/Users/Joshua/OneDrive/Documents/Programming Languages/PYTHON/LESSONS/(8) Python_Files_Handling/l/sample.txt", "a")
content.write("Now the file has no more content!\n")
content.close()

content = open("C:/Users/Joshua/OneDrive/Documents/Programming Languages/PYTHON/LESSONS/(8) Python_Files_Handling/l/sample.txt", "r")
print(content.read())

# "r+" is basically means read and write.


# To delete a file, you must import the OS module, and run its os.remove() function.
# To delete an entire folder, use the os.rmdir() method.
# You can only remove empty folders.

import os
os.remove("C:/Users/Joshua/OneDrive/Documents/Programming Languages/PYTHON/LESSONS/(8) Python_Files_Handling/l/sample.txt")


# In addition you can specify if the file should be handled as binary or text mode:

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

# search here
with open("") as f:
    print(file=f)

# Explore more about here
