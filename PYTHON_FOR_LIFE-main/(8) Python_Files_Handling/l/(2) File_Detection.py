
# FILE DETECTION

import os

path_file = input("Enter a Path File here: ")

if os.path.exists(path_file):
    print("The file you've entered already exists.")
    if os.path.isfile(path_file):
        print("This is a file.")
    elif os.path.isdir():
        print("This is a directory.")
else:
    print("The file you've entered does not exists.")