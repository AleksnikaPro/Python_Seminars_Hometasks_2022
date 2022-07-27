# 1.Напишите программу, удаляющую из текста все слова, содержащие "абв".


def delete_find_item(param_1: str):
    list = []
    for item in param_1:
        if find_item not in item:
            list.append(item)
            result = " ".join(list)
    return result


text = 'абв голоабвдная муха селаабв на варенье'
find_item = 'абв'
splitted_text = text.split()
final_result = delete_find_item(splitted_text)
print(f'Исходный текст: {text}')
print(f'Текст после удаления "{find_item}": {final_result}')