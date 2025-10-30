def say_hello():
    print("Hello World")

say_hello()

print('------------------------------------------')

def add(x, y):
    print(x + y)

add(2, 5)

print('------------------------------------------')

def perform_add(x, y):
    return x + y

result = perform_add(10, 10)
print(result)

print('------------------------------------------')

def greet(name = 'guest'):
    print(name)

greet() #guest
greet('Gaurav') #Gaurav

print('------------------------------------------')

def student_info(name, age):
    print(f'{name} - {age}')

student_info(age = 26, name='John')

print('------------------------------------------')

def add_nums(*nums):
    add = 0
    for num in nums:
        add += num

    return add

print(add_nums(1, 2, 3, 4, 5))

print('------------------------------------------')

def display_info(**info):
    for key, value in info.items():
        print(f'key - {key} : value - {value}')

display_info(name='gaurav', age=24)

print('------------------------------------------')

def outer():
    def inner():
        print('Inner function')
    inner()

outer()

print('------------------------------------------')

def get_list():
    return [1, 2, 3, 4]

print(get_list())

print('------------------------------------------')

def get_multi_values():
    return 'test', 1, 3.5

res = get_multi_values()
print(res, type(res)) # ('test', 1, 3.5) <class 'tuple'>

print('------------------------------------------')

def get_funtion():
    def inner():
        print('I am inner function')
    return inner

result1 = get_funtion()
result1() # I am inner function