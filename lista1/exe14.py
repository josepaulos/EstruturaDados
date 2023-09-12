class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def obter_nome(self):
        return self.nome

    def obter_salario(self):
        return self.salario

    def aumentarSalario(self, porcentagem_de_aumento):
        if porcentagem_de_aumento > 0:
            aumento = self.salario * (porcentagem_de_aumento / 100)
            self.salario += aumento
            print(f"Salário aumentado em {porcentagem_de_aumento}%.")
        else:
            print("A porcentagem de aumento deve ser maior que zero.")

jose = Funcionario("jose",25000)

print("\nInformações do Funcionário:")
print(f"Nome: {jose.obter_nome()}")
print(f"Salário: R${jose.obter_salario():.2f}")

porcentagem_de_aumento = 10
jose.aumentarSalario(porcentagem_de_aumento)

print("\nNovas Informações do Funcionário:")
print(f"Nome: {jose.obter_nome()}")
print(f"Salário: R${jose.obter_salario():.2f}")
