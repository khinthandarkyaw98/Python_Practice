# numpy ufuncs

# universal functions
# operates on the ndarray object

# implement vectorization in Numpy which is way faster than iterating over elements
# provide broadcasting and additional methods like reduce, accumulate etc. that are very helpful for computation

# take addtional arguments
# where - boolean array or condition defining where the opearations should take place
# dtype - defining the return type of elements
# out - output array where the return value should be copied

# vectorization
# converting iterative statements into a vector based operation is called vectorization
# faster as modern CPUs are optimized for such operations
# add the elements of two lists
# list1 : [1, 2, 3, 4]
# lsit2 : [4, 5, 6, 7]
# One way of doing it is to iterate over both of the lists and then sum each elements.
# without ufunc, we can use Python's built-in zip() method.
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z =[]

for i, j in zip(x, y):
	z.append(i + j)
print(z)

# numpy has a ufunc for this, called add(x, y) that will produce the same result.
import numpy as np 

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]

z = np.add(x, y)
print(z)