'''1.1~10까지 합 
   2.1~10홀수 합 
   3.짝수합

'''
sum =0
for i in range(1,11) :
	sum +=i
print("1~10까지 합=",+sum)


sum = 0
for i in range(1,11,2) :
	sum +=i
print("1~10까지 홀수합=%d"%sum)


sum = 0
for i in range(0,11,2) :
	sum +=i
print("1~10까지 짝수합=%d"%sum)

	
	