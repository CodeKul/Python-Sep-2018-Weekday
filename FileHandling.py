'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)

f = open("file.txt", "rt")

f.read()
f.read(10)
f.readline()

for x in f:
  print(x)

f.write("Now the file has one more line!")

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")


'''

f = open("file.txt", "rt")
# print(f.read(7))


# line = f.readline(3)
# print(line)

lines = f.readlines()
print(lines)

f = open("myFile.txt", "rb")
# f.write("Name: abc\nAddress: Pune\nNumber: 132456789")

f.seek(6,1)
name = f.readline()

f.seek(9,1)
address = f.readline()

f.seek(8,1)
number = f.readline()

print(name)
print(address)
print(number)