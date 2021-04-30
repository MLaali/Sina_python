import csv

def read_csv(file_name,file_data):
    file_data.clear()
    file= open(file_name, mode='r')
    reader = csv.reader(file)
    for row in reader:
        file_data.append(row)

poeple=[]
read_csv('people.csv',poeple)
print(len(poeple))
