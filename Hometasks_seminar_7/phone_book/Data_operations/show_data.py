from view import view_data

def show_contact_list():
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    view_data('Список всех контактов:\n\n', content)
   











