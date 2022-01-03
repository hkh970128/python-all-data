import csv

file = open('./../_dataSet01\emp2.csv','r')

emp_csv = csv.reader(file)
emp = list(emp_csv)



name = input("검색할 사원명을 입력하세요 :").split(",")
print("보너스 확인")
print("--------------------------------------------")
for i in range(len(emp)) :
	if name == emp[i][1] :
		print("{}급여는 {}입니다.".format(emp[i][1],emp[i][5]))




print("--------------------------------------------")



