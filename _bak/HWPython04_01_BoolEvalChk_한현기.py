money = int(input("돈 확인 "))
card = eval(input("카드 확인 True or False"))
if money >= 3000 or card  :
	print("택시타라")
else : 
	print("걸어가라")
print(type(card))
