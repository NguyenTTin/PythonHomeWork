__auth__ = 'NguyenTTin'

import math

class Circle(object):
    def __init__(self,radius):
        self.radius = float (radius)
    def getArea(self):
        return self.radius**2*math.pi
    def getPerimeter(self):
        return 2*self.radius*math.pi
    def __str__(self):
        print ("Area and Perimeter is {} and {}".format(self.getArea(),self.getPerimeter()))


c1=Circle(10)
c1.__str__()
#print("The area is %.2f"%(c1.getArea()))


