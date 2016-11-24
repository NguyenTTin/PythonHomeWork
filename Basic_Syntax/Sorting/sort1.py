__auth__ = 'NguyenTTin'

import random

l=[]
for i in range(10):
    l.append(random.randrange(1000))
print(l)

def sapxep(l):
    l=list(l)
    for i in range(int(len(l))):
        for j in range(i+1, int(len(l))):
            if l[i]>l[j]:
                temp=l[i]
                l[i]=l[j]
                l[j]=temp
    print(l)

sapxep(l)

