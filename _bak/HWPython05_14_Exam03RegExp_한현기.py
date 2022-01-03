grade = [90, 30, 60, 50, 80]


for i in range(len(grade)) :
	jumsu = grade[i]

	print(f"{i+1} 번 학생{jumsu} 점 합  격 " if jumsu >=60 else f"{i+1} 번 학생{jumsu} 점 불합격" )