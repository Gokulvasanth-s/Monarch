import csv
import pandas as pd
import os

os.chdir('/Users/gshanmu2/Documents/python/Mouser/')


# reading two csv files

data1 = pd.read_csv('Test1.csv')
data2 = pd.read_csv('digikey_price.csv')

data2["ManufacturerPartNumber"] = data2["ManufacturerPartNumber"].astype(int).astype(str)
data2[git "Qty_Req"] = data2["Qty_Req"].astype(float).astype(int)
output = pd.merge(data1, data2, on='ManufacturerPartNumber',how='right')

print(output)
print(data1.info())
print(data2.info())