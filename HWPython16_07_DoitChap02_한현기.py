score =[80,75,55]
sum = score[0]+score[1]+score[2]
print(sum/3)



#-----------
num=int(input("숫자를 넣어주세요"))
if num % 2 == 0:
	print("짝수입니다")
else :
	print("홀수입니다")


#-----------
pin = "881120-1068234"

print(pin[:6]) 
print(pin[7:])  
if pin[7] == '1' or pin[7] == '3' :
	print("남자입니다")
elif pin[7] == '2' or pin[7] == '4' :
	print("여자입니다")
'''
sort 하고 reverse


sort(reverse=True)

