class Automovel:
    #classe do carro
    def __init__(self , placa):
        print("Executand o construtor..")
        self.set_placa(placa)
    def get_placa(self):
        return self.__placa
    def set_placa(self, placa):
        if len(placa) < 5:
            print("A placa não tem o suficiente ")
            self.__placa = None
        else:
            self.__placa=placa
    def dirigir(self,velocidade):
        print('Estou dirigindo a',self.velocidade,'KM/H')





corola = Automovel('123231')
fusca = Automovel('123')

print(corola.get_placa())
print(fusca.get_placa())