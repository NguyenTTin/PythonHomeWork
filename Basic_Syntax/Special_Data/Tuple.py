__auth__ = 'NguyenTTin'

# l1=[1,2,3,4,5]
# l2=['a','b','c','d','e']
# l2.reverse()
# t=list(zip(l1,l2))
# print(t)


numList = [9, 3, 2, 5, 6, 8, 11]
fl=[]
sl=[]
for i in numList:
    if i <=5:
        fl.append(i)
    else:
        sl.append(i)
result=(fl,sl)
print(result)
