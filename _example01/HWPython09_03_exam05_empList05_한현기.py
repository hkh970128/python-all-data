#사원중 보너스가 0이 아닌 리스트 출력 HWPython09_03_exam05_empList05_한현기




#
import csv

file = open('./../_dataSet01\emp2.csv','r')

emp_csv = csv.reader(file)
emp = list(emp_csv)

 

print("보너스 확인")
print("--------------------------------------------")
for i in range(len(emp)) :
	if emp[i][6] !='0' :
		print("이름:{}\t 보너스:{} ".format(emp[i][1],emp[i][6]))
print("--------------------------------------------")
