# global variables

x = "awesome"

def myfunc():
	print("Python is " + x)

myfunc()

print("Python is " + x)

# Global Keyword

def func():
	global x
	x = "fantastic"

func()