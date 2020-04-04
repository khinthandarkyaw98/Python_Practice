# and operator to combine conditional checking
a = 200 
b = 33
c = 500

if a > b and c > a:
	print("Both conditions are True.")

# or operator can be used in "and"

# pass statement to avoid getting an error
if b > a:
	pass
# while loop
i = 1
while i < 6 :
	print(i)
	i += 1

# break with loop
i = 1
while i < 6:
	print(i)
	if i == 3:
		break
	i += 1

# continue to stop the current situation
i = 0
while i < 6:
	i += 1
	if i == 3:
		continue
	print(i)

# else statement for the while loop
i = 1
while i < 6:
	print(i)
	i += 1

else:
	print('Hello')

# for loops
fruits = ['apple', 'banana','cherry']
for x in fruits:
	print(x)

for x in fruits:
	print(x)
	if x == 'banana':
		break
for x in fruits:
	print(x)
	if x == 'banana':
		continue

# range()
for x in range(2, 6):
	print(x)

# you can set the steps
for x in range(2, 30, 3):
	print(x)
