class macaco:
    def __init__(self, nome) :
        self.nome=nome
        self.bucho=[]

    def EncherBuchinho(self,comida):
        self.bucho.append(comida)   
    
    def VerBuchinho(self):
        return print('Olha o buchinho do macaco',self.bucho)
    
    def BuchinhoTaVazio(self):
        self.bucho.clear()
        return print('O Buchinho ta vazio',self.bucho)
    

macaico1=macaco('macaico')
monkey=macaco('monkey')


macaico1.EncherBuchinho('banana')
macaico1.EncherBuchinho('morango')
monkey.EncherBuchinho('carne')
monkey.EncherBuchinho('abacate')


monkey.EncherBuchinho(macaico1.bucho,)


macaico1.VerBuchinho()
monkey.VerBuchinho()

