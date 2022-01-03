
vid = 'Orange'
vPwd = '1234'


vid1 = input("아이디 입력하세요")
vPwd1 =input("비밀번호 입력하세요")


if vid ==vid1 :
	if vPwd ==vPwd1 :
		print("Orange 님 로그인 성공")

	elif  vid != vid1 :		
			print("id 확인하세요")
	elif  vPwd != vPwd1 :
			print("pwd 확인하세요")
else :
	print("Orange 님 로그인 실패")