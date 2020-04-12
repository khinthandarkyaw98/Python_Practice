# numpy provides the ufuncs sin(), cos(), and tan() 
# that takes valus in radians and produce the corresponding sin, cos and tan values

# find sine value of pi/2

import numpy as np 

x = np.sin(np.pi / 2)

print(x)

# find sine values for all of the values in arr.

# import numpy as np 

arr = np.array([np.pi /2, np.pi /3, np.pi /4, np.pi /5])

x = np.sin(arr)

print(x)

# convert degrees into radians

# By default, all of trigo func take radians as parameters
# but we can convert radians to degrees and vice versa as well in Numpy

# radians = pi / 180 * degree values

# convert all of the values in following array to radians

# import numpy as np 

arr = np.array([90, 180, 270, 360])

x = np.deg2rad(arr)

print(x)

# radians to degrees

# convert all of the values in following array to degrees

# import numpy as np 

arr = np.array([np.pi / 2, np.pi, 1.5 * np.pi, 2 * np.pi])

x = np.rad2deg(arr)

print(x)

# finding angles

# numpy provides ufuns arcsin(), arccos(), arctan() that 
# produce radian values for corresponding sin, cos and tan values given

# find the angle of 1.0

# import numpy as np 

x = np.arcsin(1.0)

print(x)

# angles of each vaue in arrays

# import numpy as np 

arr = np.array([1, -1, 0.1])

x = np.arcsin(arr)

print(x)

# hyptenues
# hypot() - takes the base and perpendicular values and 
# prouces hypotenues based on pythagoras theorem

# import numpy as np
base = 3
prep = 4

x = np.hypot(base, prep)
print(x)