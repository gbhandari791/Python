#list

list = [1, 2, 3, 4]
listcopy = [n for n in list]
print(listcopy) # [1, 2, 3, 4]

list_squares = [n * n for n in list]
print(list_squares) # [1, 4, 9, 16]

even_list = [n for n in list if n % 2 == 0]
print(even_list) # [2, 4]

pairs = [[x, y] for x in [1, 2] for y in [3, 4]]
print(pairs) # [[1, 3], [1, 4], [2, 3], [2, 4]]

# set

num_list = [1, 2, 3, 4, 5]
num_set = {n for n in num_list}
print(num_set) # {1, 2, 3, 4, 5}

set_squares = {n * n for n in num_set}
print(set_squares) #{1, 4, 9, 16, 25}


num_dict = {n:n for n in num_list}
print(num_dict) #{1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

dict_squares = {f'squares of {n}': n*n for n in num_list}
print(dict_squares)

#Generator

gen = (n for n in range(5))
print(gen)  # <generator object <genexpr> at 0x000001D865E20EE0>

for g in gen:
    print(g)