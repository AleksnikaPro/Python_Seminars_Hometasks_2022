# 3.Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.


# import os
# clear = lambda: os.system('cls')
# clear()
# import random


# def fill_list(arg_1: int):
#     new_list = []
#     for index in range(arg_1):
#         new_list.append(random.randint(1, 6))
#     return new_list


# def non_repeating_elements(arg_1: list):
#     result_list = []
#     for i in arg_1:
#         if i not in result_list:
#             result_list.append(i)
#     return result_list

# number = int(input('Задайте длину списка: '))
# filled_list = fill_list(number)
# print(f'Исходный список: {filled_list}')
# final_result = non_repeating_elements(filled_list)
# print(f'Cписок неповторяющихся элементов: {final_result}')
# _________________________________________________

# Вариант первый

# numbers = [1, 2, 2, 3, 3, 4, 5]

# def get_unique_numbers(numbers):
#     list_of_unique_numbers = []
#     unique_numbers = set(numbers)

#     for number in unique_numbers:
#         list_of_unique_numbers.append(number)

#     return list_of_unique_numbers

# print(get_unique_numbers(numbers))
# ____________________________________

# numbers = [1, 2, 2, 3, 3, 4, 5]
# unique_numbers = list(set(numbers))
# print(unique_numbers)
# _________________________________________

# Вариант 2
# numbers = [20, 20, 30, 30, 40]

# def get_unique_numbers(numbers):
#     unique = []

#     for number in numbers:
#         if number in unique:
#             continue
#         else:
#             unique.append(number)
#     return unique

# print(get_unique_numbers(numbers))
# ________________________________________







