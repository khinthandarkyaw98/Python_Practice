# to measure the accuracy of your model

# a training set and a testing set

# 80 20 Rule for the data, 80 % for training and 20 % for testing

# train the model means create the model
# test the model tests the accuracy of the model

# start with a data set you want to test

# in this data set, there are 100 customers in a shop, and their shopping habits

import numpy as np 
import matplotlib.pyplot as plt 

np.random.seed(2)
# makes the random numbers predictable
# with the seed reset(every time), the same set of numbers will appear every time

x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100) / x
 

# np.random.normal(loc = mean, scale = std, size) 
plt.scatter(x, y)
plt.show()

# x axis represents the number of minutes before making a purchase
# y axis represents the amount of money spent on the purchase

# split into train/test 
train_x = x[: 80] # end before 80
train_y = y[: 80]

test_x = x[80 :] # start at 80 
test_y = y[80 :]

# display the training set

plt.scatter(train_x, train_y)
plt.show()

# display the testing set

plt.scatter(test_x, test_y)
plt.show()

# polynomial regression is the best fit for this case

# create the model

mymodel = np.poly1d(np.polyfit(train_x, train_y, 4))

myline = np.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()

"""
import numpy as np
"""
from sklearn.metrics import r2_score
"""
np.random.seed(2)

x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100) / x

trian_x = x[: 80]
trian_y = y[: 80]

test_x = x[80: ]
test_y = y[80: ]

mymodel = np.poly1d(np.polyfit(train_x, train_y, 4))

"""

r2 = r2_score(train_y, mymodel(train_x))

print(r2)

# for test case : r-squared 
"""
import numpy as np 
from sklearn.metrics import r2_score

np.random.seed(2)

x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100) / x

train_x = x[: 80]
train_y = y[: 80]

test_x = x[80: ]
test_y = y[80: ]

mymodel = np.poly1d(np.polyfit(train_x, train_y, 4))

"""

r2 = r2_score(test_y, mymodel(test_x))
print(r2)

# r-squared for both training and testing cases are good and do we can predict values

# how much money will a buying customer spend, if she or he stays in the shop for 5 minutes?

print(mymodel(5))

