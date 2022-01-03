#총 건수를 입력하세요. : 105 , 100
#한 페이지당 보여 줄 건수 : 10
#[총 11페이지 입니다.] ,[총 10페이지 입니다.]






def getTotalPage(totalData, dataPerPage):
    if totalData % dataPerPage == 0:
        return totalData // dataPerPage
    else:
        return totalData // dataPerPage + 1
totalData=int(input("총 건수를 입력하세요. :"))
dataPerPage=int(input("한 페이지당 보여 줄 건수를 입력하세요. :"))
totalPage=getTotalPage(totalData,dataPerPage)
print(f'총 {totalPage}페이지 입니다')


while True:
       nowPage=int(input("확인할 페이지를 입력 하세요:"))
       dataOfBeginPage=(nowPage-1)*dataPerPage
       print()
       if nowPage<1:
              break
       elif nowPage>totalPage:
              print(f'^확인할 수 있는 페이지 초과 입니다')
              continue
       try:
              if dataOfBeginPage+dataPerPage>totalData:
                     raise IndexError
              for x in range(dataOfBeginPage,dataOfBeginPage+dataPerPage):
                     print(f'{x}번 데이터 확인')
       except IndexError:
              for x in range(dataOfBeginPage,dataOfBeginPage+(totalData%dataPerPage)):
                     print(f'{x}번 데이터 확인')