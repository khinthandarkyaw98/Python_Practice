# Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# negative indexing starts at -1
print(thistuple[-1])
# return cheery

# you can't change the value of a tuple
""" You have to convert the tuple into the list
	in case to change the value of a tuple 
"""

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Loop through a tuple
for i in x:
	print(i)

# check if item exists
for "apple" in x:
	print("Yes")

# Tuple length
print(len(x))

# adding new item to the tuple causes an error

# Creating a tuple with only one item
thistuple = ('apple',)

# You have to add comma at the end of the item
# Else, python will not recognize it as a tuple

# You cannot remove the item
# However, you can delete the entire tuple
del thistuple

# Join two Tuples
tuple1 = ('a', 'b', 'c', 'd')
tuple2 = ('e',)

tuple3 = tuple1 + tuple2
print(tuple3)

# Tuple constructor
# Note that double rounded brackets have to be used
thistuple = tuple(('apple', 'banana', 'cherry'))
print(thistuple)

# finding the location of the value
# use index()
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x) 
#return 3

