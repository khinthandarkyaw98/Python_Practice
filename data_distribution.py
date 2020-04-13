# creating a bigger data set

# create an array containing 250 random floats between 0 and 5

# use uniform()

import numpy as np 

x = np.random.uniform(0.0, 5.0, 250)

print(x)

# histogram

# we can draw a histogram with the data we collected 
# matplotlib.pyplot to draw a histogram

#import numpy as np 
import matplotlib.pyplot as plt 

x = np.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5) # a histogram with 5 bars

plt.show()

# create an array with 100000 random nmbers, and display them using a histogram with 100 bars

# import numpy as np 
# import matplotlib.pyplot as plt

x = np.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()
