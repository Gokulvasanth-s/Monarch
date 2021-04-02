#importing the Request library

import requests
import os
import csv
import json
from queue import *




#1 Convert input CSV to Jsofn

os.chdir("/Users/gshanmu2/Documents/python/Mouser")


with open("/Users/gshanmu2/Documents/python/Mouser/Test1.csv") as f:
  reader = csv.reader(f)
  # print(reader)
  next(reader)

  data = []

  for row in reader:
    # print(row)
    global mnf_partno
    mnf_partno = row[0]


#2 Create POST BODY

    data.append(
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
    #print(data)


with open("input.json", "w") as jsonfile:
  json.dump(data, jsonfile, indent=4)
#print(jsonfile)
jsonfile.close()



#3 Open Json File and Insert Json Object into Queue from File


os.chdir('/Users/gshanmu2/Documents/python/Mouser/')
data = json.load(open('input.json'))
q=Queue()
for i in range(len(data)):
        q.put(data[i])




# 4. api endpoint

URL = "https://api.mouser.com/api/v1/search/keyword?apiKey=bfad76ba-7837-4d46-86d0-036fe7cd00c7"

# defining param dict for the parameter to be sent
'''
PARAMS = {
  "SearchByKeywordRequest": {
    "keyword": "CC0402KRX5R6BB105",
    "records": 0,
    "startingRecord": 0,
    "searchOptions": "string",
    "searchWithYourSignUpLanguage": "string"
  }
    }
    
    '''

HEADER =  {
  'Content-Type': 'application/json',
  'version': '1',
  'Cookie': 'ASP.NET_SessionId=wu2c4jlto2fnl0fqhykikbdn'
}

# 5. sending get request and saving the response as response object

#r = requests.get(url = URL, params = PARAMS)

while not q.empty():
  PARAMS = q.get()
  global qn
  qn = (PARAMS['SearchByKeywordRequest']['qty_Needed'])
  r = requests.post(url=URL, json=PARAMS, headers=HEADER, verify=False, timeout=3)
  data = r.json()
  #print(data)
  number_of_results = data['SearchResults']['NumberOfResult']
  PARTS = data['SearchResults']['Parts']
  #print(PARTS)

  for value in PARTS:
     print(value['ManufacturerPartNumber'])
     print()
 # for i in range(1,number_of_results+1):
 #      PARTS = data['SearchResults']['Parts']


  '''
  #print(data)
  #print((data['SearchResults']['NumberOfResult']))
  #print((data['SearchResults']['Parts']))

  price_break = dict()
  l = []


  for i in data['SearchResults']['Parts']:
    #print(i['Availability'] )
    #print(i['Manufacturer'])
    #print(i['MouserPartNumber'])
    #print(i['ProductAttributes'])
    #for j in i['ProductAttributes']:
    # print(j['AttributeName'])
    #print(i['PriceBreaks'])
        for j in i['PriceBreaks']:
            Qty_range = (j['Quantity'])
            Price = (j['Price'])
            price_break[Qty_range] = Price

            if int(Qty_range) <= int(qn):
                # print("Qty_range:"+str(Qty_range))
                #print(Price)
                #price_break[Qty_range] = Price
                #l.append("{},{},{},{},{},{},{}".format(i['ManufacturerPartNumber'], i['MouserPartNumber'], i['Availability'],i['Manufacturer'], Price, Qty_range, qn))
                print("{},{},{},{},{},{}".format(i['ManufacturerPartNumber'], i['MouserPartNumber'], i['Availability'],i['Manufacturer'], price_break, qn))
                #print(l)
  #vprint(l[-1])
  #print(price_break)
  #print(list(price_break.values())[-1])
  #print(l)

#print(price_break[100])


# extracting data in json format

#data = r.json()

#print(data)

#print(status)
#print(r.headers)
'''
f.close()