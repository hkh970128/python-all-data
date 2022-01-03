import csv 
# -*- coding: utf-8 -*-
file = open("./_dataSetGilBut01/seoul.csv" ,"r")
data = csv.reader(file)
Vhead= next(data)
temList = list(data)
tmp1=0
tmp2=0
tmp3=0
for row in temList : 
	
	
	if row[-1] =="":
		tmp1+= 1
	if row[-2] =="":
		tmp2+= 1
	if row[-3] == "" :
		tmp3+= 1


print("총데이터 : {}".format(len(temList)))
print("최고기온 : {}".format(tmp1))
print("최저기온 : {}".format(tmp2))
print("평균기온 : {}".format(tmp3))