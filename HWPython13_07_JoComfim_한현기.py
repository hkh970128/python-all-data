import random

rn=[]



while True :
	name_list = input("4인 이상의 이름을 입력하세요. (종료0)")
	if len(name_list.split(' ')) <4 :
		if len(name_list.split(' ')) ==1 :
			if int(name_list)==0 :
				print(종료합니다)
				break
		print("명수를 확인하세요")
		continue

	if len(rn) == len(name_list.split(' ')) :
		break
		rnd = random.randint(1,len(name_list.split(' ')))
		if rnd not in rn :
			rn.append(rnd)


	print("\t\t이름=" ,end='\t\n')
	for name_list in name_list.split(' '):
		print(name_list,end='\t\n')
		print(rn,end='\t')


		'''
		else :
		print(rn,end="\t")
	for rn in rn :
		print(rn, end="\t")
	else :
		print("\n\n")
'''










