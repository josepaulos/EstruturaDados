class Funcionario:
    def __init__(self):
        self.__salario = None
        self.__nome = None

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def setSalario(self,salario):
        self.__salario = salario

    def getSalario(self):
        return self.__salario


jose = Funcionario()
jose.setNome('José')
jose.setSalario(1000)

paulo= Funcionario()
paulo.setNome('Paulo')
paulo.setSalario(2000)

print( 'Nome:',jose.getNome())
print('Salario:',jose.getSalario())

print('Nome:',paulo.getNome(),'Salario:',paulo.getSalario())