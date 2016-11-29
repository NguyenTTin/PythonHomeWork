__auth__ = 'NguyenTTin'
'''
def tong(n):
    if n==0 or n==1:
        return n
    else:
        return tong(n-1) + n

print(tong(10))
'''
'''
def remov(st):
    if len(st)==1:
        return st
    elif st[0]==st[1]:
        return remov(st[1:])
    else:
        return st[0] + remov(st[1:])

print(remov('abccaaaaccacaclp'))
'''