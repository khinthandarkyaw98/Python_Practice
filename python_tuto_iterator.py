# iterator object
mytuple = ('apple', 'banana', 'cherry')
myit = iter(mytuple)

# used next()
print(next(myit))
print(next(myit))
print(next(myit))

# string is also an iterable object
mystr = 'banana'
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# for loop to iterate
for x in mytuple:
	print(x)

mystr = 'strawberry'
for x in mystr:
	print(x)

# __iter__() and __next__() must have return statement
class MyNumbers:
	def __iter__(self):
		self.a = 1
		return self

	def __next__(self):
		x = self.a
		self.a += 1
		return x

myclass = MyNumbers()
myiter = iter(myclas)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# the above code can cause an error
# we have to raise StopIteration to solve the error
class MyNumbers:
	def __iter__(self):
		self.a = 1
		return sellf

	def __next__(slef):
		if self.a < = 20:
			x = self.a
			self.a += 1
			return x
		else:
			raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass) # you have to pass class in iter 

for x in myiter:
	print(x)