# MAPPING TYPE

# DICTIONARY

# Dictionaries are ordered and mutable that allow you to store different key-value pairs.
# This is created with curly braces where its key and value is separated by colon.
# Each items are separated by a comma.

# This will print out as empty dictionary
empty_dict = {}

# Adding Key-value pairs in an empty dictionary
empty_dict["Name"]= "Mavuika"
empty_dict["Position"]= "Pyro Archon"
empty_dict["Age"]= 500
empty_dict["Weapon"]= "Claymore"
print(empty_dict)

# The main operation of a dictionary is to extract a value based on the key name. 
# Unlike lists, where index numbers are used, dictionaries allow the use of a key to access its members. 
# Dictionaries can also be used to sort, iterate, and compare data.
profile_details = dict(name="Joshua", age=20, country="Philippines")
print(profile_details)

# Adding new key-value pairs
profile_details["email"] = "joshuabote2004@gmail.com"
print(profile_details)

# It can have duplicate values, but not duplicate keys.
# Values with duplicate keys will overwrite existing values.

# Using for loop in accessing key-value pairs.

# .keys(): is a method used to return a list of all the keys in the dictionary.
for key in profile_details.keys():
    print(key)

# .values(): is a method used to return a list of all the values in the dictionary.
for value in profile_details.values():
    print(value)

# fromkeys() is a method that returns a dictionary with the specified keys and the specified value.
x = ("1", "2", "3")
y = 0

nums = dict.fromkeys(x, y)
print(nums)


# When accessing a certain key-value pairs, use square brackets.
# You can access multiple key-value pairs as long as there is a comma or any separation.
weekConversion = {
    "Sun": "Sunday",
    "Mon": "Monday",
    "Tue": "Tuesday",
    "Wed": "Wednesday",
    "Thu": "Thursday",
    "Fri": "Friday",
    "Sat": "Saturday"
}

access = weekConversion["Sun"]
print(access)

# If the key or values is not present inside of dictionary, this will raise an exception or key error.

# If you want to change a certain key-value pairs or create a new one, use .update method.
weekConversion2 = dict(Sun="sunday", Sat="saturday")
weekConversion.update(weekConversion2)
print(weekConversion)


# The setdefault() method returns the value of the item with the specified key.
# If the key does not exist, insert the key, with the specified value. - dictionary.setdefault(keyname, value) -
weekConversion3 = weekConversion.setdefault("WD", "Weekdays")
print(weekConversion3)


# The .get method returns the value of the item with the specified key.
# It allows to access a single value in a dictionary.
print(weekConversion.get("Fri"))

# If the key is not present in the dictionary with .get method, then it simply returns a None.
# You can also assign any value beside None in output.
print(weekConversion.get("Hello", "Invalid Key"))

# sorted is a function used to sort the dictionary.
# This returns a new sorted iterable objects without modifying the original iterable.
for week in sorted(weekConversion.values()):
    print(f"The day is {week.lower()}.")

# The items() method returns all the key:value pairs in a dictionary. (with dict_items as output)
my_numbers = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}

for key, value in my_numbers.items():
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")


# The pop() method removes the specified item from the dictionary.
my_numbers.pop(5)
print(my_numbers)

# The popitem() method removes the item that was last inserted into the dictionary. 
# In versions before 3.7, the popitem() method removes a random item.
my_numbers.popitem()
print(my_numbers)

# Creating tuple is possible in dictionary, however, creating list in dictionary will run an error
# because this is ordered and cannot be used as a key.
my_tuple = (7, 8)
numbers = {my_tuple: 10}
print(numbers)

# You can copy a dictionary by using the built-in Dictionary method copy().
# Another way to make a copy is to use the built-in function dict().

# USE OF IF_ELSE STATEMENTS IN DICTIONARY
courses = {"LLM Concepts": "AI", 
           "Introduction to Data Pipelines": "Data Engineering", 
           "AI Ethics": "AI",
           "Introduction to dbt": "Data Engineering", 
           "Writing Efficient Python Code": "Programming",
           "Introduction to Docker": "Programming"}

# Loop through the dictionary's keys and values
for key, value in courses.items():
  
  # Check if the value is "AI"
  if value == "AI":
    print(key, "is an AI course")
  
  # Check if the value is "Programming"
  elif value == "Programming":
    print(key, "is a Programming course")
  
  # Otherwise, print that it is a "Data Engineering" course
  else:
    print(key, "is a Data Engineering course")


# NESTED DICTIONARIES
task = {
  "Saturday" : {
        "5am" : "Ride a bike",
        "11am" : "Buy meals"
  },
  "Sunday" : {
        "6am" : "Do jogging",
        "1pm" : "Grind Python"
  },
  "Monday" : {
        "8am" : "Do house chores",
        "12pm" : True
  }
}

print(task["Saturday"]["11am"])

# LOOP THROUGH NESTED DICTIONARIES
for x, obj in task.items():
    print(x)
    for y in obj:
        print(y + ":", obj[y])


# MAKING A LIST OF VALUES:
pizza = {
    "crust": "stuffed",
    "toppings": ["mushrooms", "extra cheese", "bell pepper"],
}

print(f"You ordered a {pizza["crust"]} crust pizza with the following toppings:")

for topping in pizza["toppings"]:
    print(f"\t\t{topping}")
