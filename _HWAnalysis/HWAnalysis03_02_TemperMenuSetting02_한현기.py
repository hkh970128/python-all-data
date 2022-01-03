import csv
from types import coroutine



regionMenu = []
temperRegionFileList = ['seoulNullChk.csv', 'daejeonNullChk.csv', 'daeguNullChk.csv', 'busanNullChk.csv', 'gwangjuNullChk.csv']
temperFirstLine= []
regionName = []
regionNum = []

mydict = {}

with open('./_dataSetGilBut01/temPerRagionChk.csv', mode='r') as rData:
	rData = csv.reader(rData)
	mydict = {rows[0]:rows[1] for rows in rData}



for dataIdx in range(len(temperRegionFileList)):
	regionData = open("./_dataSetGilBut01/"+temperRegionFileList[dataIdx], 'r')
	vData = csv.reader(regionData)
	vHeader = next(vData)
	temperFirstLine.append(vHeader)
	regionData.close()
	
for key, value in mydict.items():
	for idx in temperFirstLine:
		if key == idx[1]:
			regionNum.append(idx[1])
			regionName.append(value)
			regionMenu.append(value+":"+idx[1])
regionMenu.append("Q. 종료")
print(regionName)
print(regionNum)
print(regionMenu)

def regionTitle():
	print("="*30+"기온 공공데이터 분석 프로젝트 Ver01."+"="*30)
	s = "     ".join(regionMenu)
	for i in regionMenu:
		print("    "+i, end='   ')
	print('\n'+"="*96)
	menuNum = input("메뉴의 번호를 선택해주세요 : [종료 Q ]")
	if menuNum.upper() == 'Q':
		exit()
	return menuNum
	
		
	

def subMenuTitle(x):
	while True:
		for i in regionMenu :
			if x in regionNum:
				print(f"{regionName[i]}지역이 선택 되었습니다.")
				break
			else:
				print(f"{x}는 해당 없음 지역 입니다.")
				coroutine


#def subMenuChk():

while True:
	num=regionTitle()
	subMenuTitle(num)





    
    