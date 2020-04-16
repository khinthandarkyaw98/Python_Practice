# scale
# standardization

# z = (x - u) / s

"""
z = new value,
x = original value
u = mean
s = standard deviation
"""
# you do not have to do this manually
# StandardScaler()

import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("cars2.csv")

X = df[['Weight', 'Volume']]

scaledX = scale.fit_transform(X)

print(scaledX)

# predict CO2 values
# import pandas
# from sklearn import linear_model 
# from sklearn.preprocessing import StandardScaler

scale = StandardScaler()

df = pandas.read_csv('cars2.csv')

X = df[['Weight', 'Volume']]

y = df['CO2']

sclaedX = scale.fit_transform(X)

regr = linear_model.LinearRegression()

regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

preditctedCO2 = regr.predict([scaled[0]])

print(preditctedCO2)
