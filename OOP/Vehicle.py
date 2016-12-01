__auth__ = 'NguyenTTin'

class Car(object):

    def __init__(self,typ):
        self.typ = typ

    def runfunct(self):
        return("have run function")


class Canoe(object):

    def __init__(self,name):
        self._name = name

    def surffunct(self):
        return("have surf function")

class Aphibian (Car, Canoe):

    def __init__(self, Car_Type, Canoe_Brand):
        self._called = "%s - %s"%(Car_Type, Canoe_Brand)
        Car.__init__(self, 'Sport')
        Canoe.__init__(self, 'American')

    def __str__(self):
        return("The {} can {} and {}".format(self._called, self.runfunct(), self.surffunct()))


a1=Aphibian('Sport', 'Popie')
