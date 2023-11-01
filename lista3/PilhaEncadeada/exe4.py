#4. Construa um programa utilizando uma pilha que resolva o seguinte problema: 

# Armazene as placas dos carros (apenas os números) que estão estacionados numa rua sem saída estreita. 
# Dado uma placa verifique se o carro está estacionado na rua. 
# Caso esteja, informe a sequência de carros que deverá ser retirada para que o carro em questão consiga sair.


class Pilha:
    def __init__(self):
        self.itens = []

    def vazia(self):
        return len(self.itens) == 0

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.vazia():
            return self.itens.pop()
        else:
            return None  

def verificar_estacionamento(placa_desejada, carros_estacionados):
    
    estacionamento = Pilha()

    
    for carro in carros_estacionados:
        estacionamento.empilhar(carro)

    
    sequencia_retirada = []
    encontrado = False
    while not estacionamento.vazia():
        carro = estacionamento.desempilhar()
        sequencia_retirada.append(carro)
        if carro == placa_desejada:
            encontrado = True
            break

    
    if not encontrado:
        return "Carro não está estacionado na rua."

   
    sequencia_retirada = sequencia_retirada[:-1]  
    sequencia_retirada.reverse()

    return sequencia_retirada


carros_estacionados = ["ABC123", "XYZ456", "DEF789", "GHI101", "JKL202"]
placa_desejada = "DEF789"

resultado = verificar_estacionamento(placa_desejada, carros_estacionados)

if type(resultado) == list:
    print(f"Para sair com a placa {placa_desejada}, retire os seguintes carros nesta ordem:")
    for carro in resultado:
        print(carro)
else:
    print(resultado)
