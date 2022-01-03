menu = ['1. 회원가입', '2. 로그인', '3. 회원목록','4. 회원수정','5. 회원탈퇴', '9. 메뉴종료']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
menuChk = ['1','2','3','9']
memList = []
temp = []



while True :

	print("\n====================메뉴선택=============================================")
	print(' '.join(menu))
	print("=========================================================================",end="\n")

	num=int(input("	메뉴의 번호를 선택해 주세요 :"))
#  회원 가입 --------------------------------------------
	if num == 1:
		print("\t\t가입\n")
		for i in range(len(itemList)) :
			temp.append(input("\t\t{}   :".format (itemList[i])))
		memList.append(temp)
		temp = []
		print("\t\t{}\n\n".format(memList))
		print("\t\t현재 학생 수는 :{}".format(len(memList)))


# 회원 로그인 ---------------------------------------------------------


	elif num ==2:
		chkMem =0 
		chkIdx=-1
		print("log in\n\n")
		if len(memList) == 0 :
			print("회원가입부터 해주세요")
			continue
		
		ID= input("\t\t아이디를 입력하세요\n")
		PW= input("\t\t패스워드를 입력하세요\n")
		for idx in range (len(memList)) :
			if ID ==memList[idx][0]:
				chkMem=1
				chkIdx=idx
				break
		if chkMem==1 :
			if (memList[chkIdx][1] ==PW) :
				print("로그인 상태 입니다.")
			else :
				print("패스워드 확인하세요.")
		else:
			print("아이디 확인하세요.")
			
		
#  회원 목록 --------------------------------------------
	elif num ==3:
		print("\t\t^member List !\n")
		print("="*60)

		for i in range(len(itemList)) :
			print(itemList[i],end=' ')
		print()
		print("="*60)

		for i in range(len(memList)) :
			print('\t'.join(memList[i]),end='\n')
		print()
		print("-"*60)
#  회원 수정 --------------------------------------------
	elif num ==4:
		if len(memList) == 0 :
			print("회원가입부터 해주세요")
			continue
		chkMem =0 
		chkIdx=-1
		ID= input("\t\t아이디를 입력하세요\n")
		PW= input("\t\t패스워드를 입력하세요\n")
		for idx in range (len(memList)) :
			if ID ==memList[idx][0]:
				chkMem=1
				chkIdx=idx
				break
		if chkMem==1 :
			if (memList[chkIdx][1] ==PW) :
				print("{}님은 수정 가능합니다.".format(memList[chkIdx][0]))
				print("수정전 내용 확인:",memList[chkIdx],end='\n\n')
				for i in range(len(itemList)) :
					ch = input("\t\t{}수정 (Y / N) :".format (itemList[i]))
					memList[chkIdx] = []
					temp.append(input("\t\t{}   :".format (itemList[i])))
				memList.append(temp)
				print("수정완료")
		
			else :
				print("패스워드를 확인하세요")
		else:
			print("아이디를 확인하세요")
#  회원 삭제 --------------------------------------------
	elif num ==5:
		if len(memList) == 0 :
			print("회원가입부터 해주세요")
			continue
		chkMem =0 
		chkIdx=-1
		ID= input("\t\t아이디를 입력하세요\n")
		PW= input("\t\t패스워드를 입력하세요\n")
		for idx in range (len(memList)) :
			if ID ==memList[idx][0]:
				chkMem=1
				chkIdx=idx
				break
		if chkMem==1 :
			if (memList[chkIdx][1] ==PW) :
				print("{}님은 삭제되었습니다" .format(memList[chkIdx][0]))
				del(memList[chkIdx])
			else :
				print("패스워드를 확인하세요")
		else:
			print("아이디를 확인하세요")
#  회원 종료 --------------------------------------------
	elif num==9: 
		print("\t\t",menu[5])
		break
	else :
		print("\t\t다시 선택하세요")
