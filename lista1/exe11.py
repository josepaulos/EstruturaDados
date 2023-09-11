class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.gasolina = 0

    def andar(self, distancia):
        litros_gastos = distancia / self.consumo
        self.gasolina -= litros_gastos
        print(f'Andamos {distancia} km de distância.')

    def obterGasolina(self):
        return self.gasolina

    def adicionarGasolina(self, qtd):
        self.gasolina += qtd
        print(f'Adicionado {qtd} litros ao tanque.')

