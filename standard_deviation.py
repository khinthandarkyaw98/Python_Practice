# standard deviation is a number that describes how spread out the values are

# a low standard deviation means that most of the numbers are close to the mean(average) value.

# a high standard deviation means that the values are spread out over a wider range.

"""
speed = [86,87,88,86,87,85,86]
The standard deviation is: 0.9
Meaning that most of the values are 
within the range of 0.9 from the mean value, which is 86.4.

Let us do the same with a selection of numbers 
with a wider range:

"""
import numpy as np

speed = np.array([86, 87, 88, 86, 87, 85, 86])

x = np.std(speed)

print('The standard deviation: ', x)

