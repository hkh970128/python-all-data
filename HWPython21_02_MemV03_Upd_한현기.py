
import sys
from os import write


menu    = ['1. 회원가입', '2. 로그인', '3. 회원목록', '4. 회원수정',  '5. 회원탈퇴','9. 메뉴종료']
itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
menuChk = []
userList = []
temp = []
temp2 = []
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
        print('='*90)
        for i in line:
            print("{0:^7}".format(i), end='')
        print()
        print('='*90)
        print()
        print(f"현재 회원수는 {len(line)}명입니다")


		




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
        print("qwdqwd")
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

    if len(line) ==0:
        print()
    else:    
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
            if (memList[1] ==PW) :
                print()
                print("\t\t로그인 상태 입니다.")
            else :
                print("\t\t패스워드 확인하세요.")
        else:
        	print("\t\t아이디 확인하세요.")
		

        
#-------------------------------------이제 사용 x	
def memList():
	print("\t\t","^Member List !")

	if len(userList)==0:
		print()
		print("{0:>25}".format("먼저 회원가입해주세요"))
		print()
	else:
		print('='*70)
		for a in itemList:
			print("{0:^7}".format(a), end='')
		print()
		print('='*70)
		print()
		for x in userList:
			for y in x:
				print("{0:^7}".format(y), end='')
			print()
	print()


#-------------------------------------------------------------------업데이트
def memUpd():

	try : 
		file =open("MemV03.txt","r")
		line = file.readlines()

		if not line :
			raise FileNotFoundError()
	except FileNotFoundError :
		print("{0:>25}".format("먼저 회원가입해주세요!!"))
		

	finally:
		file.close()
	if len(line) ==0:
		print()
	else :
		ID= input("\t\t아이디를 입력하세요\n")
		PW= input("\t\t패스워드를 입력하세요\n")
		chkMem=0
		for idx in range(len(line)):
			memList = line[idx].split(",") # 원본데이터를  memlist 에 담음
			if ID == memList[0]:
				chkMem=1
				chkIdx=idx
				break
		if chkMem==1:
			if PW==memList[1]:
			
				for x in range(1,len(itemList)):
				
					ans = input(itemList[x] + '를 수정하시겠습니까? Y/N : ')
					if ans.upper() == 'Y':
						
						memList[x] = input("\t\t입력해주세요 :")

				print(memList)
				line[chkIdx] = ",".join(memList)

				Mem = "".join(line)
				file=open("MemV03.txt","w")
				file.write(Mem)

				print('회원 수정이 완료되었습니다.')

				file.close()
			
				
				print()
				print()
			elif PW!=memList[1]:
				print("{0:>25}".format("비번확인"))
				print()
				print()
		elif ID != memList[0]:
			print("{0:>25}".format("아이디 확인"))
			print()
			print()

#--------------------------------------------------------------------------------회원삭제
def memDel():
	temp=[]
	try : 
		file =open("MemV03.txt","r")
		line = file.readlines()

		if not line :
			raise FileNotFoundError()
	except FileNotFoundError :
		print("{0:>25}".format("먼저 회원가입해주세요!!"))
	
		
	finally:
		file.close()
	if len(line) ==0:
		print()
	else:	
	   
		ID= input("\t\t아이디를 입력하세요\n")
		PW= input("\t\t패스워드를 입력하세요\n")
		chkMem=0
		for idx in range(len(line)):
			memList = line[idx].split(",") # 원본데이터를  memlist 에 담음
			if ID == memList[0]:
				chkMem=1
				break
		if chkMem==1:
			if PW==memList[1]:
			
				del line[idx]
			
				print("{0:>25}".format("탈퇴 성공"))
				print(f"현재 회원수는 {len(line)}명입니다")
				file=open("MemV03.txt","w")
			
				Mem = "".join(line)
				file.write(Mem)
				file.close()
			
				
				print()
				print()
			elif PW!=memList[1]:
				print("{0:>25}".format("비번확인"))
				print()
				print()
		elif ID != memList[0]:
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
	else :
		print("다시선택하세요")
		continue
    

    