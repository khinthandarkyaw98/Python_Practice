"""
A permutation refers to an arrangement of elements.
e.g. [3,2, 1] is a permutaion of [1, 2, 3] and vice-versa.
The numpy random module provides two methods for this:
shuffle() and permutation().
"""

# shuffling arrays
# shuffle()

from numpy import random
import numpy as np 

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr)

# generating permutation of arrays

# from numpy import random
# import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))
random.permutation(arr)
print(arr)

# permuatation() returns an re-arranged array( and leaves
# the original array un-changed ) meanwhile shuffle changes