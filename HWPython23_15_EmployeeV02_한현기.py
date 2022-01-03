class Employee():
	
	def __init__(self,no,name,initday):
		self.no=no
		self.name=name
		self.initday=initday
	def paychk(self):
		return 0
	def getNo(self):
		return self.no
	def getName(self) :
		return self.name
	def getInitday(self):
		return self.initday
	
	def setNo(self,no):
		self.no=no
	 
	def setName(self,name) :
		self.name = name
	def setInitday(self,initday):
		self.initday = initday
	
	


class Regular(Employee):
	def __init__(self,no,name,initday,pay):
		super().setNo(no)
		super().setName(name)
		super().setInitday(initday)
		self.pay = pay

	def paychk(self):
		return self.pay
	


class Daily(Employee):
	

	def __init__(self,no,name,initday,workday,dailypay):
		super().setNo(no)
		super().setName(name)
		super().setInitday(initday)
		self.workday=workday
		self.dailypay=dailypay

	def paychk(self):
		return self.workday*self.dailypay


regObj01 = Regular('r001','오렌지','2021-10-11','200')
dayObj01 = Daily('d001','한현기','2021-10-12',9,20)

print('='*50)
print("사번 성명  입사일  급여")
print('='*50)
print(regObj01.getNo(),regObj01.getName(),regObj01.getInitday(),regObj01.paychk())
print(dayObj01.getNo(),dayObj01.getName(),dayObj01.getInitday(),dayObj01.paychk())
