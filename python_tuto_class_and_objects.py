# create a class
class Myclass:
	x = 5

p1 = Myclass()
print(p1.x)

# __init__() function
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

p1 = Person('John', 36)

print(p1.name, p1.age)

# Object methods
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def myfunc(self):
		print('Hello my name ' +  self.name)

p1 = Person('Alice', 21)
p1.myfunc()

# self paramenter is a reference to the current instance of the class.
# it doesn't need to be named self, you can give the name whatever you want to
class Person:
	def __init__(mysillyobject, name, age):
		mysillyobject.name = name
		mysillyobject.age = age

	def myfunc(abc):
		print('Hello my name is ' + abc.name)

p1 = Person('John', 36)
p1.myfunc()

# Modify Object Properties

p1.age = 40

# Delete Object Properties
# use del keyword
 
del p1.age

# Delete Objects
del p1

# pass statement for the class 
class Persons:
	pass

	