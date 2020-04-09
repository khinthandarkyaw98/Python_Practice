# rayleigh_distribution

# used in signal processing

# It has two parameters.
# scale - standard deviation, decides how flat the distribution will be default 1.0
# size - the shape of the returned array

# draw out a sample for rayleigh distribution with scale of 2 with size 2x3

from numpy import random

x = random.rayleigh(scale = 2, size = (2, 3))

print(x)

# visualization of rayleigh distribution
# from numpy import random
import matplotlib.pyplot as plt 
import seaborn as sns 

sns.distplot(random.rayleigh(size = 1000), hist = False)
plt.show()

# similarity between rayleigh and chi square distribution

# at unit stddev the???? and 2 df rayleigh and chi square represent the same distribution.
