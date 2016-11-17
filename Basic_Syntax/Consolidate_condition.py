__auth__ = 'NguyenTTin'

# num=int(input("Enter a bouder number:   "))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print ("%d"%j,end='')
#         if j==i:
#             print("")

# num = int(input("Enter the odd number:  "))
# while num%2==0:
#     num=int(input("Enter the odd number:  "))
#
# if num >=0:
#     for i in range(1, num):
#         for j in range(1, num):
#             print("%i" % num, end='')
#         print("")
#         num-=2
# else:
#     print("You have exeed the value!!")
# print(num)


list=[]
list3=[]
list5=[]
for i in range(1,101):
    list.append(i)
    # if i%3==0:
    #     list3.append(i)
    # if i%5==0:
    #     list5.append(i)

#print(len(list3), len(list5))
list3=list[::2]
list5=list[::4]
print(list3)
print(list5)

