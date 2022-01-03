#HWPython02_11_ifPractice4DoitChk03_한현기
#돈이 3000이상 이거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어가라.
#money 변스에 금액입력 /카드 변수에 true false 입력받는다.



money = int(input("돈 확인 "))
card = bool(input("카드 확인 true or false"))
if money >= 3000 or card  :
	print("택시타라")
else : 
	print("걸어가라")
