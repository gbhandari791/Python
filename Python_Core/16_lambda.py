add = lambda x, y: x + y
print(add(10, 20))


say_hello = lambda: 'Hello!'
print(say_hello())

def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))

print('---------------------------------------')

listNum = [1, 2, 3, 4, 5]

map = map(lambda x: x + 1, listNum)
print(map) #<map object at 0x00000289C3DE9680>

result_list = list(map)
print(result_list) #[2, 3, 4, 5, 6]

print('---------------------------------------')

list_num = [1, 2, 3, 4, 5]

filter_num = filter(lambda x: x % 2 == 0 , list_num)
filter_list = list(filter_num)
print(filter_list) #[2, 4]

print('---------------------------------------')

names = ['Gaurav', 'Nikhil', 'devang']
sorted_names = sorted(names, key= lambda name: name.lower())
print(sorted_names)

reversed_list = sorted(names, key= lambda name: name.lower(), reverse=True)
print(reversed_list)

print('---------------------------------------')

max_num = lambda a, b: a if a > b else b
print(max_num(10, 20))