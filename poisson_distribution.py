# poisson distribution
# poisson distribution is a discrete distribution

# it estimates how many times an event can happen in a specified time.
# e.g. If someone eats twice a day what is probability he will eat thrice?
# It has two parameters
# lam - rate or known number of occurences e.g. 2 for above problem
# size - The shape of the returned array

# generate a random 1x10 distribution for occurence 2

from numpy import random

x = random.poisson(lam = 2, size = 10)

print(x)

# visualization of poisson distribution

# from numpy import random
import matplotlib.pyplot as plt 
import seaborn as sns 

sns.distplot(random.poisson(lam =2, size = 1000), kde = False, label = 'Poisson')

plt.show()

# differnce between normal and poisson distribution

# normal distribution is continuous whereas poisson is discrete
# for a large enough poisson distribution it will become similar to normal distribution with certain std dev and mean

# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns 

sns.distplot(random.normal(loc = 50, scale = 7, size = 1000), hist = False, label = 'Normal')
sns.distplot(random.poisson(lam = 50, size = 1000), hist = False, label = 'Poisson')
plt.show()

# Difference between Possion and Binomial Distribution

"""
The difference is very subtle it is that, 
binomial distribution is for discrete trials, whereas poisson distribution is for continuous trials.
But for very large n and near-zero p binomial distribution is near 
identical to poisson distribution such tht n * p is nearly equal to lam.
"""
# from numpy import random
# import matplotlib.pyplot as plt 
# import seaborn as sns
sns.distplot(random.binomial(n = 1000, p = 0.01, size = 10000), hist = False, label ='Binomial')
sns.distplot(random.poisson(lam = 10, size = 1000), hist = False, label = 'Poisson')

plt.show()