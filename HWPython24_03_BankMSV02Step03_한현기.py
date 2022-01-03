import csv

'''
-------------------------------------------
실습 ] BankMSV01Step01 ] DTO Chk--------------------------- 

01. BankMSV01DTO.py

menu = ["고객번호", "고객이름", "계좌번호", "고객잔액"]

## class AccountV01DTO:

01. 객체 변수 : customId / customName / customNumbr / customBalance
	-> 생성자에 의해 setting

02. bankBalance = 100000; # 클래스 변수 

03. getter / setter 생성

03 . getter / setter 
'''
menu = ["고객번호", "고객이름", "계좌번호", "고객잔액"]
funGetList = ['getId()','getName()','getNumber()','getBalance()']
class AccountV01DTO ():
	bankBalance = 100000
	def __init__(self,customId,customName,customNumbr,customBalance):
		self.customId=customId
		self.customName=customName
		self.customNumbr=customNumbr
		self.customBalance=customBalance
	#getter
	def getId(self):
		return self.customId
	def getName(self) :
		return self.customName
	def  getNumber(self):
		return self.customNumbr
	def  getBalance(self):
		return self.customBalance
	#setter
	def setId(self,customId):
		self.customId = customId
	def setName(self,customName) :
		self.customName =customName
	def setNumber(self,customNumbr):
		self.customNumbr =customNumbr
	def setBalance(self,customBalance):
		self.customBalance = customBalance
#==================================================================================================================================
class AccountV01DAO() :
	

	def __init__(self):
		self.AccDtoList =[]
		self.tempLise = []
		
	def DBset(self):
		try:
			file = open("./_dataSet03Bank/BankMSDB01.txt",'r')
		except FileNotFoundError:
			file = open("./_dataSet03Bank/BankMSDB01.txt",'w')
			file = open("./_dataSet03Bank/BankMSDB01.txt",'r')
		finally:
			bankFile = file.readlines()
			file.close()
		for i in range(len(bankFile)):
			self.temList = bankFile[i].strip().split(",")
			self.AccDtoList.append(AccountV01DTO(*self.temList))
			AccountV01DTO.bankBalance+=int(self.AccDtoList[i].getBalance())
#-----------------------------------------------------------------------------------------------------------------------------------------------			
	def customSel(self):

		print("-"*60)
		print("\t\t은행관리 프로그램 V01")
		print("-"*60)
		print(' '.join(menu))
		print("-"*60)	
		
		for i in range(len(self.AccDtoList)):
			print(dooObj.AccDtoList[i].getId(),dooObj.AccDtoList[i].getName(),dooObj.AccDtoList[i].getNumber(),dooObj.AccDtoList[i].getBalance())
		
		print("-"*60)
		print(f"총 인원수 :{len(dooObj.AccDtoList)} 은행장고: {dooObj.AccDtoList[i].bankBalance}") 
		print("-"*60)
		print()
	def customInfo(self):
		
			num=int(input("고객 번호 입력 [5번 : 종료 / 0번 : 고객list / 9번   : 고객가입] "))
			if num ==5 :
				print("시스템을 종료합니다.")
				exit()
			elif num ==0:
				dooObj.customSel()
			elif num == 9:
				print("\t\t 고객 가입 Algorithm Chk")
			else :
				print("다시 입력하세요")
			



	

dooObj = AccountV01DAO()
dooObj.DBset()
dooObj.customSel()
while True:
	dooObj.customInfo()





















'''
for i in range(len(dooObj.AccDtoList)):
	print(dooObj.AccDtoList[i].getId(),dooObj.AccDtoList[i].getName(),dooObj.AccDtoList[i].getNumber(),dooObj.AccDtoList[i].getBalance())
print()
print(f"총 인원수 :{len(dooObj.AccDtoList)} 은행장고: {dooObj.AccDtoList[i].bankBalance}") 



		

#==================================================================================
def DBset():
	try:
		file = open("./_dataSet03Bank/BankMSDB01.txt",'r')
		
	except FileNotFoundError:
		file = open("./_dataSet03Bank/BankMSDB01.txt",'w')
		file = open("./_dataSet03Bank/BankMSDB01.txt",'r')
	finally:
		DBdata = file.readlines()
		
		file.close()

	for x in range(len(DBdata)):
		DBdata[x]= DBdata[x].strip().split(",")
	return DBdata


#dooObj = AccountV01DAO()
#dooObj.DBset()
#dooObj.AccDtoList 개수  >> 7개
#dooObj.AccDtoList[0]getId() >> CUST001



file = open("./_dataSet03Bank/BankMSDB01.txt",'r')
DBdata = file.readlines()
print("-"*60)
print(' '.join(menu))
print("-"*60)
for i in range(len(DBdata)):
	print(DBdata[i])
print("-"*60)
for i in range(len(DBdata)):
	int(DBdata[i][-1])
	hap += DBdata[i][-1]
print(f'현재인원{len(DBdata)}  {hap}현재 시드머니')





		for outer in range(len(self.AccDtoList)):
			for inner in range(len(funGetList)):
				funget="self.AccDtoList[outer]"+funGetList[inner]
'''




		