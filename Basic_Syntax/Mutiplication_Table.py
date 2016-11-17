__auth__ = 'NguyenTTin'


counter=0 # Create a variable to count the number of line
print("\t\tMUTILPLICATION TABLE")
for i in range(1,10):
    print("  {0:2d}".format(i),end='')
print("")
print("--"*20)
for j in range(1,10):
    print(str(j) + '|', end='')
    for k in range(1,10):
        print(" %3d"%(j*k),end='')
        counter+=1
        if counter %9==0:
            print("")



