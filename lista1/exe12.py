class Conta:
    def __init__(self, saldo, juros):
        self.saldo = saldo
        self.juros = juros / 100 

    def adicioneJuros(self):
        self.saldo += self.saldo * self.juros


poupanca = Conta(saldo=1000.0, juros=10.0)
print("saldo inicial é: R$1000")

for _ in range(5):
    poupanca.adicioneJuros()


print(f"Saldo após 5 aplicações de juros: R${poupanca.saldo}")