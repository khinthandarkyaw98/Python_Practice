# finding LCM(Lowest Common Multiple)

# The lowest common multiple is the least number that is common multiple of both of the numbers

# find the lcms of the following two numbers

import numpy as np 

num1 = 4
num2 = 6

x = np.lcm(num1, num2)

print(x)
# return 12

# finding lcm in arrays
# to find the lowest common multiple of all values in an array
# you can use the reduce() method

# the reduce() uses the ufunc, lcm() on each element and reduce the array by one dimension

# import numpy as np 

arr = np.array([3, 6, 9])

x = np.lcm.reduce(arr)

print(x)

# find the lcm of all an array where the array contains all integers from 1 to 10

# import numpy as np 

arr = np.arange(1, 11)

x = np.lcm.reduce(arr)

print(x)