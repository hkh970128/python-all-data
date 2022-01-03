menu =['orange','strawberry','peach','mango','grape']
price = [1000,2500,1500,2000,2000]
coin = [5000,1000,500,100]


money=0




while True :
	print("******우송대학교 과일 판매머신*******")
	for i in range(len(menu)):
		print(i+1 , menu[i], price[i],'원')
	print("-"*35)
    
	num = int(input("숫자를 입력하시오1-5 "))
	if num == 1:
		
		print("구매하신 번호는 %d 입니다\n" % num)
		print("사용할수 있는 코인은 {}입니다" .format(coin))
		money = int(input("코인을 입력하세요"))
		print("투입된 금액은 %d 입니다." % money)
		print("-"*35)
		print("잔돈은 %d 입니다" % (money-int(price[0])))
		

	if num == 2:
		print("구매하신 번호는 %d 입니다\n" % num)
		print("사용할수 있는 코인은 {}입니다" .format(coin))
		money = int(input("코인을 입력하세요"))
		print("투입된 금액은 %d 입니다." % money)
		print("-"*35)
		print("잔돈은 %d 입니다" % (money-int(price[1])))
		
	if num == 3:
		print("구매하신 번호는 %d 입니다\n" % num)
		print("사용할수 있는 코인은 {}입니다" .format(coin))
		money = int(input("코인을 입력하세요"))
		print("투입된 금액은 %d 입니다." % money)
		print("-"*35)
		print("잔돈은 %d 입니다" % (money-int(price[2])))
		
	if num == 4:
		print("구매하신 번호는 %d 입니다\n" % num)
		print("사용할수 있는 코인은 {}입니다" .format(coin))
		money = int(input("코인을 입력하세요"))
		print("투입된 금액은 %d 입니다." % money)
		print("-"*35)
		print("잔돈은 %d 입니다" % (money-int(price[3])))
		
	if num == 5:
		print("구매하신 번호는 %d 입니다\n" % num)
		print("사용할수 있는 코인은 {}입니다" .format(coin))
		money = int(input("코인을 입력하세요"))
		print("투입된 금액은 %d 입니다." % money)
		print("-"*35)
		print("잔돈은 %d 입니다" % (money-int(price[4])))
		
	else :
		print("종료")
		break

	










'''   
    if  num==1:
        print( menu[0], price[0],'원')
        continue
    if num == 2 :
        print( menu[1], price[1],'원')
        continue
    if num == 3 :
        print( menu[2], price[2],'원')
        continue
    if num == 4 :
        print( menu[3], price[3],'원')
        continue
    if num == 5 :
        print( menu[4], price[4],'원')
        continue
    else :
        print("종료")
    break

'''

