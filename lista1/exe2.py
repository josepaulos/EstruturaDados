class quadrado:
    def __init__(self,lado):
        self.__lado = lado
    
    def getLado(self):
        return self.__lado

quad=quadrado(12)
quad.getLado()
print(quad.getLado())