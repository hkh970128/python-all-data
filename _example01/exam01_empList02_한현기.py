# exam01_empList01_한현기.py
'''
01 파일 오픈
_dataSet01\emp2.csv 
02 . read
03 type Chk

'''

import csv

file = open('./../_dataSet01\emp2.csv','r')

emp_csv = csv.reader(file)
emp = list(emp_csv)
print("-------------------------------")
print("사원명\t\t연봉")
print("-------------------------------")
for i in range(len(emp)) :
	print(emp[i][1],"\t\t" , emp[i][5],)