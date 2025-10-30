#Numeric Types

a = 10
b = 3.5
c = 2 + 4j

print(c)

print(type(a))  #<class 'int'>
print(type(b))  #<class 'float'>
print(type(c)) #<class 'complex'>
print("----------------------------------------------------")

#String

e = "Test-1"
f = 'Test-2'
g = """ Test-3 - 
this is test
"""

print("----------------------------------------------------")

#List

listTest = ["apple", 1, True, "banana", 1, "apple"]
print(listTest)
print(listTest[1])
listTest.append("Test-1")
print(listTest)

print("----------------------------------------------------")

#Tuple

tupleTest = ("Banana", 1, True, 1.3, "Test-1")
print(tupleTest)
print(tupleTest[1])

print("----------------------------------------------------")

#Dictionary (dict)

dictTest = {"name": "Gaurav", "age": 24, "alive": True, "innerDict": {"laguage": "Python", "experice": "3 Years"}}
print(dictTest)
print(dictTest['name'])
print(dictTest["innerDict"])
print(dictTest["innerDict"]["laguage"])

print("----------------------------------------------------")

#Set and Frozenset
setTest = {"test-1", 1, 2, True, 1, "test-1"}
print(setTest)
setTest.add("test-2")
print(setTest)
#print(setTest[1])  #Not possible

#frozenset
#testFrozen = frozenset("Test-1", "Test-2", "Test-2") - not possible
testFrozen = frozenset(setTest)
print(testFrozen)
print("----------------------------------------------------")

#Boolean

x = True
y = False
print(1 > 2)
print(2 > 1)

print("----------------------------------------------------")

z = None
print(z)
print(type(z))