import re

# check if it starts with 'The' and ends with 'Spain'
txt = 'The rain in Spain'
x = re.search("^The.*Spain$", txt)
print(x)
# return <re.Match object; span=(0, 17), match='The rain in Spain'>

# findall() function
# import re
txt = 'The rain in Spain'
x = re.findall('ai', txt)
print(x)

# return ['ai', 'ai']

# split()
# import re
txt = 'The rain in Spain'
x = re.split('\s', txt)
print(x)

# return ['The', 'rain', 'in', 'Spain']

# you can control the number of occureences by specifying the maxspilt parameter
# import re
txt = 'The rain in Spain'
x = re.split('\s', txt, 1)
print(x)

# retun ['The', 'rain in Spain']

# sub() function replaces the matches the text of your choice
# import re
txt = 'The rain in Spain'
x = re.sub('\s', '9', txt)
print(x) 

# return The9rain9in9Spain

# conrol the number of replacements by specifying the count parameter
txt = 'The rain in Spain'
x = re.sub('\s', '9', txt, 2)
print(x)

# retrun The9rain9in Spain
# note that n - 1

# I don't understand the following code.
# I need to memorize things like how \b works
# import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

# import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string) 

# import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())