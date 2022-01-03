menu = ['1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
menuChk = ['1','2','3','9']
memList = []
temp = []


while True :

	print("\n====================메뉴선택==============================")
	print(' '.join(menu))
	print("==========================================================",end="\n")

	num=int(input("	메뉴의 번호를 선택해 주세요 :"))
#  회원 가입 --------------------------------------------
	if num == 1:
		print("\t\t가입\n")
		for i in range(len(itemList)) :
			temp.append(input("{}   :".format (itemList[i])))
		memList.append(temp)
		temp = []
		print("{}\n".format(memList),end=" ")
		print("현재 학생 수는 :{}".format(len(memList)))
	elif num ==2:
		print("\t\t",menu[1],"알고리즘 Chk")
#  회원 목록 --------------------------------------------
	elif num ==3:
		print("\t\t^member List !\n")
		print("="*60)

		for i in range(len(itemList)) :
			print(itemList[i],end='\t')
		print()
		print("="*60)

		for i in range(len(memList)) :
			print('\t'.join(memList[i]),end='\n')
		print()
		print("-"*60)
#  회원 종료 --------------------------------------------
	elif num==9: 
		print("\t\t",menu[3])
		break
	else :
		print("\t\t다시 선택하세요")
