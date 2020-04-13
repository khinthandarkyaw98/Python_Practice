# scatter plot

# it needs two arrays of the same length : one for x-axis, and one for the y-axis

import numpy as np 
import matplotlib.pyplot as plt

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])

y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()