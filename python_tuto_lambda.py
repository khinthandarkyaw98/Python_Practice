# lambda function
"""
Lambda function takes any number of arguments 
but can only have one expression.
"""

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# lambda inside a function
def myfunc():
	return lambda a : a * number

mydoubler = myfunc(2)

print(mydoubler(11))

