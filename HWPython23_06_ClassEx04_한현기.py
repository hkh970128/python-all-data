
class CalV01:
	def dbset(self):
		self.num1=0
		self.num2=0

	def add (self,num1,num2) :
		self.num1=num1
		self.num2=num2
		
		return self.num1+self.num2

	def sub (self,num1,num2) :
		self.num1=num1
		self.num2=num2
		
		return self.num1-self.num2

	def mul (self,num1,num2) :
		self.num1=num1
		self.num2=num2
		
		return self.num1*self.num2

	def div (self,num1,num2) :
		self.num1=num1
		self.num2=num2
		
		return self.num1//self.num2

#덧셈 객체.	
cal01 = CalV01()
cal01.dbset()
result = cal01.add(100,20)


# 뺄셈 객체
cal02 = CalV01()
cal02.dbset()
result2 = cal02.sub(100,20)
# 곱셈 객체
cal03 = CalV01()
cal03.dbset()
result3 = cal03.mul(100,20)
#나눗셈 객체
cal04 = CalV01()
cal04.dbset()
result4 = cal04.div(100,20)



print(f' {cal01.num1} + {cal01.num2} = {result}')
print(f' {cal01.num1} - {cal01.num2} = {result2}')
print(f' {cal01.num1} * {cal01.num2} = {result3}')
print(f' {cal01.num1} / {cal01.num2} = {result4}')


