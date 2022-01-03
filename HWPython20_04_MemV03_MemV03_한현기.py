
import sys
from os import write


menu    = ['1. 회원가입', '2. 로그인', '3. 회원목록', '4. 회원수정',  '5. 회원탈퇴','9. 메뉴종료']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
menuChk = []
userList = []
temp = []
for x in menu:
	menuChk.append(x[0])
def memTitle():
	print('='*40,'메뉴선택','='*40)
	print(menu)
	print('='*90)

def menuSelect():
	num=0
	num=input("\t""메뉴의 번호를 입력해주세요 :")
	if num in menuChk:
		return num
	else:
		print("\t""다시 입력해주세요")
		print()
def memSel():
    try : 
        file =open("MemV03.txt","r")
        line = file.readlines()

        if not line :
            raise FileNotFoundError()

    except FileNotFoundError :
        print("{0:>25}".format("먼저 회원가입해주세요!!"))
    else :
        print('='*50)
        for i in line:
            print("{0:^7}".format(i), end='')
        print()
        print('='*50)
        print()


		




def memIns():
    temp=[]	
    
    try:
        file =open("MemV03.txt","r")
    except FileNotFoundError :
        file=open("MemV03.txt","a")
        file=open("MemV03.txt","r")      
    finally :
        line = file.readlines()
        file.close()
    chk=0
    print("\t\t","^SignUp !")
    print("MemV03.txt","r")
    
    for signUp in itemList :
        print()
        print(f"\t{signUp:<10}:",end="") 
        templist=input()
        temp.append(templist)
        
        print()
    for i in range(len(line)):
        liness=line[i].split(",")[0]
        if liness ==temp[0]:
            chk=1
    if chk==0 :
        file=open("MemV03.txt","a")
        a="\n"
        Mem03 = ",".join(temp)+a
        file.write(Mem03)
        file.close()
        print(f"현재 회원수는 {len(line)+1}명입니다")
    elif chk==1 :
        print("중복 아이디가 있습니다.")
        
    
		
# ----------------------------------
def memLog():
	
    chkMem=0
    chkIdx=-1
    try : 
        file =open("MemV03.txt","r")
        line = file.readlines()

        if not line :
            raise FileNotFoundError()

    except FileNotFoundError :
        print("{0:>25}".format("먼저 회원가입해주세요!!"))
    else:
        print("\t\t","^Log in !")
        print()
    finally:
        file.close()

        
    ID= input("\t\t아이디를 입력하세요\n")
    PW= input("\t\t패스워드를 입력하세요\n")
    chkMem = -1
    for idx in range(len(line)) :
        memList = line[idx].split(",")
        
        if ID == memList[0]:
            
            chkMem=1
            chkIdx=idx
            break
    
    
    if chkMem==1 :
        if (line[chkIdx][1] ==PW) :
            print("로그인 상태 입니다.")
        else :
            print("패스워드 확인하세요.")
    else:
        print("아이디 확인하세요.")
		

        
	
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
		memSel()
#회원수정------------------------------------------------------------------------
	elif int(nums) == 4:
		memUpd()
#회원탈퇴----------------------------------------------------------------------------------------------
	elif int(nums) == 5:
		memDel()
	elif int(nums) == 9:
		memExit()
		break
    

    