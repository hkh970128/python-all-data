
print("="*130)

for i in range(2,10) :
	print("%d 단\n" % i ,end="\t")
print("="*130)





for x in range (2,10) :
	for y in range (2,10) :
		print("%3d x%3d = %3d" % (y, x, (x*y)), end='\t')
	print()