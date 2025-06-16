# JSON MODULE

# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation, which can be used to work with JSON data.


# If you have a JSON string, you can parse (analze or interpret) it by using the json.loads() method.

import json

# some JSON string:
json_str = '{ "name":"Joshua", "age":20, "city":"Calamba"}'

# parse json_str:
parse = json.loads(json_str)

# the result is a Python dictionary:
print(parse["age"])


# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# Python object (dict):
x = {
  "name": "Joshua",
  "age": 20,
  "city": "Calamba"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


# You can convert Python objects of the following types into JSON string:

# Dictionary to Object
print(json.dumps({"name": "John", "age": 30}))

# list to Array
print(json.dumps(["apple", "bananas"]))

# tuple to Array
print(json.dumps(("apple", "bananas")))

# string to String
print(json.dumps("hello"))

# int to Number
print(json.dumps(42))

# float to Number
print(json.dumps(31.76))

# Boolean Values to true and false
print(json.dumps(True))
print(json.dumps(False))

# None to null
print(json.dumps(None))
print("\n")

# The example below prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

# The json.dumps() method has parameters to make it easier to read the result, 
# which is the use of "indent" parameter to define the numbers of indents.

# It also has a parameters to order the keys in the result, 
# which is the "sort_keys" parameter to specify if the result should be sorted or not.

info = {
  "name": "Joshua",
  "age": 20,
  "married": False,
  "single": True,
  "children": ("Guitar","Bike"),
  "money": None,
  
  "desktop": [
    {"model": "ASUS PC", "ROM": 1024.25},
    {"model": "ASUS VIVOBOOK", "ROM": 475.95}
  ]
}

print(json.dumps(info, indent=4, sort_keys=True))

# You can also define the "separators="", default value is (", ", ": "), 
# which means using a comma and a space to separate each object, and a colon and a space to separate keys from values.