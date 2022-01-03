a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)


tu = (1, 2, 3)
tu = tu + (4,)
print(tu)    


a = dict()
{}
a['name'] = 'python'
a[('a',)] = 'python'
a[250] = 'python'







a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)     # a 리스트를 집합자료형으로 변환
b = list(aSet)    # 집합자료형을 리스트 자료형으로 다시 변환
print(b)     




a  =[1,2,3]
a=b
print(id(a))
print(id(b))
a[1]=4
