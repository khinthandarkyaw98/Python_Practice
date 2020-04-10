# rounding decimals 

# There are primarily five ways of rounding off decimals in Numpy
# truncation
# fix
# rounding
# floor
# ceil

# Truncation
# to integer closet to zero. Use the trunc() and fix() functions.

# example
# truncate elements of following array:

import numpy as np 

arr = np.trunc([-3.1666, 3.6667])

print('truncation: ', arr)
# remove the decimal points

# round() increments preceding digit or decimal by 1 if >= 5 else do nothing.

# if 3.1666 then 3.2

# import numpy as np 

arr = np.around(3.1666, 2)

print("Around to 2 decimal places: ", arr)

# floor() rounds off decimal to nearest lower integer.

# import numpy as np 

arr = np.floor([-3.1666, 3.6667])

print("floor: ", arr)

# floor() returns floats, unlike trunc() returns integers

# ceil() rounds off decimal to nearest upper integer

# import numpy as np 

arr = np.ceil([-3.1666, 3.6667])

print("Ceil: ", arr)
