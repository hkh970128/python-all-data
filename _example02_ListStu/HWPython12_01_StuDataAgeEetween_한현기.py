import csv
file = open('./../_dataSet01\StuDataSet02.csv','r')
stu_csv = csv.reader(file)


stu = list(stu_csv)

min_age= int(input("검색할 연령(하한) 을 입력하세요: "))
max_age= int(input("검색할 연령(상한) 을 입력하세요: "))
print("="*50)
for i in stu :
	
	num = i[2] # 주민번호
	phone = i[4] # 통신사
	phone_num = i[3] # 핸드폰 번호
	num1= num[:2]# 00
	num2=list(num[:1]) #9
	
	
	for j in num2 :
		if j =="0" :
			birth ='20' +num1
		else :
			birth = '19' + num1
		age = 2022-int(birth) # 한국나이 2021(현재년도)+1 
		
	if max_age>=age>=min_age  :
		print("이름 :"+i[1]+" 나이:"+str(age)+" 통신사:"+i[4]+" 전화번호:"+i[3])
	
print("="*50)
