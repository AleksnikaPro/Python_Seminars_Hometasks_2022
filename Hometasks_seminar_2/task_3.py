    
# 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на 
# экран их сумму.
    
#     *Пример:*
    
#     - Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37, 4: 2.44, 5: 2.49, 6: 2.52}
#      сумма = 14.07
 
import os
clear = lambda: os.system('cls')
clear()

def number_sequence(n: int):
    result = 0
    count = 0
    summ = 0
    for i in range(1, n + 1):
        result = (1 + 1/i)**i
        count += 1
        print(f' {count} число последовательности: {round(result, 2)}')
        summ += result
    print(f'Сумма чисел последовательности: {round(summ, 2)}')
number = int(input('Введите число: '))
number_sequence(number)
