
# DOCSTRINGS

# Docstrings is a string or a block of text used to describe what a function does.
# These are displayed along with the information when we use the help function.

# The help() displays documentation about various Python objects including modules, functions, classes, and keywords.
# It allows to access information about the function inlucding its docstring by calling help().
print(help(ascii))


# Two sets of double underscore referred to as dunder in programming 
# __doc__ is used to access the docstring only or the dunder-doc attribute to the function
round.__doc__


# Creating a docstring inside the function in single line or multiline format.
def HelloUser():
    '''
        Just A Simple Greet
    '''
    print("Hello, User")


print(help(HelloUser))


# Create the convert_data_type function
def convert_data_structure(data, data_type="list"):
  # Add a multi-line docstring
  
  """
  Convert a data structure to a list, tuple, or set.
  
  Args:
  	data (list, tuple, or set): A data structure to be converted.
    data_type (str): String representing the type of structure to convert data to.
    
  Returns:
  	data (list, tuple, or set): Converted data structure.
  """

  if data_type == "tuple":
    data = tuple(data)
  elif data_type == "set":
    data = set(data)
  else:
    data = list(data)
  return data

print(help(convert_data_structure))
