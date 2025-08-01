
# NUMPY (NUMERIC PYTHON)

# NumPy is a Python library used for working with arrays created in 2005 by Travis Oliphant.
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.

# It is used as an alternative to Python list to perform calculations over entrie array. (Easy and Fast)
import numpy as np

# Array is a commonly used function in numpy. The commas will remove automatically.
# Numpy arrays cannot contain elements with different types. 
# Second, the typical arithmetic operators, such as +, -, * and / have a different meaning for regular Python lists and numpy arrays.

# BMI CALCULATIONS SAMPLE
height = [5.78, 4.34, 5.11, 4.97]
np_height = np.array(height)
print(np_height)

weight = [52.6, 67.4, 81.5, 71.2]
np_weight = np.array(weight)
print(np_weight)

bmi =  np_weight / np_height ** 2
print(bmi)

# Remember, the numpy array contain only one type and will converted into string.
my_array = np.array([1.2, "is", True])
print(my_array)


# FIRST SAMPLE

# The output concatenates two list, generating a list of six elements.
nums = [1, 2, 3]
adding = nums + nums
print(adding)

# With numpy array, the output added two list where the Python do an element-wise sum of the arrays.
num_array =  np.array([1, 2, 3])
adding2 = num_array + num_array
print(adding2)


# Instead of doing like what is shown above, you can also do this to simply call the array functions without the use of numpy dot here.
from numpy import array

array([4, 5, 6])

# SECOND Sample
fruit_weight = ["apple", 21.5, "banana", 24.3, "carrot", 10.7, "durian", 19.2]
new_fruit = fruit_weight + ["eggplant", 11.8]

print(f"{str(len(new_fruit))} is the length of fruit elements.")

np_fruit_weight = np.array(new_fruit)
print(np_fruit_weight)

# Getting the index inside of Numpy
# Subsetting (using the square bracket notation on lists or arrays) works exactly the same with both lists and arrays.
bmi = array([1.57445433, 3.5783304, 3.12115839, 2.88248606])
print(bmi[1])

print(bmi[bmi < 2])