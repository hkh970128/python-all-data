import csv 

file = open("./_dataSetGilBut01/seoul.csv" ,"r")
data = csv.reader(file)
data2= next(data)

print(data2)