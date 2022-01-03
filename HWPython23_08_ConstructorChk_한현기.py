
class CalV01:
	def __init__(self,n01,n02) :
		self.num1 = n01
		self.num2 = n02
		

	def add (self) :

		
		return self.num1+self.num2

	def sub (self) :

		
		return self.num1-self.num2

	def mul (self) :

		
		return self.num1*self.num2

	def div (self) :

		
		return self.num1//self.num2

#덧셈 객체.	
cal01 = CalV01(100,20)
result = cal01.add()
# 뺄셈 객체
cal02 = CalV01(100,20)
result2 = cal02.sub()
# 곱셈 객체
cal03 = CalV01(100,20)
result3 = cal03.mul()
#나눗셈 객체
cal04 = CalV01(100,20)
result4 = cal04.div()



print(f' {cal01.num1} + {cal01.num2} = {result}')
print(f' {cal01.num1} - {cal01.num2} = {result2}')
print(f' {cal01.num1} * {cal01.num2} = {result3}')
print(f' {cal01.num1} / {cal01.num2} = {result4}')


