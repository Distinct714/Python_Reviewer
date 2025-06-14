
# IMPORTING CLASS FROM OTHER FILE

# Beside the "from" is the name of a file.
# Beside of import is where actual information or attributes comes from. (class)

from Class_Pizza import Pizza

# Inside the parenthesis, these are the information you give when creating an object. (Values)
# It's taking that information and stored it as an attributes for the object.
pizza_type = Pizza("beef", "cheddar","tomato", "bell pepper") 
print(pizza_type.meat)

# Object Function (Method)
first_toppings = Pizza("beef", "cheddar","tomato", "bell pepper")
print(first_toppings.topping())

# Modify Object Properties
first_toppings.cheese = "Parmesan"
print(first_toppings.cheese)

# Object function (Method)
second_toppings = Pizza("sausage", "swiss","belchamel", "mushroom")
print(second_toppings.topping())

# Without methods and attributes in object, the output will return as memory address.