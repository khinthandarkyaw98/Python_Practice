import mymodule

mymodule.greeting('Coral')

a = mymodule.person1['age']
print(a)

# buit-in modules
import platform as pl

x = pl.system()
print(x)

# dir() is a built-in function to list all the function names or variable names
x = dir(pl)
print(x)

# you can import only specific part you like from the module
from mymodule import person1
print(person1['name'])

# here if you use from keyword, 
# you do not need to refer the module name like mymodule.person1['name']