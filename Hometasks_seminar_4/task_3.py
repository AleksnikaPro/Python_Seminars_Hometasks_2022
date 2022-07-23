# 3.Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.


import os
clear = lambda: os.system('cls')
clear()
import random


def fill_list(arg_1: int):
    new_list = []
    for index in range(arg_1):
        new_list.append(random.randint(1, 6))
    return new_list


def non_repeating_elements(arg_1: list):
    result_list = []
    for i in arg_1:
        if i not in result_list:
            result_list.append(i) 
    return result_list

number = int(input('Задайте длину списка: '))
filled_list = fill_list(number)
print(f'Исходный список: {filled_list}')
final_result = non_repeating_elements(filled_list)
print(f'Cписок неповторяющихся элементов: {final_result}')





