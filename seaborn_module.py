# seaborn

# visualize distributions with seaborn
# seaborn is a library that uses matplotlib underneath to plot graphs
#It will be used to visualize random distributions

# install seaborn : pip install seaborn
"""
Displot stands for distribution plot, it takes as input
an array and plots a curve corresponding to the distribution
of points in the array.
import the pyplot object of the matplotlib module in your code 
import the seaborn in your code 
"""
import matplotlib.pyplot as plt 
import seaborn as sns 

# plotting a distplot

sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()

# plotting a distplot without the histogram
# import matplotlib.pyplot as plt
# import seaborn as sns 
sns.distplot([0, 1, 2, 3, 4, 5], hist = False)
plt.show()