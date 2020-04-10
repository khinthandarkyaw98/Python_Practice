# how to create your own ufunc
"""
TO create your own ufunc, you have to define a function,
like you do with normal functions in Python, then you add it to your Numpy ufunc library with the
frompyfunc() method

The fromfunc() method takes the following arguments.
1. function - the name of the function
2. inputs - the number of input argumens (arrays)
3. outputs - the number of output arrays
"""

# create your own ufunc for addition
import numpy as np 
def myadd(x, y):
	return x + y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

# check if a function is ufunc

# check the type of a function to check if it is a ufunc or not

# a ufunc should return <class 'numpy.ufunc'

# check if a function is a ufunc

# import numpy as np 
print(type(np.add))

# check the type of another function: concatenate()

print(type(np.concatenate))