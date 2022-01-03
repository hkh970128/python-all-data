thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)




thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])



thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1



tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


			#0 1   2  3  4  5  6  7 8  9 
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)