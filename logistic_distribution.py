# logistic_distribution
# used to describe growth
# used extensively in machine learning in logistic regression, neural networks etc.
# It has three parameters.
# loc = mena, where the peak is, Default 0.
# scale = standard deviation, the flatness of distribution. Default 1.
# size = The shape of the returned array.

# Draw 2x3 samples from a logistic distribution with mean at 1 and stddev 2.0

from numpy import random

x = random.logistic(loc = 1, scale = 2, size = (2,3))

print(x)

# visualization of logistic distribution

# from numpy import random
import matplotlib.pyplot as plt 
import seaborn as sns 

sns.distplot(random.logistic(size = (1000)), hist = False)
plt.show()

# Difference between logistic and normal distribution
"""
Both distributions are near identical, but logistic distribution
has more area under the tails. i.e. It representage more possibility
of occurence of an event further away from mean.  For higher value of scale
(standard deviation) the normal and logistic distributions are near identical
apart from the peak
"""

# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns 

sns.distplot(random.normal(scale = 2, size = 1000), hist = False, label = 'Normal')
sns.distplot(random.logistic(size = 1000), hist = False, label = 'Logistic')

plt.show()