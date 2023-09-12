class funcionario:
    def __init__(self,nome, salario):
        self.nome=nome
        self.salario=salario

    def getNome(self):
        return self.nome
    
    def getSalario(self):
        return self.salario
    

nomeFun=input('Qual é o nome do Funcionario ')
salarioFun=input('Qual é o salário do Funcionario ')

fun=funcionario(nomeFun,salarioFun)

print('Nome:',fun.getNome())
print('Salário:',fun.getSalario())