import csv

def csv_reader():
    
    print('Список всех контактов:\n')
    with open('phonebook_2.csv', mode='r', encoding='utf-8', newline='') as r_file:
        reader = csv.reader(r_file)
        for row in reader:
            print(row)
            
            
        


