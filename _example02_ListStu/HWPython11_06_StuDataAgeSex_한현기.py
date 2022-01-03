import csv
file = open('./../_dataSet01\StuDataSet02.csv','r')
stu_csv = csv.reader(file)


stu = list(stu_csv)


for i in stu :
	
	num = i[2] # 주민번호
	
	num1= num[:2]# 00
	num2=list(num[:1]) #9
	num3=list(num[7:8]) # 성별 1 3 2
	
	
	for j in num2 :
		if j =="0" :
			birth ='20' +num1
		else :
			birth = '19' + num1
		age = 2021-int(birth)
	if num3[0]=="1" or num3[0]=="3" :
		gender ='남자'
	else :
		gender ='여자'
	print("이름 :"+i[1]+" 나이: "+str(age)+" 성별:"+gender)
	
	
	
	
	