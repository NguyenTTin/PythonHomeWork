__auth__ = 'NguyenTTin'

class Animal():
    def __init__(self):
        pass
    def whistle(self):
        pass

class Tiger(Animal):
    def __init__(self):
        pass

    def whistle(self):
        return("The Tiger whistles Woaaa!!!")

class Pig(Animal):
    def __init__(self):
        pass

    def whistle(self):
        return("The Pig whistles Ecccc!!!")

class Wolf(Animal):
    def __init__(self):
        pass

    def whistle(self):
        return ("The Wolf whistles Hwooo!!!")

t=Tiger()
p=Pig()
w=Wolf()

l=[t,p,w]

for i in l:
    print(i.whistle())