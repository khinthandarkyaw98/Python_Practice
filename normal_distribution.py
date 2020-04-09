# normal (Gaussian) distribution

# The normal distribution is also called the Gaussian distribution
# It fits the probability distribution of many events, eg. IQ scores, Heartbeat etc
# use random.normal() method to get a normal data distribution

# it has three parameters
# loc- (mean) where the peak of the bell exists.
# scale- (standard deviation) how the flat the graph distribution should be.
# size - The shape of the returned array.

# generate a random normal distribution of size 2x3

from numpy import random

x = random.normal(size=(2, 3))

print(x) 

# generate a random normal distribution of size 2x3 with mean at 1
# and standard deviation of 2

# from numpy import random

x = random.normal(loc = 1, scale= 2, size= (2, 3))

print(x)

# visualization of normal distribution
# from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size = 1000), hist = False)
plt.show()

# the curve of a Normal Distribution is also known as the Bell Curve because of the bell-shaped curve.
