__auth__ = 'NguyenTTin'


dic={0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h',
     8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o',
     15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v',
     22: 'w', 23: 'x', 24: 'y', 25: 'z'}


def sapxep(l):
    l=list(l)
    for i in range(int(len(l))):
        for j in range(i+1, int(len(l))):
            if l[i]>l[j]:
                temp=l[i]
                l[i]=l[j]
                l[j]=temp
    return l

ch=list(input("Enter a string wich you want to sort:  \n"))
new_ch=[]
for i in ch:
    for j,k in dic.items():
        if i==k:
            new_ch.append(j)

new_ch1=sapxep(new_ch)
print("The string after sorted is:  ")

for c in new_ch1:
    print(dic.get(c),end='')





