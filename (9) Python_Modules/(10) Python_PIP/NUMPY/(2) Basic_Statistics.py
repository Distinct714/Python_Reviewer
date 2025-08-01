
# A typical first step in analyzing your data is getting to know you data in the first place.

import numpy as np

# np_city = np.array([
#     [1.64, 71.78],
#     [1.37, 63.35],
#     [1.6, 55.09],
#     ...,
#     [2.04, 74.85],
#     [2.04, 68.72],
#     [2.01, 73.57],
# ])

# print(np.mean(np_city[:, 0]))

# print(np.median(np_city[:, 0]))

# correlation
# print(np.corrcoef(np_city[:, 0], np_city[:, 1]))
#
# Standard Deviation
# print(np.std(np_city[:, 0]))


# Generate Data

height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)

np_city = np.column_stack((height, weight))
print(np_city)


#
x = np.array([
    [1, 2, 7], 
    [7, 7, 1]
    ])

y = np.array([
    [6, 5, 5], 
    [0, 6, 1]
    ])

print(x + y)

# column_stack
np_arr1 = np.array([1, 2, 3, 4])
np_arr2 = np.array([5, 6, 7, 8])

print(np.column_stack((np_arr1, np_arr2)))



np_2d = np.array([[2, 3], 
                  [4, 5]])

print(np_2d * np.array([2, 0]))