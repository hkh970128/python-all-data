class ValChk() :
	vi = 10
	def __init__(self):
		self.mv01 = 10



obj01=ValChk()
obj02=ValChk()
obj03= ValChk()


obj01.mv01 +=10 
ValChk.vi +=10
print(obj01.mv01)
print(obj01.vi,ValChk.vi)
print()

obj02.mv01 +=10 
ValChk.vi +=10
print(obj02.mv01)
print(obj02.vi,ValChk.vi)
print()



obj03.mv01 +=10 
ValChk.vi +=10
print(obj03.mv01)
print(obj03.vi,ValChk.vi)



