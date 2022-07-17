# 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def get_binary_number(param_1: int):
    result = ' '
    while param_1 > 0:
        result += str(param_1 % 2)
        param_1 = param_1 // 2
    return result[::-1]

number = int(input('Введите десятичное число: '))
final_result = get_binary_number(number)
print(f'Десятичное число {number} в двоичной системе счисления равно: {final_result}')
