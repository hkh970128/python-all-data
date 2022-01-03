import csv
file = open('./../_dataSet01\StuDataSet02.csv','r')
stu_csv = csv.reader(file)


stu = list(stu_csv)

print("="*50)
for i in stu :
	
	num = i[2] # 주민번호
	phone = i[4] # 통신사
	num1= num[:2]# 00
	num2=list(num[:1]) #9
	
	
	
	for j in num2 :
		if j =="0" :
			birth ='20' +num1
		else :
			birth = '19' + num1
		age = 2021-int(birth)
	
	if age>=30 and phone.strip(" ") =="sk" :
		print("이름 :"+i[1]+" 나이: "+str(age))
	
print("="*50)		



