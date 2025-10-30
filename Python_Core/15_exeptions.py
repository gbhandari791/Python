try:
    a = 10/0
except Exception as e:
    print(f'following error  occurs  : {e}')

print('---------------------------------------------------')

try:
    a = 10/0
except ZeroDivisionError as ze:
    print(f'following error occures : {ze}')
except ValueError as ve:
    print("Value error occures")

print('---------------------------------------------------')

try:
    print('No error occured')
except:
    print('error occured')
else:
    print('running if error noy occured')

print('---------------------------------------------------')

try:
    a = 10/0
except: 
    print('Exception occured')
finally:
    print('This will always execute')

print('---------------------------------------------------')

age = 15

if age <  18:
    raise ValueError("Age should be more than 18")

print('---------------------------------------------------')
