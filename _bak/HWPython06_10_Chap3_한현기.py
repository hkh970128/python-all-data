#  글 이해하기
a = "Life is too short, you need python"
if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")


#2 1000까지 3의배수
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0: 
        result += i
    i += 1

print(result) 


#3 별 * ** *** **** *****
i = 0
while True:
    i += 1 
    if i > 5: break     
    print('*' * i)

#4 for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
for x in range(1,101) :
	print(x)
	

# 5for문을 사용하여 A 학급의 평균 점수를 구해 보자.
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total =0

for jumsu in A :
	total += jumsu

av =  total / len(A)

print(av)


'''6numbers = [1, 2, 3, 4, 5]

result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2) < 이걸 표현식으로 아까처럼'''


numbers = [1,2,3,4,5]
result = [ n*2 for n in numbers if n %2 ==1 ]
print(result)
