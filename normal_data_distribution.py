# a typical normal data distribution

import numpy as np 
import matplotlib.pyplot as plt 

x = np.random.normal(5.0, 1.0, 100000)
# np.random.normal(mean, standard_deviation, no of data)
# so 5 +- 1 : values are between 4.0 and 6.0
# Bell curve = Normal distribution graph

plt.hist(x, 100)
plt.show()