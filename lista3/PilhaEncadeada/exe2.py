#2. Utilizando uma pilha resolver o exercício a seguir: Dada uma sequência contendo N (N >0) números reais, imprimi-la na ordem inversa.

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

def inverter_sequencia(sequencia):
    pilha = Pilha()


    for numero in sequencia:
        pilha.empilhar(numero)


    while not pilha.vazia():
        numero = pilha.desempilhar()
        print(numero)


sequencia = [1.0, 2.0, 3.0, 4.0, 5.0]

print("Sequência original:")
for numero in sequencia:
    print(numero)

print("\nSequência invertida:")
inverter_sequencia(sequencia)
