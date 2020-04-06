# python string formatting

# a placeholder where you want to display the price
price = 49
txt = 'The price is {} dollars'
print(txt.format(price))

# Display a number with two decimals
txt = 'The price is {:.2f} dollars.'
print(txt.format(price))

# multiple values
quantity = 3
itemno = 567
price = 49
myorder = 'I want {} pieces of item number {} for {:.2f} dollars.'
print(myorder.format(quantity, itemno, price))

# index number 
myorder = 'I want {0} pieces of item number {1} for {2:.2f} dollars.'
print(myorder.format(quantity, itemno, prince))

# if you want to refer to the same value more than once, use the index number.
age = 36
name = 'John'
txt = 'His name is {1}. {1} is {0} years old.'
print(txt.format(age, name))

# named indexes
myorder = 'I have a {carname}, it is a {model}.'
print(myorder.format(carname = 'Ford', model = 'Mustang'))