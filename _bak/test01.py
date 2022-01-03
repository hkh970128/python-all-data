menu = ["고객번호", "고객이름", "계좌번호", "고객잔액"]
file = open("./_dataSet03Bank/BankMSDB01.txt",'r')
DBdata = file.readlines()
print("-"*60)
print(' '.join(menu))
print("-"*60)
for i in range(len(DBdata)):
	print(DBdata[i])
print("-"*60)