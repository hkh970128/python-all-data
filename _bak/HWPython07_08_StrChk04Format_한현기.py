a = "Hello"
b = "World"
c = a + b
print(c)

c = a + " " + b #한칸이 뛰어짐
print(c)



age = 36
txt = "My name is John, and I am {}" #{} 안에 들어감 age
print(txt.format(age))



quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


myorder = "I want to pay {2} dollars for {0} pieces of item {1}." # 재배열 
print(myorder.format(quantity, itemno, price))



txt = "We are the so-called \"Vikings\" from the north." #\   \  사용
print(txt)