menu = [' 1. 탈퇴학생 ', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 4. 합격생목록 ',' 9. 메뉴종료 ']
menuChk = ['1','2','3','4','9']
itemList = ['ID','필기점수','실기점수','인성점수']
MenuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];

dic = {}
deleteIDList = []
idx = 0;


def stuTitle() :
	print()
	print("-"*70)
	print("\t\t\t>>학생관리시스템<<\t\t\t")
	print("-"*70)
	print(' '.join(menu))
		
		
		
while True :
	stuTitle()
	num =int(input("\n\n번호를 입력하세요"))
		
	if num ==  1 :
		print("\t\t\t"+menu[0],"Chk")
	elif num == 2 :
		print("\t\t\t"+menu[1],"Chk")
	elif num == 3 :
		print("\t\t\t"+menu[2],"Chk")
	elif num == 4 :
		print("\t\t\t"+menu[3],"Chk")
	elif num == 9 :
		break
	else :
		print("다시입력")
