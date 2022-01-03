import csv
file = open('./../_dataSet01\StuDataSet02.csv','r')
stu_csv = csv.reader(file)


stu = list(stu_csv)

print(stu[0][1])