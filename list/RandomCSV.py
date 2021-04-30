import csv
import random

records=900
print("Making %d records\n" % records)

fieldnames=['id','name','vote','city']
writer = csv.DictWriter(open("people.csv", "w"), fieldnames=fieldnames)

names=['Nazanin','Mohammad','Mojtaba','Foujan','Fateme','Melina','Sajede',
       'Hosein','Artemis','MobinaZ','MohammadAmin',
       'Hannane','Zahra','MohammadSaeed','Parmida','Raika',
       'Bahar','Maryam','MobinaH','Parisa']


cities=['Kashan', 'Tabriz', 'Hamdan', 'Rasht']

writer.writerow(dict(zip(fieldnames, fieldnames)))
for i in range(0, records):
  writer.writerow(dict([
    ('id', i),
    ('name', random.choice(names)),
    ('vote', str(random.randint(100,10000))),
    ('city', random.choice(cities))]))
