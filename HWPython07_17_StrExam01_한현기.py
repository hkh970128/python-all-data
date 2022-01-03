strEx = 'https://search.naver.com/search.naver?'
where ='nexearch&sm=top_hty&fbm=1&ie=utf8&query=html'
'''
sm = top_hty

fbm = 0
ie = utf8
query = html

'''

s =strEx.split('?')
w = where.split('&')


print(" url=","".join(s))
for i in range(len(w)) :
	print("",w[i])



print(f" 변수는 %d" % len(w))
