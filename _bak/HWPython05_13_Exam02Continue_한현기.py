grade = [90, 30, 60, 50, 80]

hapGyuk = "합 격"
for i in range(len(grade)) :
	if grade[i] < 60 :
		continue
	print("%d 번 학생은 %3d 점 %3s 입니다." %  (i+1, grade[i],hapGyuk))


	