''' 01money 변수에 true  false 입력받는다

HWPython02_11_ifPractice4DoitChk01_한현기.zip

sample run    money 확인 ex true  false 입력받는다
02money 타입 확인

true 면 택시 아니면 걸어간다
02 
만약에 3000원 이상의돈을 가지고 있으면
택시를 타고 그렇지않으면 걸어가라
03
돈이 3000이상 이거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어가라.
money 변스에 금액입력 /카드 변수에 true false 입력받는다.
'''
money = bool(input("돈 확인 true or false"))

print(type(money))
if money :
	print("택시를 타고 가라")
else :
	print("걸어가")


