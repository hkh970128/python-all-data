import csv

temperRegionFileList = ['seoulNullChk.csv', 'daejeonNullChk.csv', 'daeguNullChk.csv', 
        'busanNullChk.csv', 'gwangjuNullChk.csv']

temperFirstLine = []



for i in temperRegionFileList:
    f = open("./_dataSetGilBut01/"+i,'r')
    data = csv.reader(f)
    data1 = list(data)
    temperFirstLine.append(data1)



print(temperFirstLine)
