__auth__ = 'NguyenTTin'

class Vehicle():
    def __init__(self, colour):
        self.colour=colour

class Car(Vehicle):
    def __init__(self, colour, ty):
        self.ty=ty
        Vehicle.__init__(self,colour)
    def speed(self, maxspeed):
        self.maxspeed = float(maxspeed)
        return maxspeed

class Motobike(Vehicle):
    def __init__(self,colour, ty):
        self.ty = ty
        Vehicle.__init__(self, colour)


car1=Car('Red','SUV')
print(car1.colour)
car1.speed(1000)
print(car1.speed(1000))
moto1=Motobike('Blue','Sport')
print(moto1.ty)
