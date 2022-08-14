import csv

def csv_writer(data: list):
   
    with open('phonebook_2.csv', mode='a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)   
        writer.writerow(data)
    

 

  