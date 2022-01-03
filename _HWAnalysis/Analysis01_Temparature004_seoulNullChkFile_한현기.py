import csv 
# -*- coding: utf-8 -*-
file = open("./_dataSetGilBut01/seoul.csv" ,"r")
data = csv.reader(file)
Vhead= next(data)
temparatureFileList = []


for i in data :
	temparatureFileList.append(i)
print(len(temparatureFileList))


for i in temparatureFileList :
	if temparatureFileList[-1] =='':
		del temparatureFileList[-1]
	if temparatureFileList[-2] =='':
		del temparatureFileList[-2]
	if temparatureFileList[-3] =='':
		del temparatureFileList[-3]
print(temparatureFileList)
tem= ''.join(temparatureFileList)
file = open("List.csv", "w")
file.write(tem)


file.close()




