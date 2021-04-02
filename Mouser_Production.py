#1. importing the Request library

import requests
import os
import csv
import pandas as pd
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

#3. create POST body payload
payload = []

for row in input:
    payload.append(
        {
            "SearchByKeywordRequest": {
                "keyword": row[0],
                "records": 0,
                "startingRecord": 0,
                "searchOptions": "string",
                "searchWithYourSignUpLanguage": "string",
                "qty_Needed": row[1]
            }
        }
    )

#print(payload)
'''
for p in payload:
    print(p)
'''

# 4. END point

URL = "https://api.mouser.com/api/v1/search/keyword?apiKey=bfad76ba-7837-4d46-86d0-036fe7cd00c7"

HEADER =  {
  'Content-Type': 'application/json',
  'version': '1',
  'Cookie': 'ASP.NET_SessionId=wu2c4jlto2fnl0fqhykikbdn'
}

results = []

for p in payload:
    r = requests.post(url=URL, json=p, headers=HEADER, verify=False, timeout=3)
    response = r.json()
    results.append(response)
#print(result)
#print(type(result))

print(input)
#print(type(input))



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

#print(outputnl)



fields = ['ManufacturerPartNumber', 'Qty_Req', 'Mouser_unit_price','Mouser_Availability']


filename = "Mouser_price.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(outputnl)


#data1 = pd.read_csv('Test1.csv')
#data2 = pd.read_csv('digikey_price.csv')

'''

for i in range(len(result)):
    dict = print(result[i])
    print(type(result[i]))
#print(result['SearchResults']['Parts'])

#5. Retrive data from result Json
    #format needed mfg_part_no,
#print(len(result))


'''


#pandas







