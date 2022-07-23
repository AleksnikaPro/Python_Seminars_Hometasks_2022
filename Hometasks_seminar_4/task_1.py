# 1.Вычислить число c заданной точностью d

# Пример:

# - при d = 0.001, π = 3.141.    10^{-1} ≤ d ≤10^{-10}


import os
clear = lambda: os.system('cls')
clear()
import math
from math import pi

def get_count(number: float):#  определяем количество знаков после запятой в заданной точности
    number_conversion = str(number)
    if '.' in number_conversion:
        return abs(number_conversion.find('.') - len(number_conversion)) - 1
    else:
        return 0

number_pi = pi
print(f'Число Pi: {pi}')
given_accuracy = input('Введите точность, которую нужно определить, по образцу 0.001: ')
accuracy_count = get_count(given_accuracy)
print(f'Число Pi c заданной точностью {given_accuracy}: {round(math.pi, accuracy_count)}')


 


# = get_given_accuracy_pi(number, s)
# 

# def get_given_accuracy_pi(number):
#     result = 
#     return result




# print(abs(s.find('.') - len(s)) - 1)
# result = round(math.pi, given_accuracy)
# print(result)