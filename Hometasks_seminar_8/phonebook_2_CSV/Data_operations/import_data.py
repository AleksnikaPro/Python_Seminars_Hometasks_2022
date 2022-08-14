from csv_writer import csv_writer

def import_contact()-> None:
 
    first_name = [input('Введите имя: ')]
    last_name = [input('Введите фамилию: ')]
    phone_number = [input('Введите номер телефона: ')]
    description = [input('Введите описание: ')]
    new_contact = first_name + last_name + phone_number + description
  
    csv_writer(new_contact)
    print('Новый контакт внесен в телефонный справочник!\n')
   