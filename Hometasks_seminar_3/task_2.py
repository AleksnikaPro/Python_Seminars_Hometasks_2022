# 2.Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import os
clear = lambda: os.system('cls')
clear()
import random

def fill_list(arg_1: int):
    new_list = []
    for index in range(arg_1):
        new_list.append(random.randint(0, 10))
    return new_list


def elements_multiplicaton(param_1: list):
    i = 0
    j = len(param_1) - 1
    result = []
    while i < len(param_1) / 2:
        result.append(param_1[i] * param_1[j])
        i += 1
        j -= 1
    return result


number = int(input('Задайте длину списка: '))
filled_list = fill_list(number)
print(f'Исходный список: {filled_list}')
new_list = []
new_list = elements_multiplicaton(filled_list)
print(f'Произведение пар чисел исходного списка: {new_list}')



