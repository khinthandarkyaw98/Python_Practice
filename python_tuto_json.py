import json

# some JSON:
x = '{"name" : "John", "age" : "30", "city" : "New York"}'

# convert from json to python with json.loads()
y = json.loads(x)

# the result is a Python dictionary
print(y["age"])

# convert from python to json wiht json.dumps()

# a python object(dict)
x = {
	'name' : 'John',
	'age' : 21
	'city' : 'New York'
}

y = json.dumps(x)

# result is a JSON string
print(y)

# you can format the JSON string to be readable by using indent parameter
a = json.dumps(x, indent = 4)
print(a)

# use separators to change the default separators
b = json.dumps(x, indent = 4, separators = (". ", "= "))

# order the result
c = json.dumps(x, indent = 4, sort_keys = True)