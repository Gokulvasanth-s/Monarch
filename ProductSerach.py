import json
import requests
import os
from pip._vendor.distlib.compat import raw_input
import csv

WORKING_DIR = '/Users/gshanmu2/Documents/python/Mouser'
INCOMING_FILE = '/Users/gshanmu2/Documents/python/Mouser/Incoming/Test1.csv'
OUTPUT_DIR = '/Users/gshanmu2/Documents/python/Mouser/Output'
#1 Change Directory

os.chdir(WORKING_DIR)



#2. Function Call

def Digikey():

    print("Entering Digikey")


    # 1. OAUTH2:

    authorize_url = "https://api.digikey.com/v1/oauth2/authorize"
    token_url = "https://api.digikey.com/v1/oauth2/token"

    # callback url specified when the application was defined
    callback_uri = "https://monarchele.com"

    # test_api_url = "https://api.digikey.com/Search/v3/Products/GJM1555C1H6R0CB01D"

    # client (application) credentials - located at apim.byu.edu
    client_id = 'AydtcTOo0tgZ0v7usYt0PstlPZQQVNjH'
    client_secret = 'D8uzqMc26bA0mrvR'

    # step A - simulate a request from a browser on the authorize_url - will return an authorization code after the user is
    # prompted for credentials.

    authorization_redirect_url = authorize_url + '?response_type=code&client_id=' + client_id + '&redirect_uri=' + callback_uri + '&scope=openid'

    print("go to the following url on the browser and enter the code from the returned url: ")
    print("---  " + authorization_redirect_url + "  ---")
    authorization_code = raw_input('code: ')
    print(authorization_code)

    # step I, J - turn the authorization code into a access token, etc
    # data = {'grant_type': 'authorization_code', 'code': authorization_code, 'redirect_uri': callback_uri}

    data = {'grant_type': 'authorization_code', 'code': authorization_code, 'redirect_uri': callback_uri,
            'client_id': client_id, 'client_secret': client_secret}
    print("requesting access token")
    # access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False, auth=(client_id, client_secret))
    access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False)

    print(access_token_response)

    print("response")
    print(access_token_response.headers)
    print('body: ' + access_token_response.text)

    # we can now use the access_token as much as we want to access protected resources.
    tokens = json.loads(access_token_response.text)
    access_token = tokens['access_token']
    print("access token: " + access_token)

    api_call_headers = {'Authorization': 'Bearer ' + access_token,
                        'X-DIGIKEY-Client-Id': 'AydtcTOo0tgZ0v7usYt0PstlPZQQVNjH'}

    # READ INPUT FILE

    os.chdir(WORKING_DIR)

    with open(INCOMING_FILE) as f:
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

    # format output:

    for i in range(len(data)):
        # print(data[i][0])
        test_api_url = "https://api.digikey.com/Search/v3/Products/{}".format(data[i][0])
        # print(test_api_url)
        api_call_response = requests.get(test_api_url, headers=api_call_headers, verify=False)
        res = api_call_response.json()
        print(res)

        Avail_qty = res['AlternatePackaging']
        # print(Avail_qty)
        # print(type(Avail_qty))

        for item in Avail_qty:
            min_qty = item['MinimumOrderQuantity']

            if min_qty == 1:
                Digikey_qty_avail = item['QuantityAvailable']

        # print(Avail_qty)
        # print(type(Avail_qty))
        prices = res['StandardPricing']

        req_qty = int(data[i][1])
        # print("req_qty: "+str(req_qty))

        for price in prices:
            # print(price["BreakQuantity"])
            if req_qty >= price["BreakQuantity"]:
                # print("{},{},{}".format(req_qty,price["BreakQuantity"], price['UnitPrice']))
                digikey_price.append(price['UnitPrice'])
        output.append(("{},{},{},{}".format(data[i][0], data[i][1], digikey_price[-1], Digikey_qty_avail)))

    print(list(output))

    # list to nested list
    temp = []
    outputnl = []

    for i in output:
        string_i = str(i)
        string_stp = string_i.strip("[]'")
        # print(string_stp)
        x = string_stp.split(',')
        outputnl.append(x)

    # print("output_nested_list: "+str(output_nested_list))
    # write to csv

    os.chdir('/Users/gshanmu2/Documents/python/Mouser/')

    fields = ['ManufacturerPartNumber', 'Qty_Req', 'Digikey_unit_price','Digikey-Avail']

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

    f.close()


