# using a package
# use 'camelcase'

# pip install camelcase is essential 
import camelcase

c = camelcase.CamelCase()

txt = "lorem ipsum dolor sit amet"

print(c.hump(txt))

# return Lorem Ipsum Dolor Sit Amet 

# list packages of pip on cmd
# pip list
