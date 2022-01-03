import csv
file = open('./../_dataSet01\StuDataSet02.csv','r')
stu_csv = csv.reader(file)
print(stu_csv)

stu = list(stu_csv)


for i in range(len(stu)) :
	print(stu[i])