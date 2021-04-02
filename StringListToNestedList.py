

l = [['GJM1555C1H6R0CB01D,15,0.085'], ['CC0402KRX5R6BB105,30,0.08']]


temp = []


for i in l:
   string_i = str(i)
   string_stp = string_i.strip("[]'")
   print(string_stp)
   x  = string_stp.split(',')
   temp.append(x)

print(temp[0][0])



