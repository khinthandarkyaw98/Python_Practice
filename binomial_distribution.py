# binomial_distribution is a discrete distribution

# it describes the outcome of binary scenarios, 
# e.g. toss of a coin, it will either be head or till
# it has three parameters
# n - number of trials
# p - probability of occurence of each trial(e.g for toss of a coin = 0.5 for each)
# size - the shape of the returned array

# Discrebe Distribution -
# the distribution is defined at separate set of events.

from numpy import random

x = random.binomial(n = 10, p = 0.5, size = 10)

print(x)

# visualization of binomial distribution

import matplotlib.pyplot as plt 
import seaborn as sns 

sns.distplot(random.binomial(n = 10, p = 0.5, size = 1000), hist = True, kde = False)
plt.show()

# difference between normal and binomial distribution

"""
The main difference is that normal distribution is continuous 
whereas binomial is discrete, but if there are enough data points
it will be quite similar to normal distribution will certain loc, and scale
"""
# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns 

sns.distplot(random.normal(loc = 50, scale = 5, size = 1000), hist = False, label = 'normal')
sns.distplot(random.binomial(n = 100, p = 0.5, size = 1000), hist = False, label = 'binomial')
plt.show()
