
# 5. Реализуйте алгоритм перемешивания списка.

import os
clear = lambda: os.system('cls')
clear()
import random

def shuffle_list(new_list):
    random.shuffle(new_list)
    return new_list

list = [18, 12, 5, 11, 10, 3]
print(f'Исходный список {list}')
print(f'Перемешанный список {shuffle_list(list)}')

