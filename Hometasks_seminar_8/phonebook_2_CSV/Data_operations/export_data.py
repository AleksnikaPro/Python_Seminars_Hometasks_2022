import csv

def delete_contact()-> None:
   
    # search_result = []
    search_result = ''
    del_contact = input('Введите контакт(имя), который хотите удалить:\n')
    
    filename = 'phonebook_2.csv'
    with open(filename, mode='r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        for contact in reader:
            if del_contact in contact:
                # search_result.append(contact)
                search_result = contact
                print(search_result)

    if search_result != []:
        print(del_contact, ' - найден в списке контактов.')
           

        confirm_word = bool(input('Введите "да", если подтверждаете операцию удаления!\n' 
                                  'Нажмите кнопку Enter, если хотите отменить операцию удаления!\n'))

        if confirm_word:
            
            filename = 'phonebook_2.csv'
            with open(filename, mode='r', encoding='utf-8', newline='') as file:
                reader = csv.reader(file)
                for contact in reader:
                    print(contact)
                    # for find_contact in search_result:
                        # if contact != find_contact:
                    if contact != search_result:
                        with open(filename, mode='w', encoding='utf-8', newline='') as file:
                            writer = csv.writer(file)   
                            writer.writerow(contact)
                            print('Удален контакт: ', del_contact)
                            break
          
        else:
            print(del_contact, '- НЕ удален!\n')
    else: 
        print(del_contact, ' НЕ найден в списке контактов!\n')
          
          



        



