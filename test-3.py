import json
import os
import csv

os.chdir('/Users/gshanmu2/Documents/python/Mouser/')
data = json.load(open('format-lid2.json'))


print((data['SearchResults']['NumberOfResult']))

value = data['SearchResults']['NumberOfResult']

for i in range(1,value):
    print(i)

#print((data['SearchResults']['Parts']))


#print(type(data['SearchResults']['Parts']))


price_break = dict()
'''
for i in data['SearchResults']['Parts']:
    #print(i['Availability'] )
    #print(i['Manufacturer'])
    #print(i['MouserPartNumber'])
    #print(i['ProductAttributes'])
    #for j in i['ProductAttributes']:
    #    print(j['AttributeName'])
    #print(i['PriceBreaks'])
    for j in i['PriceBreaks']:
        Qty = (j['Quantity'])
        Price = (j['Price'])
        price_break[Qty] = Price
    print("{},{},{},{}".format(i['MouserPartNumber'],i['Availability'],i['Manufacturer'],i['PriceBreaks']))

print(price_break[100])


'''
qn=15

for i in data['SearchResults']['Parts']:
    #print(i['Availability'] )
    #print(i['Manufacturer'])
    #print(i['MouserPartNumber'])
    #print(i['ProductAttributes'])
    #for j in i['ProductAttributes']:
    #    print(j['AttributeName'])
    #print(i['PriceBreaks'])
        for j in i['PriceBreaks']:
            Qty_range = (j['Quantity'])
            Price = (j['Price'])
            price_break[Qty_range] = Price
            if int(Qty_range) <= int(qn):
                print("Qty_range:"+str(Qty_range))
                print(Price)
        #print(price_break)
                print("{},{},{},{},{},{}".format(i['ManufacturerPartNumber'],i['MouserPartNumber'],i['Availability'],i['Manufacturer'],Price,qn))
#print(price_break[100])








