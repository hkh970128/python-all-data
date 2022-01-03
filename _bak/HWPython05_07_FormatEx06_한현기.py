alignLeft = "{1:<10}".format("niceday","hi")
alignRight = "{:>10}".format("niceday")
alignCenter = "{0:^10}".format("niceday")

spaceFill01 = "{:*^10}".format("hi")


print(alignLeft)
print(alignRight)
print(alignCenter)
print(spaceFill01)



x  = 342134234
y =	 3.42134234

floatEx1 = "{0:0.4f}".format(y,x) 
floatEx2 = "{0:10.4f}".format(y)


print(floatEx1)
print(floatEx2)