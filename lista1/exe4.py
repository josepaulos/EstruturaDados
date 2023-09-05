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
    

    def emagrecer(self,peso2):
        return self.__peso - peso2
    
    
    def engordar(self,peso2):
        return self.__peso + peso2
    
    def envelhecer(self,idade2):
        return self.__peso + idade2
    
    
    def envelhecer(self,idade2):
        return self.__peso + idade2
    
    #def crescer(self,):