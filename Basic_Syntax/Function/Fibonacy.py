__auth__ = 'NguyenTTin'

def fibo(n):
    a,b=0,1
    if n<2:
        b=1
    else:
        for i in range(n):
            a,b=b,a+b
    return b

print(fibo(8))
