# 1.Напишите программу, удаляющую из текста все слова, содержащие "абв".

# ИСХОДНЫЙ КОД

# def delete_find_item(param_1: str):
#     list = []
#     for item in param_1:
#         if find_item not in item:
#             list.append(item)
#             result = " ".join(list)
#     return result


# text = 'абв голоабвдная муха селаабв на варенье'
# find_item = 'абв'
# splitted_text = text.split()
# final_result = delete_find_item(splitted_text)
# print(f'Исходный текст: {text}')
# print(f'Текст после удаления "{find_item}": {final_result}')


def delete_find_item(param_1: str):
    list = [item for item in param_1 if find_item not in item]
    result = " ".join(list)
    return result

text = 'абв голоабвдная муха селаабв на варенье'
find_item = 'абв'
splitted_text = text.split()
final_result = delete_find_item(splitted_text)
print(f'Исходный текст: {text}')
print(f'Текст после удаления "{find_item}": {final_result}')

#_____________________________________________
# def delete_find_item(param_1: list):
#     find_item = 'абв'
#     return find_item not in param_1

# text = 'абв голоабвдная муха селаабв на варенье'
# print('Исходный текст:', text)
# splitted_text = text.split()
# res = list(filter(delete_find_item, splitted_text))
# result = " ".join(res)
# print(f'Текст после удаления "абв": {result}')

#_____________________________________________________________

# def delete_find_item(param_1: list):
#     find_item = 'абв'
#     return find_item not in param_1


# text = ['абв', 'голоабвдная', 'муха', 'селаабв', 'на варенье']
# print('До:', text)
# res = list(filter(delete_find_item, text))
# result = " ".join(res)
# print('После:', result)