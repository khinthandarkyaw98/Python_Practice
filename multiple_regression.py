# predict the CO2 emission of a car based on
# the size of the engine. but 
# with multiple regression we can throw in more variables,
# like the weight of the car, to make the prediction more accurate.

import pandas

# the pandas module allows us to read csv files 
# and return a DataFrame object

df = pandas.read_csv('cars.csv')

# make a list of the independent values and call this variable x
# put the dependent values in a variable called y

X = df[['Weight', 'Volume']]
y = df['CO2']

# it is common to name the list of independent vaues with a upper case X
# and the list of dependent values with a lower case y

# import sklearn module to use linearRegression()

from sklearn import linear_model

"""
This object has a method called fit() that takes the independent and dependent values as parameters
and fills the regression object with data that describes the relationship
"""

# create a model called LinerRegression()
regr = linear_model.LinearRegression()

# pass independent and dependent variables to fit object
regr.fit(X, y)

# now we have a regression object that are ready to predict
# CO2 values based on a car's weight and volume

# predict the CO2 emission of a car where the weight is 2300 kg, and the volume is 1300 cm
predictCO2 = regr.predict([[2300, 1300]])

# note double [[]] squared brackets

print(predictCO2)

# Coefficient 
"""
The coefficient is a factor that describes the relationship
with an unkown variable.

"""
# print the coefficient vaules of the regression object

# import pandas
# from sklearn import linear_model

df = pandas.read_csv('cars.csv')

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_)

# predict with weight 3300

# from pandas
# import sklearn import linear_model

df = pandas.read_csv('cars.csv')

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

predictedCO2 = regr.predict([[3300, 1300]])

print(predictedCO2)

# here with 2300 grams of weight : CO2 value = 107.20 
# so by using coeff: 107.20 + ( 1000 * 0.00755095) = 114.75968
# The answer is correct. 1000 is the weight difference between the 3300 and 2300
