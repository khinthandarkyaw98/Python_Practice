# variance
"""
Variance is another number that indicates how spread out the values are.
In fact, if you take the square root of the variance, 
you get the standard deviation.
Or the other way around, if you multiply the standard deviation by itself, you get the variance.
To calculate the variance, you have to do as follows.
1. Find the mean.
2. For each value: find the difference from the mean.
3. For each difference: find the square value.
4. The variance is the average number of these squared differences.
"""
# but you can user var() of numpy to find the variance.

import numpy as np 

speed = np.array([32,111,138,28,59,77,97])

x = np.var(speed)

print("The variance: ", x)
