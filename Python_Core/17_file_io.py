import os

file = open("D:\\Gaurav\\Personal\\Version\\repo_python\\Python\\Python_Core\\files\\demo.txt", "r")
content = file.read()
print(content)
print(type(content))

file.close()

print("-----------------------------------------")

file2 = open("D:\\Gaurav\\Personal\\Version\\repo_python\\Python\\Python_Core\\files\\demo.txt", "r")
line1 = file2.readline() # This is demo file
line2 = file2.readline() # creted for python

print(line1)
print(line2)

file2.close()

print("-----------------------------------------")

file3 = open("D:\\Gaurav\\Personal\\Version\\repo_python\\Python\\Python_Core\\files\\demo.txt", "r")
allLines = file3.readlines()
print(allLines)
print(type(allLines))
file3.close()

print("-----------------------------------------")

file4 = open("D:\\Gaurav\\Personal\\Version\\repo_python\\Python\\Python_Core\\files\\sample.txt", "w")
file4.write("Hello Python\n")   
file4.write("I am writing the file")
file4.close()

print("-----------------------------------------")

file5 = open("D:\\Gaurav\\Personal\\Version\\repo_python\\Python\\Python_Core\\files\\sample.txt", "w")
list_lines = ['First line\n', 'Second Line\n', 'Third Line']
file5.writelines(list_lines)
file5.close()

print("-----------------------------------------")

file6 = open("D:\\Gaurav\\Personal\\Version\\repo_python\\Python\\Python_Core\\files\\sample.txt", "a")
file6.write("\nThis line is appended")
file6.close()

print("-----------------------------------------")

file7 = open("D:\\Gaurav\\Personal\\Version\\repo_python\\Python\\Python_Core\\files\\sample.txt", "r+")
con = file7.read()
print(con)
file7.write('\nThis is by read and write')
file7.close()

print("-----------------------------------------")

with open("D:\\Gaurav\\Personal\\Version\\repo_python\\Python\\Python_Core\\files\\sample.txt", "r") as file8:
    c = file8.read()
    print(c)
# file is automatically closed after the block

print("-----------------------------------------")

path = os.path.join('D:\\', 'Gaurav', 'Personal', 'Version', 'repo_python', 'Python', 'Python_Core', 'files', 'sample.txt')
with open(path, "r") as file8:
    data = file8.read()
    print(data)

print("-----------------------------------------")

if os.path.exists(path):
    print('path exists')
else:
    print('path does not exists')
