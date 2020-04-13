# mean = the average value
# median = the mid point value
# mode = the most common value
import numpy as np 

speed = np.array( [99,86,87,88,111,86,103,87,94,78,77,85,86] )

mean_value = np.mean(speed)

print('Mean: ', mean_value)

# median value is the value in the middle, after you have sorted all the values

median_value = np.median(speed)

print('Median: ', median_value)

"""
Use the Scipy mode() method to find the number that appears that he most
"""
from scipy import stats

mode_value = stats.mode(speed)

print('Mode: ', mode_value)
