# create a python dictionary
thisdict = {
	'brand' : 'Ford',
	'model' : 'Mustang',
	'year'	: 1964
}

print(thisdict)

# accessing an item from the dictionary
x = thisdict['model']

# Instead of using the square bracket, you can also use get() to retrive the value of the dictionary.
y = thisdict.get('model')

# Change the value of dictionaries
thisdict['year'] = 2018

# Loop through a dictionary
# return a key, it will never return a value
for i in thisdict:
	print(i)

# you can print the value by using the following writing style
for i in thisdict:
	print(thisdict[i])

# you can also use values()
for i in thisdict.values():
	print(i)

# Loop through both keys and values by using items()
for x, y in thisdict.items():
	print(x, y)

# Check if the item exists
# check only key
if 'model' in thisdict:
	print("yes")
