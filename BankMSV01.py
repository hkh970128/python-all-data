
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
			file=open("./_dataSet03Bank/BankMSDB01.txt","r")
		except:
			file=open("./_dataSet03Bank/BankMSDB01.txt","w")
			file=open("./_dataSet03Bank/BankMSDB01.txt","r")
		finally:
			bankFile=file.readlines()
			file.close()
		for idx in range(len(bankFile)):
			tempList=bankFile[idx].strip().split(",")
			self.AccDtoList.append(AccountV01DTO(tempList[0],tempList[1],tempList[2],tempList[3]))
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
		userInput=input("고객 번호 입력[5번: 종료  /  0번: 고객List  /  9번: 고객가입] :")
		try:
			self.customChk(userInput)
			return
		except:
			if userInput=="5":
				print("^시스템을 종료합니다.")
				exit()
			elif userInput=="0":
				self.customSel()
			elif userInput=="9":
				self.customIns()
			else: 
				print("다시 입력해주세요.")
				print()

		
		

# ------------------------------------------------------------------------------
	def customIns(self):
		
		temp=[0,0,0,0]
		_addId=int(self.AccDtoList[len(self.AccDtoList)-1].getId()[4:]) + 1
		userId="{0:0>3}".format(str(_addId))
		_addNum=int(self.AccDtoList[len(self.AccDtoList)-1].getNumbr()[8:]) + 1
		userNumber="{0:0>3}".format(str(_addNum))
		print(self.AccDtoList[len(self.AccDtoList)-1].getId()[:4]+userId, self.AccDtoList[len(self.AccDtoList)-1].getNumbr()[:-3]+userNumber)
		inputName=input("고객이름 :")
		inputMoney=input("초기입금 :")
		temp[0]=self.AccDtoList[len(self.AccDtoList)-1].getId()[:4]+userId
		temp[1]=inputName
		temp[2]=self.AccDtoList[len(self.AccDtoList)-1].getNumbr()[:-3]+userNumber
		temp[3]=inputMoney
		print(temp)
		self.AccDtoList.append(AccountV01DTO(temp[0],temp[1],temp[2],temp[3]))
		AccountV01DTO.bankBalance+=int(temp[3])
		print(f"{temp[0]} 가입확인")
		file=open("./_dataSet03Bank/BankMSDB01.txt", "a")
		tempWrite=",".join(temp)+"\n"
		file.write(tempWrite)
		file.close()
		
# -----------------------------------------------------------------------------------

	def customChk(self,userInput):
	
		for idx in range(len(self.AccDtoList)):
			if self.AccDtoList[idx].getId()==userInput:
				idxChk=idx
				break
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
			userInput2=input(">>선택:")
			if userInput2=="5":
				print("서브 메뉴를 종료합니다.")
				break
			elif userInput2=="3":
				print("-"*80)		
				print(f"\t{self.AccDtoList[idxChk].getName()}님 계좌")
				print("-"*80)
				print(f"\t{menu[0]}: {self.AccDtoList[idxChk].getId()}")
				print(f"\t{menu[1]}: {self.AccDtoList[idxChk].getName()}")
				print(f"\t{menu[2]}: {self.AccDtoList[idxChk].getNumbr()}")
				print(f"\t{menu[3]}: {self.AccDtoList[idxChk].getBalance()}")
				print("-"*80)
			elif userInput2=="4":
				self.customDel(idxChk, self.AccDtoList[idxChk].getId())
			
			elif userInput2=="1":
				self.deposit(idxChk)
			
			elif userInput2=="2":
				self.withDraw(idxChk)
				
			
#입금=====================================================================================================================================
	def deposit(self, idxChk):
		vMoney=input("입금 금액 확인하세요:")
		if int(vMoney) > 0:
			self.AccDtoList[idxChk].setBalance(str(int(self.AccDtoList[idxChk].getBalance())+int(vMoney)))
			AccountV01DTO.bankBalance+=int(vMoney)
			print(f"고객잔액:{self.AccDtoList[idxChk].getBalance()}")
			print(f"은행잔액:{AccountV01DTO.bankBalance}")
			file=open("./_dataSet03Bank/BankMSDB01.txt", "r")
			bankFile=file.readlines()
			bankFile[idxChk]=bankFile[idxChk].split(",")
			bankFile[idxChk][-1]=str(int(bankFile[idxChk][-1])+int(vMoney))
			bankFile[idxChk]=",".join(bankFile[idxChk])+"\n"
			file=open("./_dataSet03Bank/BankMSDB01.txt", "w")
			file.writelines(bankFile)
			file.close()
		else:
			print("0원 이상 입금하세요")

#출금 ============================================================================================================================
	def withDraw(self, idxChk):
		money=input("출금 금액 확인하세요:")
		if int(money) > 0: # 만약에 0보다 큰값을 입금해야하니까 
			mymoney = int(self.AccDtoList[idxChk].getBalance())
			if int(money) <= AccountV01DTO.bankBalance:
				if int(money) <= mymoney:
					self.AccDtoList[idxChk].setBalance(str(int(self.AccDtoList[idxChk].getBalance())-int(money)))
					AccountV01DTO.bankBalance-=int(money)
					print(f"출금금액:{money}")
					print(f"고객잔액:{self.AccDtoList[idxChk].getBalance()}")
					print(f"은행잔액:{AccountV01DTO.bankBalance}")
					dataList=[]
					file=open("./_dataSet03Bank/BankMSDB01.txt", "r")
					bankFile=file.readlines()
					#bankFile[idxChk]=bankFile[idxChk].split(",")
					#bankFile[idxChk][-1]=str(int(bankFile[idxChk][-1])-int(money))

					dataList.append(self.AccDtoList[idxChk].getId())
					dataList.append(self.AccDtoList[idxChk].getName())
					dataList.append(self.AccDtoList[idxChk].getNumbr())
					dataList.append(self.AccDtoList[idxChk].getBalance())
					bankFile[idxChk]=",".join(dataList)+"\n"
					file=open("./_dataSet03Bank/BankMSDB01.txt", "w")
					file.writelines(bankFile)
					file.close()
				else:
					print("고객님의 잔액이 부족합니다.")
			else:
				print("은행에 돈이 없습니다.")
		else:
			print("0원 이상 입금하세요")






	#=========================================================================================================================================================		
	def customDel(self, idxChk, custId ):
		print("^탈퇴")
		idChk=input("고객번호 확인:")
		if idChk==custId:
			
			AccountV01DTO.bankBalance-=int(self.AccDtoList[idxChk].getBalance())

			popUser=self.AccDtoList.pop(idxChk)
			
			print(len(self.AccDtoList))
			
			
			file=open("./_dataSet03Bank/BankMSDB01.txt", "r")
			bankFile=file.readlines()

			del bankFile[idxChk]
			file=open("./_dataSet03Bank/BankMSDB01.txt", "w")
			file.writelines(bankFile)
			file.close()
			print(f"{popUser.getName()} 회원탈퇴 성공!")