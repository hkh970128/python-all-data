import csv


with open("./_dataSetGilBut01/temperRegion.txt" ,encoding='UTF-8') as file:
    lines = file.readlines()

for i in range(len(lines)) :
    if ':' in lines[i]:
        temp = lines[i].split(':')
        lines[i]=temp[1]
    lines[i].strip()

lines =','.join(lines)
lines = lines.split(",")
Writefile=""

for i in lines :
    temp = i.strip().split('(')
    Writefile += temp[1][:-1]+','+temp[0]+'\n'



with open("./temPerRagionChk.csv",'w',encoding='cp949') as file:
    
    file.write(Writefile)
    

print(Writefile)



