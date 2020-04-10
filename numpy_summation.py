# add() is done between two elements : return an array
# sum([]) happens over n elements : return an element

import numpy as np 

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

newarr = np.add(arr1, arr2)

print("add():", newarr)

newarr = np.sum([arr1, arr2])
# note that sum([])

print("sum(): ", newarr)

# Summation over an axis

newarr = np.sum([arr1, arr2], axis = 1)

print("sum() over an axis", newarr)

# cummulative sum : partially adding the elements in array

# The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10]

# cumsum()

# import numpy as np 

arr = np.array([1, 2, 3])

print("cummulative Sum: ", np.cumsum(arr))