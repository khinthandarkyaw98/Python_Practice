""" 
List negative indexing starts from -1
	 Positive indexing starts from 0.
"""
thislist = ["a", "b", "c"]
print(thislist[-1]) 
# return "c"

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# return ['cherry', 'orange', 'kiwi']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
# return ["orange", "kiwi", "melon"]

thislist[2] = "C"
print(thislist)
# return ['a', 'b', 'C']

# Loop Through a List
for x in thislist:
	print(x)

# Chenck if item exists
if "apple" in thislist:
	print("Yes")

# List Length
print(len(thislist))

# Add Item to list
thislist.append("d")

# Add Item with the specific location
thislist.insert(3, "e")
# return ['a', 'b', 'C', 'e', 'd']

# Remove Item
thislist.remove('d')

# pop index reomoves the specified index 
# or the last item if index is not specified
thislist.pop()

# del keyword removes the specified keyword
del thislist[0]

# del keyword can be used to delete the list completely
del thislist

# clear method empties the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()

# copy a list using copy()
"""
You cannot copy a list simply by typing list2 = list1, 
because: list2 will only be a reference to list1, 
and changes made in list1 will automatically also be made 
in list2.
"""
mylist = thislist.copy()

# Copy a list using list()
mylist2 = list(thislist)

# Join Two Lists
# + operator

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) 

# Join Two lists with append()

for x in list2:
	list1.append(x)

print(list1)

# Join the lists with extend()
list4 = ["a", "b" , "c"]
list5 = [1, 2, 3]

list4.extend(list5)
print(list4)

# list constructor to make a new list
# use double round brackets
new_list = list(("orange", "mango", "pineapple" ))
print(new_list)
