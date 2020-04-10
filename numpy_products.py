# products
# prod([])

import numpy as np 

arr = np.array([1, 2, 3, 4])

x = np.prod(arr)

print("Product: ", x)

# find the product of the elements of two arrays

# import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

x = np.prod([arr1, arr2])

print("Product of two arrays: ", x)

# product over an axis

newarr = np.prod([arr1, arr2], axis = 1)

print('Product over an axis: ', newarr)
