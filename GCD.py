# finding GCD(Greatest Common Denominator)

# GCD aks HCF : the biggest number that is a common factor of both of the numbers

import numpy as np 

num1 = 6
num2 = 9

x = np.gcd(num1, num2)

print(x)

# finding the GCD in arrays

# reduce(), gcd() 

# import numpy as np 

arr = np.array([20, 8, 32, 36, 16])

x = np.gcd.reduce(arr)

print(x)