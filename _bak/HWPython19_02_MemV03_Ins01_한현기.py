#HWPython19_02_MemV03_Ins01_정승현.py

menu    = ['1. 회원가입', '2. 로그인', '3. 회원목록', '4. 회원수정',  '5. 회원탈퇴','9. 메뉴종료']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
menuChk = []
userList = []
temp = []
for x in menu:
	menuChk.append(x[0])
def memTitle():
	print('='*30,'메뉴선택','='*30)
	print(menu)
	print('='*70)

def menuSelect():
	num=0
	num=input("\t""메뉴의 번호를 입력해주세요 :")
	if num in menuChk:
		return num
	else:
		print("\t""다시 입력해주세요")
		print()




def memIns():
	temp=[]	
	print("\t\t","^SignUp !")
	print()
	for signUp in itemList:
		print(f"\t{signUp:<10}:",end="") 
		templist=input()
		temp.append(templist)
	userList.append(temp)
	f=open("MemV03.txt","w")
	for i in range(len(userList)):
		a=","
		b= "\n"
		for x in range(len(userList[i])):
			data="%s"%userList[i][x]
			f.write(data)
			if x < len(userList[i])-1:
				f.write(a)
		f.write(b)
	
	for vList in userList:
		print(vList)
	print(f"현재 회원수는 {len(userList)}명입니다")	
	print()
		

def memLog():
	temp=[]
	if len(userList)==0:
		print()
		print("{0:>25}".format("먼저 회원가입해주세요"))
		print()
	else:
		print("\t\t","^Log in !")
		print()
		print()
		for signIn in range(2):
			print(f"\t{itemList[signIn]}:",end="")
			templist=input()
			temp.append(templist)
		chkMem=0
		for idx in range(len(userList)):
			if temp[0] == userList[idx][0]:
				chkMem=1
				break
		if chkMem==1:
			if temp[1]==userList[idx][1]:
				print("{0:>25}".format("로그인 성공"))
				print()
				print()
			elif userList[idx][1]!=temp[1]:
				print("{0:>25}".format("비번확인"))
				print()
				print()
		elif temp[0] != userList[idx][0]:
			print("{0:>25}".format("아이디 확인"))
			print()
			print()
	
def memList():
	print("\t\t","^Member List !")
	if len(userList)==0:
		print()
		print("{0:>25}".format("먼저 회원가입해주세요"))
		print()
	else:
		print('='*50)
		for a in itemList:
			print("{0:^7}".format(a), end='')
		print()
		print('='*50)
		print()
		for x in userList:
			for y in x:
				print("{0:^7}".format(y), end='')
			print()
	print()



def memUpd():
	MemChk = 0
	Chkidx = -1
	if len(userList) == 0:
		print('등록된 회원이 없습니다.')
	else :
		ID = input ('ID를 입력하세요.')
		PWD = input('PWD를 입력하세요.')
		for idx in range(len(userList)):
			if ID == userList[idx][0]:
				MemChk = 1
				Chkidx = idx
				break
		if MemChk == 1:
			if (userList[Chkidx][1] ==PWD) :
				print(userList[Chkidx])
				for x in range(1,len(itemList)):
					ans = input(itemList[x] + '를 수정하시겠습니까? Y/N : ')
					if ans.upper() == 'Y':
						vx = input('수정하실' +  itemList[x]  +  '를 입력하세요. : ')
						userList[idx][x] = vx
				print('회원 수정이 완료되었습니다.')
				print(userList[Chkidx])

			else :
					print('PWD를 확인하세요.')
		else :
			print('ID를 확인하세요.')


def memDel():
	temp=[]
	if len(userList)==0:
		print()
		print("{0:>25}".format("먼저 회원가입해주세요"))
		print()
	else:
		print("\t\t","^회원탈퇴")
		print()
		print()
		for signIn in range(2):
			print(f"\t{itemList[signIn]} :",end="")
			templist=input()
			temp.append(templist)
		chkMem=0
		for idx in range(len(userList)):
			if temp[0] == userList[idx][0]:
				chkMem=1
				break
		if chkMem==1:
			if temp[1]==userList[idx][1]:
				print("{0:>25}".format("탈퇴 성공"))
				del userList[idx]
				
				print()
				print()
			elif userList[idx][1]!=temp[1]:
				print("{0:>25}".format("비번확인"))
				print()
				print()
		elif temp[0] != userList[idx][0]:
			print("{0:>25}".format("아이디 확인"))
			print()
			print()



def memExit():
	print("\t""9. 메뉴를 종료합니다")
	print()
	
while True:
	memTitle()
	nums = menuSelect()

#회원가입-------------------------------------------------------------------
	if int(nums) == 1:
		memIns()
		
		
#로그인-----------------------------------------------------------------------------
	elif int(nums) == 2:
		memLog()
			

#회원목록-----------------------------------------------------------------------
	elif int(nums) == 3:
		memList()
#회원수정------------------------------------------------------------------------
	elif int(nums) == 4:
		memUpd()
#회원탈퇴----------------------------------------------------------------------------------------------
	elif int(nums) == 5:
		memDel()
	elif int(nums) == 9:
		memExit()
		break