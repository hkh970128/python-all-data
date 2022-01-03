#HWPython14_09_Recommend_한현기
'''
#01. list -2글자 >> 이상 뒤 2글자
#02. set : 중복체크
       range list에서 몇개 체크
       vName[], vNum[] 

민교,강경태, 고재호, 김태인, 한현기,재호,민교,재호,선웅,박연희,민교, 선웅, 
강경태, 고재호, 김태인, 한현기, 이준혁,민교, 선웅,임재우,민교,강경태,경태,경태
"민교","강경태","고재호","김태인","한현기","재호","민교","재호","선웅","박연희","민교","선웅","강경태","고재호","김태인","한현기","이준혁","민교","선웅","임재우","민교","강경태","경태","경태"
'''

vNum=[]
nameList = ['민교','강경태','고재호','김태인','한현기','재호','민교','재호','선웅','박연희','민교','선웅','강경태','고재호','김태인','한현기','이준혁','민교','선웅','임재우','민교','강경태','경태','경태']
vName   = []


	

for i in nameList :
	if len(i) !=2 :
		vName.append(i[1:])
	else :
		vName.append(i)

vNameset= set(vName) #set으로 중복제거
vNamelist =list(vNameset)

print(vNamelist)

for x in range(len(vNamelist)) :
	vNum.append(vName.count(vNamelist[x]))


print(vNum)
print("짝이 맞긴함 \n")


for x in vNamelist :


	print(x,vName.count(x),'표')





		
		