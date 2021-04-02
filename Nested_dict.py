import os
import csv
import json
from queue import *

#2. Read the input file


os.chdir("/Users/gshanmu2/Documents/python/Mouser")

input = []
output = []
Mouser_price = []


with open("/Users/gshanmu2/Documents/python/Mouser/Test1.csv") as f:

    #a) create csv reader object
    csvreader = csv.reader(f)

    #b) fields
    field = next(csvreader)

    #c) rows
    for row in csvreader:
        input.append(row)

results = json.load(open('nested.json'))

#print(input)
#print(result)

#get the part no

for i in range(len(input)):
    Req_mfg_partno = input[i][0]
    Req_Qty = input[i][1]


    dict_list = results[i]

    #print(type(dict_list))
    #print(dict_list)
    #print(dict_list['Errors'])
    #print(dict_list['SearchResults'])
    #print(dict_list['SearchResults']['NumberOfResult'])
    Number_of_result = dict_list['SearchResults']['NumberOfResult']
    #print(dict_list['SearchResults']['Parts'])

    for number in range(Number_of_result):
        Mouser_Availability    = dict_list['SearchResults']['Parts'][number]['Availability']
        Rec_manu_partno = dict_list['SearchResults']['Parts'][number]['ManufacturerPartNumber']
        Price_break = dict_list['SearchResults']['Parts'][number]['PriceBreaks']
        print(Rec_manu_partno)
        #print(type(Price_break))
        print(Req_Qty)

        print(Price_break)

        for price in Price_break:
            print(price['Quantity'])
            print(price['Price'])

            if int(Req_Qty) >= price['Quantity']:
                # print("{},{},{}".format(req_qty,price["BreakQuantity"], price['UnitPrice']))
                Mouser_price.append(price['Price'])
        if Rec_manu_partno == Req_mfg_partno:
            output.append(("{},{},{},{}".format(Rec_manu_partno, Req_Qty, Mouser_price[-1],Mouser_Availability)))



    #Get Unit Price

    #output.append(("{},{}".format(input[i][0], input[i][1])))

outputnl = []

for i in output:
    #print(output[1])
    string_i = str(i)
    x = string_i.split(',')
    outputnl.append(x)

print(outputnl)



fields = ['ManufacturerPartNumber', 'Qty_Req', 'Mouser_unit_price']


filename = "Mouser_price.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(outputnl)

