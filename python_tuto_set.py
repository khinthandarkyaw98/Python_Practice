# creating a set
thisset = {'apple', 'banana', 'cherry'}
print(thisset)

#set are unordered and unindexed 
# you cannot expect how the order will pop up whenver you run 

# you cannot add a new item to the set with a specified positon
# However, you can add in case you cannot expect where it will be located

# you cannot change the item of the set once it was created

# use add()
thisset.add('orange')
print(thisset)

# use update([]) to add multiple items 
thisset.update(['papaya', 'beans', 'strawberry'])
print(thisset)

# use remove()
thisset.remove('strawberry')

# use discard()
thisset.discard('banana')

# use pop()
# you do not know which item is removed bc it is unordered
thisset.pop()

# empty the set
thsiset.clear()

# delete the set completely
del thsiset

# Join Two sets
# union()
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# update()

set1.update(set2)
print(set1)

# set() constructor
# note the double round brackets
thisset = set(('a', 'b', 'c'))