def Mouser():
    print("Entering Mouser")

    input = []
    output = []
    Mouser_price = []

    with open(INCOMING_FILE) as f:

        # a) create csv reader object
        csvreader = csv.reader(f)

        # b) fields
        field = next(csvreader)

        # c) rows
        for row in csvreader:
            input.append(row)

    # 3. create POST body payload
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

    # print(payload)
    '''
    for p in payload:
        print(p)
    '''

    # 4. END point

    URL = "https://api.mouser.com/api/v1/search/keyword?apiKey=bfad76ba-7837-4d46-86d0-036fe7cd00c7"

    HEADER = {
        'Content-Type': 'application/json',
        'version': '1',
        'Cookie': 'ASP.NET_SessionId=wu2c4jlto2fnl0fqhykikbdn'
    }

    results = []

    for p in payload:
        r = requests.post(url=URL, json=p, headers=HEADER, verify=False, timeout=3)
        response = r.json()
        results.append(response)
    # print(result)
    # print(type(result))

    print(input)
    # print(type(input))

    for i in range(len(input)):
        Req_mfg_partno = input[i][0]
        Req_Qty = input[i][1]

        dict_list = results[i]

        # print(type(dict_list))
        # print(dict_list)
        # print(dict_list['Errors'])
        # print(dict_list['SearchResults'])
        # print(dict_list['SearchResults']['NumberOfResult'])
        Number_of_result = dict_list['SearchResults']['NumberOfResult']
        # print(dict_list['SearchResults']['Parts'])

        for number in range(Number_of_result):
            Mouser_Availability = dict_list['SearchResults']['Parts'][number]['Availability']
            Rec_manu_partno = dict_list['SearchResults']['Parts'][number]['ManufacturerPartNumber']
            Price_break = dict_list['SearchResults']['Parts'][number]['PriceBreaks']
            print(Rec_manu_partno)
            # print(type(Price_break))
            print(Req_Qty)

            print(Price_break)

            for price in Price_break:
                print(price['Quantity'])
                print(price['Price'])

                if int(Req_Qty) >= price['Quantity']:
                    # print("{},{},{}".format(req_qty,price["BreakQuantity"], price['UnitPrice']))
                    Mouser_price.append(price['Price'])
            if Rec_manu_partno == Req_mfg_partno:
                output.append(("{},{},{},{}".format(Rec_manu_partno, Req_Qty, Mouser_price[-1], Mouser_Availability)))

        # Get Unit Price

        # output.append(("{},{}".format(input[i][0], input[i][1])))

    outputnl = []

    for i in output:
        # print(output[1])
        string_i = str(i)
        x = string_i.split(',')
        outputnl.append(x)

    # print(outputnl)

    fields = ['ManufacturerPartNumber', 'Qty_Req', 'Mouser_unit_price', 'Mouser_Availability']

    filename = "Mouser_price.csv"

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)

        # writing the data rows
        csvwriter.writerows(outputnl)

    # data1 = pd.read_csv('Test1.csv')
    # data2 = pd.read_csv('digikey_price.csv')

    f.close()

def MergeFiles():

    print("Entering MergeFiles")

    os.chdir(OUTPUT_DIR)

    print(os.getcwd())


    fields = []
    Input_rows = []
    Digikey_rows = []
    Mouser_rows = []

    output_1 = []
    output_2 = []

    # Reading input-Csv file

    with open(INCOMING_FILE) as f:

        # 1. creating the object
        csvreader = csv.reader(f)

        # 2. extracting fields

        fields = next(csvreader)

        # 3.
        # print(reader)
        for row in csvreader:
            Input_rows.append(row)
        # print(Input_rows)

        # print('Field names are:' + ', '.join(field for field in fields))

    # print("Total no. of rows: %d"%(csvreader.line_num))

    # read Digikey_price CSV

    with open("/Users/gshanmu2/Documents/python/Mouser/Digikey_price.csv") as d:

        # 1. creating the object
        csvreader_d = csv.reader(d)

        # 2. extracting fields

        fields_d = next(csvreader_d)

        # 3.
        # print(reader)
        for row in csvreader_d:
            Digikey_rows.append(row)
        # print(Digikey_rows)

        # print('Field names are:' + ', '.join(field for field in fields_d))

    # print("Total no. of rows: %d"%(csvreader.line_num))

    # read Mouser_price CSV

    with open("/Users/gshanmu2/Documents/python/Mouser/Mouser_price.csv") as m:

        # 1. creating the object
        csvreader_m = csv.reader(m)

        # 2. extracting fields

        fields_m = next(csvreader_m)

        # 3.
        # print(reader)
        for row in csvreader_m:
            Mouser_rows.append(row)
        # print(Mouser_rows)

        # print('Field names are:' + ', '.join(field for field in fields_d))

    # print("Total no. of rows: %d"%(csvreader.line_num))

    # digikey_forLoop

    # for first value matches with any value in the column then append the list here

    for i in range(len(Input_rows)):
        # print(Input_rows[i][0])
        for j in range(len(Digikey_rows)):
            # print(Digikey_rows[j][0])
            if (Input_rows[i][0] == Digikey_rows[j][0]):
                # print('{},{}'.format(Input_rows[i],Digikey_rows[i]))
                temp_list = Input_rows[i] + Digikey_rows[i]
                # print(temp_list)
                output_1.append(temp_list)

            if (Input_rows[i][0] == Mouser_rows[j][0]):
                temp_list2 = temp_list + Mouser_rows[i]
                # print(temp_list2)
                output_2.append(temp_list2)
    # print(output_2)

    # print(output_1)

    fileds_final = ['Req_ManufacturerPartNumber', 'Req_qty', 'Digikey_ManufacturerPartNumber', 'Digikey_Res_qty',
                    'Digikey_unitPrice', 'Digikey_Availibility', 'Mouser__ManufacturerPartNumber', 'Mouser_Res_qty',
                    'Mouser_unit_Price', 'Mouser_availibility']

    filename = "Result.csv"

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fileds_final)

        # writing the data rows
        csvwriter.writerows(output_2)


    f.close()
    d.close()

#3 Call Main

Digikey()
Mouser()
MergeFiles()