__auth__ = 'NguyenTTin'

NoL=int(input("Please enter number of the lines:   "))
NoA=int(input("Please enter number of the asterisk:   "))
Bouder=NoL*NoA

for i in range(1,NoA+1):
    for j in range(i,Bouder+1):
        print(" "*j,end='')
        if j%NoA==0:
            print("*",end='')
    print("")

