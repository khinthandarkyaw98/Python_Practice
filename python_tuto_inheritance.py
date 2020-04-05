# inheritance
class Person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname

	def printname(self):
		print(self.firstname, self.lastname)

# use the Person class to create an object, and then execute the printname method
x = Person('John', 'Doe')
x.printname()

# create a child class
#The child class inherits the parent class and so pass inside child's parenthesis.
class Student(Person):
 	pass

x = Student('Mike', 'Olsen')
x.printname()

class Student(Person):
	def __init__(self, fname, lname):
"""
When you add the __init__() function, the child class 
will no longer inherit the parent's __init__() function.
The child's __init__() function overrides
 the inheritance of the parent's __init__() function.
 To keep the inheritance of the parent's __init__() function, 
 add a call to the parent's __init__() function:
"""
		Person.__init__(self, fname, lname):

# super() function
# the child class inherits all methods and properties from its parent
# if super() is used
class Student(Person):
	def __init__(self, fname, lname, year):
		super().__init__(fname, lname):
		# why don't I see self in super()
		self.graduationyear = year

	def welcome(self):
		print('Welcome', self.firstname, self.lastname, 'to the class of', self.graduationyear)
# If you add a method in the child class with the same name as a function in the parent class, 
# the inheritance of the parent method will be overridden.