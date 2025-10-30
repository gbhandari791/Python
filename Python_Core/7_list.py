fruits = ['apple', 'banana', 'orange']
number = [1, 2, 3, 4]
mixed = ['apple', 1, 2, True, 3.5]

print(fruits[0])
print(fruits[1])
print("--------------------------------------")
print(fruits[-1])
print(fruits[-2])

print("--------------------------------------")

fruits[0] = 'mango'
print(fruits) #['mango', 'banana', 'ornage']

print("--------------------------------------")

fruits.append('dragonfruit')
print(fruits) #['mango', 'banana', 'orange', 'dragonfruit']

fruits.insert(1, 'cherry')
print(fruits) #['mango', 'cherry', 'banana', 'orange', 'dragonfruit']

fruits2 = ['lemon', 'watermelon']
fruits.extend(fruits2)
print(fruits) #['mango', 'cherry', 'banana', 'orange', 'dragonfruit', 'lemon', 'watermelon']

print("--------------------------------------")

fruits.remove('mango')
print(fruits)

fruits.pop(2)
print(fruits)

del fruits[4]
print(fruits)

#fruits.clear()
print(fruits)

print("--------------------------------------")

if 'lemon' in fruits:
    print('Banana is present in fruits')

print("--------------------------------------")

num = [2, 4, 1, 5, 3]

num.reverse() 
print(num) #[3, 5, 1, 4, 2]

num.sort() 
print(num) # [1, 2, 3, 4, 5]

num.sort(reverse=True)
print(num) #[5, 4, 3, 2, 1]

print("--------------------------------------")

origList = [1, 2, 3, 4]

copyList1 = origList.copy()
origList.append(5)
print(copyList1)

#OR

copyList2 = list(origList)
origList.append(6)
print(copyList2)