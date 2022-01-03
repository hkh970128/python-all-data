result = 0
class CalV01:
	def dbset(self):
		self.result = 0
	def add (self,num) :
		#global result
		
		self.result += num
		return self.result

#객체 생성을 했다.	
cal01 = CalV01()
#result 초기화 함
cal01.dbset()

print(cal01.add(5))
print(cal01.add(7))





#객체 생성을 했다.	
cal02 = CalV01()
#result 초기화 함
cal02.dbset()

print(cal02.add(50))
print(cal02.add(7))

''' 클래스  
 객체 생성후
 java 는 new 생성자()  객체자신>> this
 클래스()
 생성자 : 모양_메소드 같다 >> 클래스이름과 같은 메소드 

 파이썬 
 객체명 = 생성자

'''



