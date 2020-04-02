# remove whitespaces
x =  " Hello "
print(x.strip())
# return "Hello"

# format
"""
You can combine strings and numbers by using the format() method!
"""

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age)) 
# return "My name is John, and I am 36"

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

"""
You can use index numbers {0} to be sure 
the arguments are placed in the correct placeholders:
"""
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) 
# return "I want to pay 49.95 dollars for 3 pieces of item 567."

# escape character ( used when there're 2 double quotes)
txt = "We are the so-called \"Vikings\" from the north."

# check if an object is an integer or not:
x = 200
print(isinstance(x, int))

