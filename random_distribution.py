"""
A random distribution is a set of random numbers 
that follow a certain propability density function.

Probability Density Function:
A function that describes a continuous probability.
i.e. probability of all values in an array.

The probability is set by a number between 0 and 1, 
where 0 means that the value will never and 
1 means that the value will always occur.

Generate a 1-D array containing 100 values,
where each value has to be 3, 5, 7 or 9.
The probability for the value to be 3 is set to be 0.1.
The probability for the value to be 5 is set to be 0.3.
The probability for the value to be 7 is set to be 0.6.
The probability for the value to be 9 is set to be 0.
"""

from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0], size=(100))

print(x)

"""
The sum of all probability numbers should be 1.
Even if you run the example above 100 times, the value 9 will
nevr occur.
You can return arrays of any shape and size by specifying
the shape in the size parameter.
"""

# same example, but return a 2-D array

# from numpy import random

x = random.choice([3, 5, 7, 9], p = [0.1, 0.3, 0.6, 0.0], size = (3, 5))

print(x)


