# try block tests a block code of errors
# except block handles the eror
# finally block executes code regardless of the result of the try - and except blocks.

try: 
	print(x)

except:
	print('An exception occurred')

# Many Exceptions
try: 
	print(x)
except NameError: # use different exception name
	print('Variable x is not defined')
except:
	print('Something else went wrong')

# use else to generate for no error case
try:
	print(x)
except:
	print('Something went wrong')
else:
	print('Nothing went wrong')

# finally block is executed if the try block raises an error or not
try:
	print(x)
except:
	print('Something went wrong')
finally:
	print('The \'try except\' is finished')

# try to open and write to a file that is not writeable.
try:
	f = open('file.txt')
	f.write('Lorum Ipsum')
except:
	print('Something wrong!!!')
finally:
	f.close()

# Raise an exception
