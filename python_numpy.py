# ndarray is faster than the list
# bc it stores in one continuous memory and utiize the lateset CPU architecture
# import numpy as np

# arr = np.array([1, 2, 3, 4, 5])

# print(arr)

# print(np.__version__)
import requests

r = requests.get("http://google.com")
print(r.status_code)

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr)) 

# here 
#AttributeError: partially initialized module 'numpy' has no attribute 'array' (most likely due to a circular import)
# bc i put this file with other file that doesn't work properly in the same folder
# circular import problem occurs then error dependency
# how did i solve?
# aha, I created a new folder and put this file only in it
# problem solved
# thanks stack overflow

# use a tuple to create a NumPy array
arr = np.array((1, 2, 3, 4, 5))
print(arr)
# here tuple is converted into the list bc of numpy

# O-D array
arr = np.array(42)
print(arr)

# 1-D array
arr = np.array([1, 2])

# 2-D arry
arr = np.array([[1, 2], [3, 4]])
print(arr)

# 3-D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)

# you can use ndim to check the number of dimensions
print(arr.ndim)

# higher dimensional arrays
# you can define the number of dimensions by using the ndmin argument
arr = np.array([1, 2, 3, 4, 5], ndmin =5)

print(arr)
print('number of dimensions : ', arr.ndim)

# note that ndmin.... ndim 
# see the difference ?

# access array elements
arr = np.array([1, 2, 3, 4])

print(arr[0]) 

print(arr[2] + arr[3])

# access 2-D arrays
arr = np.array([1, 2, 3, 4], ndmin = 2)
print('2nd element on 1st dim', arr[0, 3])


arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st dim: ', arr[0, 1]) 

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd dim: ', arr[1, 4]) 

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])
# return 6

# negative indexing

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1]) 
# return -10
print(arr[-1, -1])
# return -10

# numpy array slicing
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1: 5])

# return [2 3  4 5]


print(arr[4:]) 

print(arr[:4]) 

# negative slicing
print(arr[-3: -1])

# step
print(arr[1: 5: 2])

# return every other element from the entire array
print(arr[::2])

# Slicing 2-D array
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1: 4])
# return [7 8 9]

print(arr[0:2, 2]) # return both elements, return index 2
# return [3 8]

print(arr[0:2, 1:4])
# return [[2 3 4]
 #       [7 8 9]]

# for n-D array slicing 
"""
arr[row , element]
"""

# checking the data type of an array
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

# defining the data type with dtype parameter
arr = np.array([1, 2, 3, 4, 5], dtype = 'S')
print(arr)
print('S', arr.dtype)


arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype) 

# converting data type on existing arrays
# astype() method
# astype() creates a copy of the array and 
# allows you to specify the data type as a parameter

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')
# newarr = arr.astype(int)
# note that open inverted and close inverted for i but not for int

print(newarr, newarr.dtype)
# retrun [1 2 3] int32

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)
print(newarr, newarr.dtype)
# return [ True False  True] bool

# array copy()
arr = np.array([1, 2, 3, 4, 5])

new = arr.copy()
arr[0] =42

print("Original array", arr)
print("Array copy", new)

# array view()
arrview = arr.view()
arr[0] = 0
print('Original array', arr)
print('Array view', arrview)

# Check if array owns its data
"""
Every NumPy array has the attribute base 
that returns None if the array owns the data.
Otherwise, 
the base  attribute refers to the original object. 
"""
x = arr.copy()
y = arr.view()
print(x.base) # return None
print(y.base) # return [0 2 3 4 5]

# Get the shape of an array
print(arr, arr.shape)

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape) 
# return shape of array : (1, 1, 1, 1, 4)

two_D_arr = np.array([[1, 2], [3, 4]])
print('2D array shape: ', two_D_arr.shape)

# reshape from 1 D to 2 D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3) # here 2 elments so 2 D
print(newarr)

# reshape from 1 D to 3 D
newarr = arr.reshape(2, 3, 2) # here 3 elements so 3 D
print(newarr)

# return copy or view
print(arr.reshape(2, 6).base)

# unknown dimension
# pass - 1 as the value and numpy will calculate this number for you
newarr = arr.reshape(2, 2, -1)
print(newarr)
# we cannot pass - 1 to more than one dimension

# flattening the arrays
# converting a multidimensional arra into a 1 D array

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)

# iterating the numpy arrays
arr = np.array([1, 2, 3])

for x in arr:
	print(x)

