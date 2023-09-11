class pessoa:
    def __init__(self):
        self.__nome = None
        self.__idade = None
        self.__peso = None
        self.__altura = None
    
    def setPessoa(self,nome,idade,peso,altura):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura

    def getNome(self):
        return self.__nome
    

    def emagrecer(self,peso2):
        return self.__peso - peso2
    
    
    def engordar(self,peso2):
        return self.__peso + peso2
    
    def envelhecer(self,idade2):
        return self.__idade + idade2
    
    def crescer(self):
        idade = self.__idade
        if idade <21:
           self.__altura += 0.05
           return self.__altura
        



jose=pessoa()
jose.setPessoa('José Paulo ',18,120,1.83)
print(jose.getNome())
print(jose.emagrecer(2))
print(jose.engordar(2))
print(jose.envelhecer(2))
print(jose.crescer())


    