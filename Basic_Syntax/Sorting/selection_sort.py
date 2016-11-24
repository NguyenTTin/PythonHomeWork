__auth__ = 'NguyenTTin'


import random
import time

nlist=[]
for i in range(20):
    nlist.append(random.randrange(1000))

print(nlist)

start_time=time.perf_counter()
#The selection sort
for i in range(len(nlist)-1):
    i_min=i
    for j in range(i+1,len(nlist)):
        if nlist[j]<nlist[i_min]:
            i_min=j
    tmp=nlist[i]
    nlist[i]=nlist[i_min]
    nlist[i_min]=tmp
stop_time=time.perf_counter()
print(nlist)
print(stop_time-start_time)