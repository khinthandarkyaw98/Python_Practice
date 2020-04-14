# x-axis represents the hours of the day
# y-axis represents the speed

# scatter plot

import numpy as np 
import matplotlib.pyplot as plt 

x = np.array([1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22])
y = np.array([100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100])

plt.scatter(x, y)
plt.show()

# linear-regression
from scipy import stats

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
	return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

# polynomial_regression

# polynomial model
mymodel = np.poly1d(np.polyfit(x, y, 3))

# start at position 1 and end at position 22
myline = np.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))

plt.show()

# r-squared 

# the relationship to predict

# pip install numpy scipy scikit-learn
from sklearn.metrics import r2_score

mymodel = np.poly1d(np.polyfit(x, y, 3))

print(r2_score(y, mymodel(x)))

# predict the car passing at 17 P.M\

# mymodel = np.poly1d(np.polyfit(x, y, 3))

speed = mymodel(17)
print(speed)

# bad fit 
x = np.array([89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40])
y = np.array([21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15])

mymodel = np.poly1d(np.polyfit(x, y, 3))

myline = np.linspace(2, 95, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

# r-squared
# from sklearn.metrics import r2_score

print(r2_score(y, mymodel(x)))