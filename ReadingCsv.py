import csv
import os



os.chdir('/Users/gshanmu2/Documents/python/Mouser/')

fields = []
rows = []


with open("/Users/gshanmu2/Documents/python/Mouser/Test1.csv") as f:

#1. creating the object
    csvreader = csv.reader(f)

#2. extracting fields

    fields = next(csvreader)

#3.
    # print(reader)
    for row in csvreader:
        rows.append(row)
    print(rows)

    print('Field names are:' + ', '.join(field for field in fields))


print("Total no. of rows: %d"%(csvreader.line_num))

print('\nFirst 1 rows are:\n')
for row in rows[:1]:
   for col in row:
       print("%10s"%col),print('\n')