from BankMSV01 import *


daoObj= AccountV01DAO()
daoObj.DBSet()
daoObj.customSel()

while True:
	
	daoObj.customInfo()