class Nodo:
    def __init__(self, dado=0,nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self) :
        return '%s -> %s' %(self.dado,self.anterior)

class Pilha:
    def __init__(self):
        self.topo = None

    def __repr__(self):
        return "[" +str(self.topo)+"]"

    