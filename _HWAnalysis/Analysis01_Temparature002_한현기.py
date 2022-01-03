import csv 

file = open("./_dataSetGilBut01/seoul.csv" ,"r")
data = csv.reader(file)
Vhead= next(data)

for i in data : 
	print(i)