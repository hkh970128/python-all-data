menu =['orange','strawberry','peach','mango','grape','종료']
price = [1000,2500,1500,2000,2011]



print("******우송대학교 과일 판매머신*******")



while True :
    for i in range(len(menu)) :
        print(i+1 , menu[i], price[i],'원')
    
    num = int(input("숫자를 입력하시오"))

    if num < 6 :
        print( menu[num-1], price[num-1],'원')
        continue
    else :
        print("종료")
        break
	

		