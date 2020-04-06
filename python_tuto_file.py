# file 
# open('filename','mode')

# opening a file
f = open('file.txt')

# open a file and read as a text
f = open('file.txt', 'rt')

# read the file
f = open('file.txt', 'r')
print(f.read())

# read only parts of the file
f = open('file.txt', 'r')
print(f.read(5))
# return the first characters of the file from 0 to 5
# return Hello

# readline()
f = open('file.txt', 'r')
print(f.readline())
# return the first line in the file

f = open('file.txt', 'r')
print(f.readline())
print(f.readline())
# return the firstline and secondline in the file

# return the whole file--> you have to loop through the file
f = open('file.txt', 'r')
for i in f:
	print(x)

# close the file
f = open('file.txt', 'r')
print(f.read())
f.close()
# you have to close the file. Don't forget

# writing to an exsiting file
f = open('file.txt', 'a')
f.write('Now the file has more content!')
f.close()

# open and read the file after the appending
f = open('file.txt', 'r')
print(f.read())
f.close()

# overwrite the content
f = open('file.txt', 'w')
f.write('Oh, I have deleted the content!')
f.close()

# open and read the file after the appending
f = open('file.txt', 'r')
print(f.read())
f.close()

# create a new file
f = open('file2.txt', 'x')
# error occurs if the file already exits 

# python delete a file
# to delete a file, you must import the OS module, and run its os.remove() function.
import os
os.remove('file2.txt')

# check if file exists to avoid the error
# import os
if os.path.exists('file2.txt'):
	os.remove('file2.txt')
else:
	print('The file does not exist')

# Delete an entire folder, use os.rmdir()
# import os
os.rmdir('myfolder')

