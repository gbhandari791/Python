my_set_1 = {1, 2, 3, 3, 4, 1}
print(my_set_1)

#or

my_set_2 = set([1, 2, 3, 3, 4])
print(my_set_2)

print("-----------------------------------")

for item in my_set_1:
    print(item)

my_set_1.add(6)
print(my_set_1)

print("-----------------------------------")

my_set_1.update([7, 8])
print(my_set_1)

print("-----------------------------------")

my_set_1.remove(1) # removes 1 (error if not found)
my_set_1.discard(3) # no error even if 2 not found

print(my_set_1)

print("-----------------------------------")

# value = my_set_1.pop()
# print(value)

print("-----------------------------------")

my_set_1.clear()
print(my_set_1)

print("-----------------------------------")

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union: ", a | b) 
print("Intersection: ", a & b)
print("Difference:", a - b)
print("Symmetric Difference: ", a ^ b)

print("-----------------------------------")

test_set = {10, 20, 30}
print(20 in test_set)  # True
print(40 not in test_set) # True

print("-----------------------------------")

test_set_2 = {1, 2, 3, 4}
test_froz_set = frozenset(test_set_2)
print(test_froz_set)

print("-----------------------------------")
