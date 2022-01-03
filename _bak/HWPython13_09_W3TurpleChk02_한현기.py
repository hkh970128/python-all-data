thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])



#             0			1			2			3		4		  5			6
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
# cherry~~ kiwi


print(thistuple[:4])
#orange 까지



print(thistuple[2:])
#채리부터 쭉

print(thistuple[-4:-1])
#오렌지부터~ 멜론

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")