import csv

def read_csv(file_name,file_data):
    file_data=[]
    file= open(file_name, mode='r')
    reader = csv.reader(file)
    for row in reader:
        file_data.append(row)


read_csv('people.csv',poeple)
print(people)
