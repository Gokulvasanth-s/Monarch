import requests, json
import subprocess
import sys
import os
import csv
from pip._vendor.distlib.compat import raw_input


#read input file


#1 Convert input CSV to Jsofn

os.chdir("/Users/gshanmu2/Documents/python/Mouser")





#1. OAUTH2: 

authorize_url = "https://api.digikey.com/v1/oauth2/authorize"
token_url = "https://api.digikey.com/v1/oauth2/token"


#callback url specified when the application was defined
callback_uri = "https://monarchele.com"

#test_api_url = "https://api.digikey.com/Search/v3/Products/GJM1555C1H6R0CB01D"

#client (application) credentials - located at apim.byu.edu
client_id='AydtcTOo0tgZ0v7usYt0PstlPZQQVNjH'
client_secret='D8uzqMc26bA0mrvR'


#step A - simulate a request from a browser on the authorize_url - will return an authorization code after the user is
# prompted for credentials.

authorization_redirect_url = authorize_url + '?response_type=code&client_id=' + client_id + '&redirect_uri=' + callback_uri + '&scope=openid'

print("go to the following url on the browser and enter the code from the returned url: ")
print("---  " + authorization_redirect_url + "  ---")
authorization_code = raw_input('code: ')
print(authorization_code)

# step I, J - turn the authorization code into a access token, etc
#data = {'grant_type': 'authorization_code', 'code': authorization_code, 'redirect_uri': callback_uri}

data = {'grant_type': 'authorization_code', 'code': authorization_code, 'redirect_uri': callback_uri, 'client_id': client_id, 'client_secret': client_secret}
print("requesting access token")
#access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False, auth=(client_id, client_secret))
access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False)

print(access_token_response)

print("response")
print(access_token_response.headers)
print('body: ' + access_token_response.text)


# we can now use the access_token as much as we want to access protected resources.
tokens = json.loads(access_token_response.text)
access_token = tokens['access_token']
print("access token: "+access_token)

api_call_headers = {'Authorization': 'Bearer ' + access_token,'X-DIGIKEY-Client-Id': 'AydtcTOo0tgZ0v7usYt0PstlPZQQVNjH'}



# READ INPUT FILE

os.chdir("/Users/gshanmu2/Documents/python/Mouser")

with open("/Users/gshanmu2/Documents/python/Mouser/Test1.csv") as f:
    reader = csv.reader(f)
    # print(reader)
    next(reader)
    data = []
    for row in reader:
        data.append(row)
    print(data)

# FORMAT THE REQUEST AND SEND TO DIGIKEY USING OAUTH2

digikey_price = []
output = []


#format output:


for i in range(len(data)):
    #print(data[i][0])
    test_api_url = "https://api.digikey.com/Search/v3/Products/{}".format(data[i][0])
    #print(test_api_url)
    api_call_response = requests.get(test_api_url, headers=api_call_headers, verify=False)
    res = api_call_response.json()
    print(res)

    Avail_qty = res['AlternatePackaging']
    #print(Avail_qty)
    #print(type(Avail_qty))

    for item in Avail_qty:
        min_qty = item['MinimumOrderQuantity']

        if min_qty == 1:
            Digikey_qty_avail = item['QuantityAvailable']

    #print(Avail_qty)
    #print(type(Avail_qty))
    prices = res['StandardPricing']

    req_qty = int(data[i][1])
    #print("req_qty: "+str(req_qty))

    for price in prices:
        #print(price["BreakQuantity"])
        '''
        if price["BreakQuantity"] > req_qty:
            print("{},{}".format(req_qty,price['UnitPrice']))
            digikey_price.append(price['UnitPrice'])
            break

        '''

        if req_qty >= price["BreakQuantity"]:
            #print("{},{},{}".format(req_qty,price["BreakQuantity"], price['UnitPrice']))
            digikey_price.append(price['UnitPrice'])
    output.append(("{},{},{},{}".format(data[i][0], data[i][1], digikey_price[-1],Digikey_qty_avail)))

print(list(output))

#list to nested list
temp = []
'''
for elm in output:
    temp2 = elm.split(', ')
    temp.append((temp2))

#print(temp)

outputnl  = []

for elm in temp:
    temp3 = []
    for e in elm:
        temp3.append(e)
    outputnl.append(temp3)

print(outputnl)

'''


outputnl = []


for i in output:
   string_i = str(i)
   string_stp = string_i.strip("[]'")
   #print(string_stp)
   x  = string_stp.split(',')
   outputnl.append(x)




#print("output_nested_list: "+str(output_nested_list))
#write to csv

os.chdir('/Users/gshanmu2/Documents/python/Mouser/')

fields = ['ManufacturerPartNumber', 'Qty_Req', 'Digikey_unit_price']


filename = "digikey_price.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(outputnl)

print(outputnl[0])

print(outputnl[0][1])








