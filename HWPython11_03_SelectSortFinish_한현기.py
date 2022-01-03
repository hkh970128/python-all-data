a = [75,65,100,80,90,55,95,30,20,50]


print("소트전 데이터",a)

for i in range(len(a)-1): # 전체돌려버리고
    idx = i
    for j in range(i + 1, len(a)): # 분친처럼 돌려야함
      
        if a[idx] > a[j]:
            idx = j
		a[i], a[idx] = a[idx],a[i]

			
		print("소트후 데이터",a)