# iterating 2-D arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)  # scalar elemenst ( it produces one by one)


for x in arr:
	print(x)

# iterating arrays using nditer()
# it can be used for any dimension
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
	print(x) # scalar elements (one by one)

# iterating array with different data types
# op_dtypes to change the datatype of elements while iterating
# it needs a buffer so flags = ['buffered'] is used

arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags = ['buffered'], op_dtypes =['S']):
	print(x)

# iterating with different step size
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]): # arr[row, element(start: end: step)]
	print(x)
	# return 1 3 5 7

# enumerated iteration using ndenumerate()
# means mentioning sequence number of somethings one by one
arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
	print(idx, x) 
	# return (0,) 1
	#	(1,) 2
	#	(2,) 

# ndenumerate 2D

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x) 
  """
  return 
(0, 0) 1
(0, 1) 2
(0, 2) 3
(0, 3) 4
(1, 0) 5
(1, 1) 6
(1, 2) 7
(1, 3) 8
  """

# numpy joining array
# concatenate()
arr1 = np.array([1, 2, 3, 4])

arr2 = np.array([5, 6, 7, 8])

arr = np.concatenate((arr1, arr2)) # no axis = row 0

# note that double rounded brackets
print("Array concatenate : axis = 0 \n", arr)

# join two 2D arrays along row (axis = 1)

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis = 1)

print("Array concatenate : axis = 1\n ", arr)

# return [[1 2 5 6] [3 4 7 8]]

# joining arrays using stack functions

arr = np.stack((arr1, arr2), axis = 1)
print("Array stacks : axis = 1 \n", arr)

arr = np.stack((arr1, arr2), axis = 2)
print("Array stacks : axis = 2 \n", arr)

# stacking along columns

arr = np.vstack((arr1, arr2))
print("Array stack along columns: \n", arr)

# stacking along height(depth)

arr = np.dstack((arr1, arr2))
print("Array stck along height: \n", arr)

# numpy splitting array
# array_split()

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print('An Array split into 3 arrays: \n', newarr)

# If the array has less elements than required,
# it will adjust from the end accordingly.

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print('An Array split into 4 arrays: \n', newarr)

# split() does not adjust but array_split() adjusts

# splitting 2-D arrays

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)


arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

print(newarr) 

# specify the axis you want to split

newarr = np.array_split(arr, 3, axis = 1)
print(newarr)

# hsplit() = split n-D array into n-D array along rows
newarr = np.hsplit(arr, 3)
print(newarr)

# seraching arrays

# search an element in an array at a certain value
# return an index of the value
# where()

arr = np.array([1, 2, 3, 4, 5, 6, 7, 1, 1])

x = np.where(arr == 1)

print(x)

# find the indexes where the values are even

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr % 2 == 0)

print(x)

# find the indexes where the values are odd

x = np.where(arr % 2 == 1)

print(x)

# searchsorted()

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)

# array must be sorted

arr = np.array([6, 8, 9, 7])

x = np.searchsorted(arr, 7)

print(x)
# return 1 bc it suppose value'7 should be at the place of value '8'

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

print(x) 

# search mutiple values
# Find the indexes where the values 2, 4, and 6 should be inserted:
arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)

# numpy sorting arrays

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))
# return the copy of an array

# sort the array alphabetically
arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr)) 
# return ['apple' 'banana' 'cherry']

# sort the boolean

arr = np.array([True, False, True])

print(np.sort(arr)) 
# return [False True True]

# sorting a 2-D array
arr = np.array([[3, 2, 4], [5, 0, 1]])
# return [[2 3 4] [0 1 5]]

print(np.sort(arr))

# filtering arrays
"""
If the value at an index is True that element 
is contained in the filtered array, 
if the value at that index is False that element 
is excluded from the filtered array.
"""

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)
# return [41 43]

# Random Number in Numpy

# Pseudo Random ( can be predicted ) True Random (cannot be predicted)

from numpy import random 

# gernerate a random integer from 0 to 100
x = random.randint(100)

print("A random Number", x)

# generate a random float from 0 to 1
x = random.rand()

print('A random float', x)

# generate random array

x = random.randint(100, size = (5))

print(x)
# return 5 random values in an array

x = random.rand(5)

print(x)
# return 5 floats in an array

x = random.rand(3, 5)

print(x)
# return a 2 D array with 3 rows and each row with 5 columns

# generate random number from array

# choice()

x = random.choice([3, 5, 7, 9])

print(x)

# choice() with size
x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)
