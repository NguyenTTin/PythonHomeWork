__auth__='TinNT'

class First():
    def __init__(self,name):
        self.name=name
        pass
    def __str__(self):
        return("The First Class Demo")
    def __setattr__(self, key, value):
        if key == self.name:
            self.value=value
