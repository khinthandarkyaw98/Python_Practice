# set is a mathematics is a collection of unique elements

# sets are used for operations involving frequent intersection, union and difference operations

# unique() : to find unique elements from any array

# e.g. create a set array, but remember that the set arrays should only be 1-D array

# convert following array with repeated elements to a set

import numpy as np 

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])

x = np.unique(arr)

print(x)

# finding union

# union1d()

# import numpy as np

arr1 = np.array([1, 2, 3, 4])

arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)

print(newarr)

# finding intersection

# instersect1d()

# import numpy as np 

newarr = np.intersect1d(arr1, arr2, assume_unique = True)

print(newarr)

# finding difference

# setdiff1d()

# import numpy as np 

newarr = np.setdiff1d(arr1, arr2, assume_unique = True)

print(newarr)

# finding only the values that are not present in both sets
# setxor1d() method

newarr = np.setxor1d(arr1, arr2, assume_unique = True)

print(newarr)
