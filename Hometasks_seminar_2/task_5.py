
# 5. Реализуйте алгоритм перемешивания списка.

import os
clear = lambda: os.system('cls')
clear()
import random

def shuffle_list(new_list: list):
    random.shuffle(new_list)
    return new_list

list = [18, 12, 5, 11, 10, 3]
print(f'Исходный список {list}')
print(f'Перемешанный список {shuffle_list(list)}')


#______________________________________________________

# def fill_list(arg_1: int):
#     my_list = []
#     for index in range(arg_1):
#         my_list.append(random.randint(0, 30))
#     return my_list

# def shuffled_list(arg_1: list):
#     for i in range(len(arg_1)-1, 0, -1):
#         j = random.randint(0, i + 1)
#         arg_1[i], arg_1[j] = arg_1[j], arg_1[i]
#     print(f'Перемешанный список: {arg_1}')

# number = int(input('Задайте длину списка: '))
# filled_list = fill_list(number)
# print(f'Исходный список: {filled_list}')
# shuffled_list(filled_list)
