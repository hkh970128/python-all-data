print("Hello")
print('Hello')


a = 'hello'
print(a)


b= ''' 안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요
안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요
안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요'''
print(b)


c = "hello world"
print(c[4]) #o

for x in "hanhyunki":
  print(x)



print(len(c))


txt = "The best things in life are free!"
print("expensive" not in txt) #없으니 True
print("best" in txt)# 있으니 True
if "expensive" not in txt:    # expensive가 없으니까 프린트문 출력
  print("No, 'expensive' is NOT present.")