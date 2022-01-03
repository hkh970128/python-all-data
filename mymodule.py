import sys
print(sys.path)


sys.path.append("./myModule3")

print('\n\n',sys.path)



import mod3

print(mod3.sum(1,2))