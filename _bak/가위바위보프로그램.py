'''
가위바위보 게임 프로그램 만들기
player는 입력받고 컴퓨터는 랜덤으로 나오게 하기
랜덤 사용법은 아랫글 참조.
젤 윗줄에 improt random 쓰기 [랜덤 숫자 생성 라이브러리 사용]
변수 선언 후에 random.randint(1,3)[1부터 3까지 사이에 정수값 랜덤으로 생성] 넣어주기
random.rand(1,3)하면 1과 3 사의 실수가 나오기 때문에 정수값만 나오도록 randint를 사용
 Com의 가위바위보 정해주는 법
 가위는 1 바위는 2 보는 3
 rn = random.randint(1, 3)
    if rn==1:
        com = '가위'. 
while문과 if문을 이용
종료를 입력했을때 프로그램 종료.
가위, 바위, 보 외에 다른걸 입력했을때 예외처리.
결과 표현은 아래 참조.
com=바위  player=보 is player win
com=보  player=바위 is com win
'''


import random



com =""
while True :
	player = input("\t가위(1) ,바위(2) ,보(3) 중 하나를 입력하세요.종료(4)을 원하시면 종료를 입력하세요\t")
	rn = random.randint(1, 3)
	if rn == 1 :
		com ="가위"
		if player == com:
			print("com=%s  player=%s 비겼습니다." % ("가위" , "가위") )
		elif player == "바위" :
			print("com=%s  player=%s 플레이어가 이겼습니다." % ("가위" , "바위") )
		elif player == "보" :
			print("com=%s  player=%s com가 이겼습니다." % ("가위" , "보") )
	elif rn == 2 :
		com = "바위"
		if player == com :
			print("com=%s  player=%s 비겼습니다." % ("바위" , "바위") )
		elif player == "보" :
			print("com=%s  player=%s 플레이어가 이겼습니다." % ("바위" , "보") )
		elif player == "가위" : 
			print("com=%s  player=%s com가 이겼습니다." % ("바위" , "가위") )
	elif rn ==3 :
		com == "보"
		if player == com :
			print("com=%s  player=%s 비겼습니다." % ("보" , "보") )
		elif player == "가위" :
			print("com=%s  player=%s 플레이어가 이겼습니다." % ("보" , "가위") )
		elif player == "바위" :
			print("com=%s  player=%s com가 이겼습니다." % ("보" , "바위") )
	elif player == "종료" : 
		print("종료합니다")
		break


	