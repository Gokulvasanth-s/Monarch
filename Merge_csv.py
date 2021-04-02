#Read input CSV

import csv
import os


os.chdir('/Users/gshanmu2/Documents/python/Mouser/Output/')

fields = []
Input_rows = []
Digikey_rows = []
Mouser_rows = []

output_1 = []
output_2 = []


#Reading input-Csv file

with open("/Users/gshanmu2/Documents/python/Mouser/Test1.csv") as f:

#1. creating the object
    csvreader = csv.reader(f)

#2. extracting fields

    fields = next(csvreader)

#3.
    # print(reader)
    for row in csvreader:
        Input_rows.append(row)
    # print(Input_rows)

    #print('Field names are:' + ', '.join(field for field in fields))


#print("Total no. of rows: %d"%(csvreader.line_num))



#read Digikey_price CSV

with open("/Users/gshanmu2/Documents/python/Mouser/Digikey_price.csv") as d:

#1. creating the object
    csvreader_d = csv.reader(d)

#2. extracting fields

    fields_d = next(csvreader_d)

#3.
    # print(reader)
    for row in csvreader_d:
        Digikey_rows.append(row)
    #print(Digikey_rows)

    #print('Field names are:' + ', '.join(field for field in fields_d))


#print("Total no. of rows: %d"%(csvreader.line_num))



# read Mouser_price CSV

with open("/Users/gshanmu2/Documents/python/Mouser/Mouser_price.csv") as m:

#1. creating the object
    csvreader_m = csv.reader(m)

#2. extracting fields

    fields_m = next(csvreader_m)

#3.
    # print(reader)
    for row in csvreader_m:
        Mouser_rows.append(row)
    #print(Mouser_rows)

    #print('Field names are:' + ', '.join(field for field in fields_d))


#print("Total no. of rows: %d"%(csvreader.line_num))


#digikey_forLoop

#for first value matches with any value in the column then append the list here

for i in range(len(Input_rows)):
    #print(Input_rows[i][0])
    for j in range(len(Digikey_rows)):
        #print(Digikey_rows[j][0])
        if (Input_rows[i][0] == Digikey_rows[j][0]):
            #print('{},{}'.format(Input_rows[i],Digikey_rows[i]))
            temp_list = Input_rows[i] + Digikey_rows[i]
            #print(temp_list)
            output_1.append(temp_list)

        if (Input_rows[i][0] == Mouser_rows[j][0]):

            temp_list2 = temp_list + Mouser_rows[i]
            #print(temp_list2)
            output_2.append(temp_list2)
#print(output_2)

#print(output_1)

fileds_final = ['Req_ManufacturerPartNumber', 'Req_qty', 'Digikey_ManufacturerPartNumber', 'Digikey_Res_qty','Digikey_unitPrice', 'Digikey_Availibility','Mouser__ManufacturerPartNumber','Mouser_Res_qty','Mouser_unit_Price','Mouser_availibility']

filename = "Result.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fileds_final)

    # writing the data rows
    csvwriter.writerows(output_2)

#read_input

'''
fileds_id = ['Req_ManufacturerPartNumber','Req_qty','Res_ManufacturerPartNumber_Digikey','Res_qty_Digikey','Digikey_unitPrice','Digikey_Availibility']

filename = "Input_digikey_price_merged.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fileds_id)

    # writing the data rows
    csvwriter.writerows(output_1)
    


'''


f.close()
d.close()