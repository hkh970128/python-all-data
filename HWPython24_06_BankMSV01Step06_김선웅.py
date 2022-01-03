

# 실습 ] BankMSV01Step01 ] DTO Chk--------------------------- 

# 01. BankMSV01.py

# menu = ["고객번호", "고객이름", "계좌번호", "고객잔액"]

# ## class AccountV01DTO:

# 01. 객체 변수 : customId / customName / customNumbr / customBalance
# 	-> 생성자에 의해 setting

# 02. bankBalance = 100000; # 클래스 변수 

# 03. getter / setter 생성
# + getId
# 	+ getName
# 	+ getNumber
# 	+ getBalance


# 폴더 dataSet03
# ## class AccountV01DAO:

menu = ["고객번호", "고객이름", "계좌번호", "고객잔액"]
submenu=["입금","출금","고객정보확인","고객 탈퇴","종료"]

class AccountV01DTO:
	bankBalance=100000
	def __init__(self,customId,customName,customNumbr, customBalance):
		self.id=customId
		self.name=customName
		self.numbr=customNumbr
		self.balance=customBalance
		
	def getId(self):
		return self.id
	def getName(self):
		return self.name
	def getNumbr(self):
		return self.numbr
	def getBalance(self):
		return self.balance
	
	
	def setID(self, id):
		self.id=id
	def setName(self, name):
		self.name=name
	def setNumbr(self, numbr):
		self.numbr=numbr
	def setBalance(self, balance):
		self.balance=balance

#-------------------------------------------------------------------------------------------------
class AccountV01DAO():
	def __init__(self):
		self.AccDtoList=[]
		self.tempList=[]
# -----------------------------------------------------------------------			
	def DBSet(self):
		try:
			self.file=open("./_dataSet03Bank/BankMSDB01.txt","r")
		except:
			self.file=open("./_dataSet03Bank/BankMSDB01.txt","w")
			self.file=open("./_dataSet03Bank/BankMSDB01.txt","r")
		finally:
			self.bankFile=self.file.readlines()
			self.file.close()
		for idx in range(len(self.bankFile)):
			self.tempList=self.bankFile[idx].strip().split(",")
			self.AccDtoList.append(AccountV01DTO(self.tempList[0],self.tempList[1],self.tempList[2],self.tempList[3]))
			AccountV01DTO.bankBalance+=int(self.AccDtoList[idx].getBalance())
# -----------------------------------------------------------------------		
	def customSel(self):
	
		print(f'{"은행 관리 프로그램 V01":=^52}')
		for x in menu:
			print(f'{x:^12}',end="")
		print()
		print("="*60)
		for i in range(len(self.AccDtoList)):
			print(f"{self.AccDtoList[i].getId():^15}{self.AccDtoList[i].getName():^12}\t{self.AccDtoList[i].getNumbr():^15}{int(self.AccDtoList[i].getBalance()):>11,}")
		print("-"*60)
		print(f"\t총 인원 {len(self.AccDtoList)}명/ 은행잔고 :{AccountV01DTO.bankBalance:,}원")
		print("="*60)


# -----------------------------------------------------------------------		
	def customInfo(self):
		self.userInput=input("고객 번호 입력[5번: 종료  /  0번: 고객List  /  9번: 고객가입] :")
		try:
			self.customChk(self.userInput)
		except:
			if self.userInput=="5":
				print("^시스템을 종료합니다.")
				exit()
			elif self.userInput=="0":
				self.customSel()
			elif self.userInput=="9":
				self.customIns()
			else: 
				print("존재하지 않는 고객 번호입니다.")
				print()

		
		

# ------------------------------------------------------------------------------
	def customIns(self):
		
		self.temp=[0,0,0,0]
		_addId=int(self.AccDtoList[len(self.AccDtoList)-1].getId()[4:]) + 1
		userId="{0:0>3}".format(str(_addId))
		_addNum=int(self.AccDtoList[len(self.AccDtoList)-1].getNumbr()[8:]) + 1
		userNumber="{0:0>3}".format(str(_addNum))
		print(self.AccDtoList[len(self.AccDtoList)-1].getId()[:4]+userId, self.AccDtoList[len(self.AccDtoList)-1].getNumbr()[:-3]+userNumber)
		self.inputName=input("고객이름 :")
		self.inputMoney=input("초기입금 :")
		self.temp[0]=self.AccDtoList[len(self.AccDtoList)-1].getId()[:4]+userId
		self.temp[1]=self.inputName
		self.temp[2]=self.AccDtoList[len(self.AccDtoList)-1].getNumbr()[:-3]+userNumber
		self.temp[3]=self.inputMoney
		print(self.temp)
		self.AccDtoList.append(AccountV01DTO(self.temp[0],self.temp[1],self.temp[2],self.temp[3]))
		AccountV01DTO.bankBalance+=int(self.temp[3])
		print(f"{self.temp[0]} 가입확인")
		self.file=open("./_dataSet03Bank/BankMSDB01.txt", "a")
		tempWrite=",".join(self.temp)+"\n"
		self.file.write(tempWrite)
		self.file.close()
		
# -----------------------------------------------------------------------------------

	def customChk(self,userInput):
		self.userInput=userInput
		for idx in range(len(self.AccDtoList)):
			if self.AccDtoList[idx].getId()==self.userInput:
				idxChk=idx
		
		print("-"*80)		
		print(f"\t{self.AccDtoList[idxChk].getName()}님 계좌")
		print("-"*80)
		print(f"\t{menu[0]}: {self.AccDtoList[idxChk].getId()}")
		print(f"\t{menu[1]}: {self.AccDtoList[idxChk].getName()}")
		print(f"\t{menu[2]}: {self.AccDtoList[idxChk].getNumbr()}")
		print(f"\t{menu[3]}: {self.AccDtoList[idxChk].getBalance()}")
		print("-"*80)
		while True:
			print("\t<<<선택하세요>>>")
			for idx in range(len(submenu)):
				print(f"\t{idx+1}.{submenu[idx]}")
			self.userInput2=input(">>선택:")
			if self.userInput2=="5":
				break
daoObj= AccountV01DAO()
daoObj.DBSet()
daoObj.customSel()

while True:
	
	daoObj.customInfo()