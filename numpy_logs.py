# numpy provides function to perform log at the base 2, e and 10.

# log at the base 2 

import numpy as np 

arr = np.arange(1, 10)

# arange(1, 10) returns an array with integers starting from 1(included) to 10 (not included)

print("Log base 2: ", np.log2(arr))

# log at base 10

# import numpy as np 

arr = np.arange(1, 10)

print('Log base 10',np.log10(arr))

# natural log or log at base e

# import numpy as np 

arr = np.arange(1, 10)

print("Log base e or Natural log: ", np.log(arr))

# log at any base 

# we have to use frompyufunc() to use math.log

from math import log
# import numpy as np 

nplog = np.frompyfunc(log, 2, 1)

print(nplog(100, 15))
