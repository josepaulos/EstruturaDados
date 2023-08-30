class bola:
    def __init__(self):
        self.__cor="azul"
        self.__circuferencia=None
        self.__material=None

    def setAtri(self,cor,circuferencia,material):
         self.__cor =cor
         self.__circuferencia =circuferencia
         self.__material =material
    
    def getAtri(self):
        return self.__cor,self.__circuferencia,self.__material



adidas=bola()
adidas.setAtri('vermelho',12,"couro")

print(adidas.getAtri())