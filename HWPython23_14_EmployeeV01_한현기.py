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
	


class Regular(Employee):
	def __init__(self,no,name,initday,pay):
		super().__init__(no,name,initday)
		self.pay=pay

	def paychk(self):
		return self.pay
	


class Daily(Employee):
	def __init__(self,no,name,initday,workday,dailypay):
		super().__init__(no,name,initday)
		self.workday=workday
		self.dailypay=dailypay

	def paychk(self):
		return self.workday*self.dailypay


regObj01 = Regular('r001','오렌지','2021-10-11','200')
dayObj01 = Daily('d001','한현기','2021-10-12',9,20)

print('='*50)
print("사번 성명  입사일  급여")
print('='*50)
print(regObj01.no,regObj01.name,regObj01.initday,regObj01.paychk())
print(dayObj01.no,dayObj01.name,dayObj01.initday,dayObj01.paychk())
