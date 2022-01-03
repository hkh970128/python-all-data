TName = ["구분","사원명","입사일","급여"]

empInfo = [
	['T160501',"캔디","2016-05-10"],
	['R160510',"장미","2016-05-10"],
	['t160811',"튤립","2016-08-15"],
	['T160821',"포도","2016-08-22"],
	['r160850',"사과","2016-08-30"]
]

empPayTable = [
	[250,10],
	[200,12],
	[300,9],
	[230,11],
	[150,12]
]


for i in range(len(TName)) :
	print(TName[i],end="\t\t")
print()
print("-"*70)
for i in range(len(empInfo)) :
	for x in range(len(empInfo)) :
		if empInfo[i][0][0] == 'R'  or empInfo[i][0][0] == 'r' :
			print("정규직\t\t{}\t\t{}\t{}" .format (empInfo[i][1] ,empInfo[i][2],empPayTable[i][0]*empPayTable[i][1]))
		else :
			print("계약직\t\t{}\t\t{}\t{}" .format (empInfo[i][1] ,empInfo[i][2],empPayTable[i][0]*empPayTable[i][1]))
