# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводит пользователь через пробел.

import os
clear = lambda: os.system('cls')
clear()

def get_list_of_elements(arg_1: int, arg_2: int):
    list1 = [int(i)for i in range(arg_1, arg_2 + 1)]
    return list1

def get_list_of_indices(arg_1: list):
    list2 = [int(i) for i in arg_1]
    return list2

def multiplication_result(arg_1: list, arg_2: list):  
    mult_operation = 1
    for i in arg_1:   
        mult_operation *= elements[i]
    return mult_operation


number1 = int(input('Введите число: '))
number2 = -number1
elements = get_list_of_elements(number2, number1)
print(f'Заданный список элементов {elements}')

element_position = (input('Введите через пробел позиции элементов, которые хотите перемножить: '))
position_list = element_position.split()
indices = get_list_of_indices(position_list)
print(f'Список позиций элементов: {indices}')

final_result = multiplication_result(indices, elements)
print(f'Произведение элементов на указанных позициях: {final_result}')  