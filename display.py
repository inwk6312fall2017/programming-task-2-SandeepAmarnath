import csv
with open('Crime.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        print (row[0])