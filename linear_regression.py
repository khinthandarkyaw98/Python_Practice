# the term regressin is used when you try to find the relationship between variables

# to prdecit the outcome of future events

# uses the relationship between the data-points to draw a straight line through all them

# x = age of the car
# y = speed of the car

import matplotlib.pyplot as plt 

import numpy as np 

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])

y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)

plt.show()

# import scipy and draw the line of linear regression

# import numpy as np
# import matplotlib.pyplot as plt 

from scipy import stats 

# excute a method that returns some important key values of linear regression
slope, intercept, r, p, std_err = stats.linregress(x, y)

# create a function to represent where on the y-axis and the corresponding  x value will be placed
def myfunc(x):
	return slope * x + intercept

# run each value of the x array through the function: the result is a new array with the new values for the y-axis
mymodel = list(map(myfunc, x))

# draw the original scatter plot
plt.scatter(x, y)
# draw the line of linear regression
plt.plot(x, mymodel)
# display the diagram
plt.show()

# r-squared : the relationship of the linear regression
# is meausred with a value called the r-squared

# value ranges from 0 to 1
# 0 means no relationship
# 1 means 100 % rated

# from scipy import stats

# slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r)


