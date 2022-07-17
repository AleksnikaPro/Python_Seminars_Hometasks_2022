    
# 2. Напишите программу, которая принимает на вход число N и выдает набор 
# произведений чисел от 1 до N.
    
#     *Пример:*
    
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import os
clear = lambda: os.system('cls')
clear()

def multiplication(n: int):
    result = 1
    list = []
    for i in range(1, n + 1):
        result *= i
        list.append(result)
        
    return list
number = int(input('Введите число: '))
print(f'Набор произведений чисел от 1 до {number}: {multiplication(number)} ')


