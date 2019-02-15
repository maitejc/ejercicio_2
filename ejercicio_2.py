class Contador():
    def __init__(self, val = None):
        if val is not None:
            self.value = val
        else:
            self.value = 5
    def incrementar(self):
        return self.value +2
    def disminuir(self):
        return self.value -2
c = Contador()     
print(c.incrementar())

