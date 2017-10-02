
import csv
csvFile = open("Crime.csv", "rb")
col1="RUCR_EXT_D"
col2="RUCR"
col3="LOCATION"
mydictionary={col1:[], col2:[], col3:[]}
#csvFile = csv.reader(open("Crime.csv", "rb"))
for row in csvFile:
  mydictionary[col1].append(row[0])
  mydictionary[col2].append(row[1])
  mydictionary[col3].append(row[2])

for row in csvFile:
  col1, col2, col3 = row
  print ("%s: %s, %s" % (col1, col2, col3))