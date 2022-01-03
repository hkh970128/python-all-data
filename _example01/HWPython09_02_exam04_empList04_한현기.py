#HWPython09_02_exam04_empList04_한현기
import csv

file = open('./../_dataSet01\emp2.csv','r')

emp_csv = csv.reader(file)
emp = list(emp_csv)

money = input("검색할 연봉 하한값 입력하세요")
maxmoney = input("검색할 연봉 상한값 입력하세요")

print("연봉 2500~3000인 사원 리스트")
print("--------------------------------------------")
for i in range(len(emp)) :
	if emp[i][5] >= money and emp[i][5] <= maxmoney :
		print("이름:{} 연봉:{} ".format(emp[i][1],emp[i][5]))
print("--------------------------------------------")
