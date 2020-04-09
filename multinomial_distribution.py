# mutlinomial_distribution
# a generalization of binomial distribution
# outcomes of muti-nomial scenarios unlike binomial 
# where scenarios must be only one of two. 
# e.g. Blood type of a population, dice roll outcome

"""
It has three parameters:
n - number of possible outcomes(e.g. 6 for dice roll).
pvals - list of probabilities of outcomes(e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll)
size - The shape of the returned array
"""

# draw out a sample for dice roll

from numpy import random

x = random.multinomial(n = 6, pvals =[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

print(x)

# visualization of multinomial distributions

# from numpy import random
import matplotlib.pyplot as plt 
import seaborn as sns 

sns.distplot(random.multinomial(n = 6, pvals =[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], size = 1000), hist = False)
plt.show()