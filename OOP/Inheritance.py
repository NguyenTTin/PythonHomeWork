__auth__ = 'NguyenTTin'


'''
class Car():
    def __init__(self, colour, ty):
        self.ty=ty
        self.colour = colour
    @staticmethod
    def speed():
        maxspeed = 300
        return maxspeed

    def __str__(self):
        return ("The colour is {} and maxspedd is {}".format(self.colour, self.maxspeed))

class Motobike():
    def __init__(self,colour, ty):
        self.ty = ty
        self.colour = colour


class MixVehicle(Car,Motobike):
    def __init__(self,colour,ty):
        Car.__init__(self,colour,ty)
        Motobike.__init__(self,colour,ty)

m=MixVehicle('Red','Sport')
print(m.speed())
'''

import random

class People(object):

    def __init__(self, haircolour, skincolour, eyecolour):
        self.haircolour = haircolour
        self.skincolour = skincolour
        self.eyecolour = eyecolour

    def __str__(self):
        return ("The haircolour is {}, skincolour is {} and eyecolour is {}".format(self.haircolour,
                                                                                    self.skincolour,
                                                                                    self.eyecolour))


class Asianer(People):

    def __init__(self, country):
        People.__init__(self, 'black', 'yellow', 'black')
        self.country = country

    def GoodatMath(self):
        print ("The {} good at math".format(self.country))

    def __str__(self):
        return ("The {} person has {} hair, {} skin and {} eyecolour".format(self.country,
                                                                             self.haircolour,
                                                                             self.skincolour,
                                                                             self.eyecolour))

class Westener(People):

    def __init__(self, country):
        People.__init__(self, 'blond', 'white', 'blue')
        self.country = country

    def GoodatArt(self):
        print("The {} good at art".format(self.country))

    def __str__(self):
        return("The {} person has {} hair, {} skin and {} eyecolour".format(self.country,
                                                                             self.haircolour,
                                                                             self.skincolour,
                                                                             self.eyecolour))

class Crossbred(Asianer,Westener):

    def __init__(self, mothercountry, fathercountry):
        self.country = "%s - %s"%(mothercountry, fathercountry)
        self.eyecolour = random.choice(['blue', 'black', 'dark blue'])
        self.haircolour = random.choice(['blond', 'black', 'red'])
        self.skincolour = random.choice(['white', 'yellow', 'pink'])

    def __str__(self):
        return ("The {} person has {} hair, {} skin and {} eyecolour".format(self.country,
                                                                             self.haircolour,
                                                                             self.skincolour,
                                                                             self.eyecolour))

Cr1=Crossbred('Japanese', 'American')
print(Cr1.GoodatArt())
print(Cr1.GoodatMath())
#print(Cr1.haircolour)
#print(Cr1.eyeclour)
#print(Cr1.eyecolor)