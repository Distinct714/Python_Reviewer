
# NUMPY ARRAYS
import numpy as np

# The output will be numpy.ndarray since you specify the type of given variable.
# ndarray stands for n-dimensional array

# Both np_height and np_weight are one dimensional arrays and it is possible to create more than one dimensional arrays.
np_height = np.array([5.78, 4.34, 5.11, 4.97])
print(type(np_height))

np_weight = np.array([52.6, 67.4, 81.5, 71.2])
print(type(np_weight))

# 2D NumPy Arrays

np_2d = np.array([
    [5.78, 4.34, 5.11, 4.97], 
    [52.6, 67.4, 81.5, 71.2]
    ])

# The shape is an attribute of np_2d array where the output show 2 rows and 4 columns as this gives more information about
# what data structure should look like.
print(np_2d.shape)

# Subsetting arrays (Index) The first index is first list, then the second is inside the list
print(np_2d[0][2])

print(np_2d[:, 1:3])

print(np_2d[1, :])