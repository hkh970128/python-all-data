class InheritParent():
	
	def __init__(self ):
		self.vi01 = 20
	def mView(self):
		print("부모메소드 확인")
		

class InheritChild(InheritParent):
	def mView(self):
		super().mView()
		print("자식메소드 확인")

obj = InheritChild()
print(obj.vi01)
obj.mView()





