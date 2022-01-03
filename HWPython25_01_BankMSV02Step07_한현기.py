
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


'''
submenu=["입금","출금","고객정보확인","고객 탈퇴","종료"]
menu = ["고객번호", "고객이름", "계좌번호", "고객잔액"]
funGetList = ['getId()','getName()','getNumber()','getBalance()']
# --------------------------------------------------------------
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
#=====================================================================================================================================================================
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


		for idx in range(len(self.AccDtoList)):
			print(dooObj.AccDtoList[idx].getId(),dooObj.AccDtoList[idx].getName(),dooObj.AccDtoList[idx].getNumber(),dooObj.AccDtoList[idx].getBalance())
		
		print("-"*60)
		print(f"총 인원수 :{len(dooObj.AccDtoList)} 은행장고: {dooObj.AccDtoList[idx].bankBalance}") 
		print("-"*60)
#====================================================================================================================================================
	def customInfo(self):
		userInput=input("고객 번호 입력[5번: 종료  /  0번: 고객List  /  9번: 고객가입] :")
		try:
			self.customChk(userInput)
		except:
			if userInput=="5":
				print("^시스템을 종료합니다.")
				exit()
			elif userInput=="0":
				self.customSel()
			elif userInput=="9":
				self.customIns()
			else:
				
				print("해당 고객 번호가 없습니다  ")

#====================================================================================================================================================
	def customIns(self):
		tempNewCustom =[0,0,0,0]
		addId=int(self.AccDtoList[len(self.AccDtoList)-1].getId()[4:])+1
		userId='{0:0>3}'.format(str(addId))
		addNum= int(self.AccDtoList[len(self.AccDtoList)-1].getNumber()[8:])+1
		userNumber = '{0:0>3}'.format(str(addNum))
		print(self.AccDtoList[len(self.AccDtoList)-1].getId()[:4]+userId,self.AccDtoList[len(self.AccDtoList)-1].getNumber()[:-3]+userNumber)
		vname = input("고객이름:")
		vBalance = input("초기입금:")
		tempNewCustom[0]=self.AccDtoList[len(self.AccDtoList)-1].getId()[:4]+userId
		tempNewCustom[1]=vname
		tempNewCustom[2]=self.AccDtoList[len(self.AccDtoList)-1].getNumber()[:-3]+userNumber
		tempNewCustom[3]=vBalance
	
		print(tempNewCustom)
		self.AccDtoList.append(AccountV01DTO(self.tempNewCustom[0],self.tempNewCustom[1],self.tempNewCustom[2],self.tempNewCustom[3]))
		AccountV01DTO.bankBalance+=int(self.tempNewCustom[3])
		print(f'{tempNewCustom[0]} 가입확인')

		file1 = open("./_dataSet03Bank/BankMSDB01.txt",'a')
		tempWrite=','.join(tempNewCustom)+'\n'
		file1.write(tempWrite)
		file1.close()
#====================================================================================================================================================
	def customChk(self,userInput):
		
			for idx in range(len(self.AccDtoList)):
				if self.AccDtoList[idx].getId()==userInput:
					idxChk=idx; break


		
			print("-"*60)		
			print(f"\t{self.AccDtoList[idxChk].getName()}님 계좌")
			print("-"*60)
			print(f"\t{menu[0]}: {self.AccDtoList[idxChk].getId()}")
			print(f"\t{menu[1]}: {self.AccDtoList[idxChk].getName()}")
			print(f"\t{menu[2]}: {self.AccDtoList[idxChk].getNumber()}")
			print(f"\t{menu[3]}: {self.AccDtoList[idxChk].getBalance()}")
			print("-"*60)
				
					
			while True:
				print("\t<<<선택하세요>>>")
				for idx in range(len(submenu)):
					print(f"\t{idx+1}.{submenu[idx]}")
				userInput2=input(">>선택:")
				if userInput2=="5":
					break
				elif userInput2=="3":
					for idx in range(len(self.AccDtoList)):
						if self.AccDtoList[idx].getId()==userInput:
							idxChk=idx
							print("-"*60)
							print(f"\t{menu[0]}: {self.AccDtoList[idxChk].getId()}")
							print(f"\t{menu[1]}: {self.AccDtoList[idxChk].getName()}")
							print(f"\t{menu[2]}: {self.AccDtoList[idxChk].getNumber()}")
							print(f"\t{menu[3]}: {self.AccDtoList[idxChk].getBalance()}")
							print("-"*60)
				elif userInput2 =="4":
					self.customDel(idxChk)
				else:
					print("해당 고객 번호가 없습니다  ")

#====================================================================================================================================================
	def customDel(self,idx,userInput):
		print("고객탈퇴를 선택하셨습니다.")
		inputid = input("고객 번호 확인:")
		if inputid == userInput :
			AccountV01DTO.bankBalance-= int(self.AccDtoList[idx].getBalance()) # 누적액을 뺴줘야함.
			delCustom = self.AccDtoList.pop(idx) 
			

			print(f"\n\t{delCustom.getName()} 회원 탈퇴 성공" ,end="\n")
			print("-"*60)

			file = open("./_dataSet03Bank/BankMSDB01.txt",'r')
			data = file.readlines()
			file = open("./_dataSet03Bank/BankMSDB01.txt",'w')
			del data[idx]
			file.writelines(data)
			file.close()
			return True
		else:
			print("고객정보가 일치 하지 않습니다.")
			return False


	
#====================================================================================================================================================
dooObj = AccountV01DAO()

dooObj.DBset()
dooObj.customSel()


while True:
	dooObj.customInfo()






















