__auth__ = 'NguyenTTin'

import random
import time
nlist=[]

for i in range(20):
    nlist.append(random.randrange(1000))

print(nlist)

start_time=time.perf_counter()
for i in range(1,len(nlist)):
    j=i
    while j:
        if nlist[j]<nlist[j-1]:
            tmp=nlist[j-1]
            nlist[j-1]=nlist[j]
            nlist[j]=tmp
        j-=1
stop_time=time.perf_counter()
print(nlist)
print(stop_time-start_time)