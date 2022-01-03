def getTotalpage(m,n):
	return (m//n)+1 if m%n!=0 else (m//n)


totalDataNum =int(input("총 데이터 건수를 입력하세요 :"))
pageSelect = int(input("한페이지 당 보여 줄 건수를 지정해주세요 :"))


print(f"[{getTotalpage(totalDataNum,pageSelect)}]페이지 입니다")
