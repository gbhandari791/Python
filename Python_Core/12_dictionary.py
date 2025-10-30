test_dict_1 = {"name": "gaurav", "age": 24}
print(test_dict_1)

#OR
print("------------------------------------------")

test_dict_2 = dict(name="Nikhil", age=42)
print(test_dict_2)

print("------------------------------------------")

print(test_dict_1['name'])

print(test_dict_1.get("john", "Not Found"))

print("------------------------------------------")

test_dict_1['laguage'] = "python"
print(test_dict_1)

print("------------------------------------------")

test_dict_1['name'] = 'john'
print(test_dict_1)

print("------------------------------------------")

for key in test_dict_1:
    print(key)

print("------------------------------------------")

for value in test_dict_1.values():
    print(value)

print("------------------------------------------")

for key, value in test_dict_1.items():
    print(key, " : ", value)

print("------------------------------------------")

students = {
    "student1": {"name": "John", "age": 20},
    "student2": {"name": "Emma", "age": 22}
}
print(students["student1"]["name"])
