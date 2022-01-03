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


'''
menu = ["고객번호", "고객이름", "계좌번호", "고객잔액"]

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


