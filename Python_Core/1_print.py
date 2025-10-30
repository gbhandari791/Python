#1. Basic Usage

print("Hello World")
print("------------------------------------------------")

#2. Printing Multiple Values

a = "gaurav"
b = 24
print("Name: ", a, "age: ", b)

#3. Using sep (Separator), default space
print("test-1", "test-2", "test-2", sep=",")

#4. Using end (Line Ending), By default, print() adds a new line (\n) at the end.
print("test-1", "test-2", end="|")
print("test-3")

#5. Using f-Strings (Modern Way)

print(f"My name is {a} and I am {b} years old ")

#6. Printing with format() (Older Way)

print("My name is {} and I am {} years old".format(a, b))






