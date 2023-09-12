class Bomba:
    def __init__(self, combustivel_t, valor_l, quantCombustivel):
        self.combustivel_t = combustivel_t
        self.valor_l = valor_l
        self.quantCombustivel = quantCombustivel

    def abastecer_por_valor(self, valor_abastecido):
        litros_abastecidos = valor_abastecido / self.valor_l
        if litros_abastecidos <= self.quantCombustivel:
            self.quantCombustivel -= litros_abastecidos
            return litros_abastecidos
        else:
            litros_abastecidos = self.quantCombustivel
            self.quantCombustivel = 0
            return litros_abastecidos

    def abastecer_por_litro(self, litros_abastecidos):
        valor_a_pagar = litros_abastecidos * self.valor_l
        if litros_abastecidos <= self.quantCombustivel:
            self.quantCombustivel -= litros_abastecidos
            return valor_a_pagar
        else:
            litros_abastecidos = self.quantCombustivel
            valor_a_pagar = litros_abastecidos * self.valor_l
            self.quantCombustivel = 0
            return valor_a_pagar

    def alterar_valor(self, novo_valor_l):
        self.valor_l = novo_valor_l

    def alterar_combustivel(self, novo_combustivel_t):
        self.combustivel_t = novo_combustivel_t

    def alterar_quantCombustivel(self, nova_quantCombustivel):
        self.quantCombustivel = nova_quantCombustivel

    def mostrar_status(self):
        print(f"Tipo de Combustível: {self.combustivel_t}")
        print(f"Valor por Litro: R${self.valor_l}")
        print(f"Quantidade de Combustível Restante: {self.quantCombustivel} litros")


bomba = Bomba(combustivel_t="Gasolina", valor_l=5.0, quantCombustivel=1000.0)

bomba.mostrar_status()

litros_abastecidos = bomba.abastecer_por_valor(160.0)
print(f"Litros abastecidos: {litros_abastecidos} litros")

valor_a_pagar = bomba.abastecer_por_litro(32.0)
print(f"Valor a pagar: R${valor_a_pagar}")

reservatorio = 1000.0 - litros_abastecidos
print(f"quantidade de combustivel apos abastecimento: {reservatorio}litros ")