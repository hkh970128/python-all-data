import csv
file = open('./../_dataSet01\emp2.csv','r')
emp_csv = csv.reader(file)
emp = list(emp_csv)

job,job1 = input(" MANAGER, SALESMAN 검색할 직업을 입력하세요").split(",")



print("----------------------------------------------")

for i in range(len(emp)):
	
	if emp[i][2] == job.strip() or emp[i][2] ==job1.strip() :
		print("이름:{}\t 직업{}\t급여:{} ".format(emp[i][1],emp[i][2],emp[i][5]))
print("----------------------------------------------")