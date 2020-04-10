# add the values in arr1 to the values in arr2.

import numpy as np 

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2)

print('addition', newarr)

# subtraction
# import numpy as np 

newarr = np.subtract(arr1, arr2)

print('subtraction', newarr)

# multiplication
# import numpy as np

newarr = np.multiply(arr1, arr2)

print('multipication', newarr)

# division
# import numpy as np

newarr = np.divide(arr1, arr2)

print('division', newarr)

#power
# import numpy as np 

newarr = np.power(arr1, arr2)

print('power', newarr)

# remainder
# import numpy as np 

newarr = np.mod(arr1, arr2)

print('remainder', newarr)

# same result as mod()

# import numpy as np 

newarr = np.remainder(arr1, arr2)

print('reaminder', newarr)

# divmod() function return both the quotient and the mod. 
# The return value is two arrays, the first array contains the
# quotient and second array contains the mod

# return the quotient and mod

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.divmod(arr1, arr2)

print("quotient and reaminder: ", newarr)

# absolute values
# absolute() should be used to avoid the python's inbuilt math.abs()

arr = np.array([-1, -2, 1, 2, 3, -4])

newarr = np.absolute(arr)

print('absolute values: ', newarr)