class ContaCorrente:
    def __init__(self, numero_conta, nome, saldo=0):
        self.numero_conta = numero_conta
        self.nome = nome
        self.saldo = saldo
    
    def getConta(self,):
        return self.numero_conta,self.nome,self.saldo

    def alterarNome(self, novo_nome):
        self.nome = novo_nome
        return self.nome

    def deposito(self, valor):
        return self.saldo + valor
        

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
           return self.saldo - valor
        else:
            return 'Saldo insuficiente'
        
    



jose=ContaCorrente(321321,'José Paulo',10000)
print(jose.getConta())
print(jose.alterarNome('Paulo'))
print(jose.deposito(1000))
print(jose.saque(12000))
print(jose.saque(1000))

        



