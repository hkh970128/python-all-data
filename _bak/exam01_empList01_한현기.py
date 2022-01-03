# exam01_empList01.py
'''
01 파일 오픈
_dataSet01\emp2.csv 
02 . read
03 type Chk

'''

import csv

file = open('./../_dataSet01\emp2.csv','r')

emp_csv = csv.reader(file)
print(type(emp_csv))
print(emp_csv)
for empList in emp_csv :
	print(empList)