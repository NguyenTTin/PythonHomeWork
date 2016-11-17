__auth__ = 'NguyenTTin'

def gcd(a,b):
    while b:
        a,b=b,a%b
    print ("The greatest common divisor is {}".format(a))

gcd(100,150)