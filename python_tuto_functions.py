# creating a function
def my_func():
	print("Hello")

my_func()

# pass an argument
def my_function(fname):
	print(fname + "Refsnes")

my_function('Emil')

# pass two arguments
def my_function(fname, lname):
	print(fname + " " + lname)

my_function('Emil', 'Refsnes')

"""
if you do not know how many arguments that will be passed 
into your function, 
add a * before the parameter name in the function defintion

It receives a tuple of arguments, 
can access the items accordingly.
"""

def function(*kids):
	print('The youngest child is ' + kids[2])

function('Emil', 'Tobias', 'Linus')

# send arguments with key = value
# order of the arguments does not matter

def my_function(child3, child2, child1):
	print('The youngest child is ' + child3)

my_function(child1 = 'Emil', child2 = 'Tobias', child3 = 'Linus')


# keyword arguments are shortened into **kwargs
def my_function(**kid):
	print('His name is ' + kid['lname'])

my_function(fname = 'Tobias', lname = 'Refsnes')


def my_function(mylist):
	for i in mylist:
		print(i)

fruits = ['apple', 'orange', 'strawberry']

my_function(fruits)

def my_function(x):
	return 5 * x

print(my_function(3))

# pass statement
def my_function():
	pass

# recursion
def tri_ recursion(k):

	if(k > 0):
		result = k + tri_recursion(k - 1)
		print(result)

	else:
		result = 0

	return result
print('\n\n Rescursion Example Results')
tri_recursion(6)