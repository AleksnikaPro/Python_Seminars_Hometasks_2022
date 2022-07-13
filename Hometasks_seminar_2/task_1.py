# 1. Напишите программу, которая принимает на вход вещественное число и показывает 
# сумму его цифр.
    
    # *Пример:*
    
    # - 6782 -> 23
    # - 0,56 -> 11

import os
clear = lambda: os.system('cls')
clear()

def summ_of_digits(number):
    summ = 0
    result = str(number).replace('.', '')
    for i in result:
        summ += int(i)
    return summ
num = input('Введите число: ')
print(f'Сумма цифр введенного числа: {summ_of_digits(num)}')





