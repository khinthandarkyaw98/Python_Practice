import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime('%A'))

# return 2020
#			Sunday

# Creating Date Objects
# import datetime
x = datetime.datetime(2020, 4, 6)
print(x)

# stringFormat
print(x.strftime('%a'))

