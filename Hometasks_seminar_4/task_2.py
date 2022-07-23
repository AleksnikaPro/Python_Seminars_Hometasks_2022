# 2.Задайте натуральное число N. Напишите программу, которая составит список
#  простых множителей числа N.

import os
clear = lambda: os.system('cls')
clear()


number = int(input('Введите число: '))
prime_factors_list = []
factor = 2
while number > 1:
    if number % factor == 0:
        prime_factors_list.append(factor)
        number = number / factor
    else:
        factor += 1
print(prime_factors_list)

