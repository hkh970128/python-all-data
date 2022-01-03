#총 건수를 입력하세요. : 105 , 100
#한 페이지당 보여 줄 건수 : 10
#[총 11페이지 입니다.] ,[총 10페이지 입니다.]
import csv 
file = open("./_dataSetGilBut01/seoul.csv" ,"r")
data = csv.reader(file)
Vhead= next(data)
tmpList = list(data)






def getTotalPage(totalData, dataPerPage):
    if totalData % dataPerPage == 0:
        return totalData // dataPerPage
    else:
        return totalData // dataPerPage + 1

dataPerPage=int(input("한 페이지당 보여 줄 레코드를 입력하세요. :"))
totalPage=getTotalPage(len(tmpList),dataPerPage)
print(f'기온 공공데이터 레코드 개수: {len(tmpList)} 입니다')
print(f'기온 공공데이터 페이지 개수: {totalPage} 입니다')


while True:
    print(f"\n\tEnter 를 치면 다음페이지{dataPerPage}개 레코드 확인")
    inputPage=(input("\t\t확인할 페이지를 입력 하세요 (Q누르면 종료):"))
    
    nowPage = inputPage
    try :
        if inputPage.upper() =="Q":
            print("\n\t\t종료합니다")
            print("\n"+'-'*100)
            break
        elif inputPage=="":
         if nowPage ==totalPage :
             print("마지막 페이지 입니다.")
         else :
             nowPage+=1
        elif int(inputPage) in range (1,totalPage+1):
            nowPage = int(inputPage)
        else :
            print("\n\t\t 해당 하는 페이지가 존재하지 않습니다 입력을 확인해주세여")
            print("\n"+'-'*100)
    except ValueError:
        print("\n\t\t 해당 하는 페이지가 존재하지 않습니다 입력을 확인해주세여")
        print("\n"+'-'*100)
    dataOfBeginPage = int((nowPage)-1)*dataPerPage
    try:
        if dataOfBeginPage+dataPerPage>len(tmpList):
            raise IndexError
        for x in range(dataOfBeginPage,dataOfBeginPage+dataPerPage):
            print(f'\t\t{x}/ {len(tmpList)} \t\t{x}번째 : {tmpList[x]} ')
            print("\n"+'-'*100)
    except IndexError:
        for x in range(dataOfBeginPage,dataOfBeginPage+(len(tmpList)%dataPerPage)):
            print(f'\t\t{x}/ {len(tmpList)} \t\t{x}번째 : {tmpList[x]} ')
            print("\n"+'-'*100)







