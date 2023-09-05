class retangulo:
    def __int__(self):
        self.base=None
        self.altura=None

    def setLados(self,base,altura):
        self.base=base
        self.altura=altura

    def getLados(self):
        return self.base,self.altura
        

    def calArea(self):
        return (self.base*self.altura)

    def calPerimetro(self):
        return (self.base+self.altura)*2



fugura=retangulo()
fugura.setLados(8,8)
print(fugura.getLados())
print("A area do retandulo é=",fugura.calArea())
print("O perimetro do retandulo é=",fugura.calPerimetro())
