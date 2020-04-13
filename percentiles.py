# percentiles are used in statistics to give you a number that describes 
# the value that a given percent of the values are lower than.

import numpy as np 

ages = np.array([5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31])

x = np.percentile(ages, 75)

print('The 75 % of the people are ' , x, 'or younger')

y = np.percentile(ages, 90)

print('The 90 % of the people are ', y, 'or younger')