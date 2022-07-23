# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт 
# сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import os
# clear = lambda: os.system('cls')
# clear()
# import random

# def fill_list(arg_1: int):
#     new_list = []
#     for index in range(arg_1):
#         new_list.append(random.randint(0, 10))
#     return new_list


# def elements_summ(arg_1: list):
#     summ = 0
#     index = 0
#     for index in range(len(arg_1)):
#         if index % 2 == 1:
#             summ += arg_1[index]
#     return summ        

# number = int(input('Задайте длину списка: '))
# filled_list = fill_list(number)
# print(f'Исходный список: {filled_list}')
# final_result = elements_summ(filled_list)
# print(f'Сумма элементов списка, стоящих на нечётной позиции: {final_result}')



import os
clear = lambda: os.system('cls')
clear()
import random

def fill_list(arg_1: int):
    new_list = []
    for index in range(arg_1):
        new_list.append(random.randint(0, 10))
    return new_list


def elements_summ(arg_1: list):
    summ = 0
    i = 0    
    for i in range(1, len(arg_1), 2):
       summ += arg_1[i]
       i += 1
    return summ        

number = int(input('Задайте длину списка: '))
filled_list = fill_list(number)
print(f'Исходный список: {filled_list}')
final_result = elements_summ(filled_list)
print(f'Сумма элементов списка, стоящих на нечётной позиции: {final_result}')
