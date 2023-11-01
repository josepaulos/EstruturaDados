# 5. Implemente uma função chamada TPilha, que receba um vetor de inteiros com 15 elementos. Para cada um deles, como segue: 

# Se o número for par, insira-o na pilha; 
# Se o número lido for ímpar, retire um número da pilha; 
# Ao final, esvazie a pilha imprimindo os elementos.


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
def TPilha(vetor):
    pilha = Pilha()

    for numero in vetor:
        if numero % 2 == 0: 
            pilha.empilhar(numero)
        else:  
            pilha.desempilhar()

    
    print("Elementos na pilha:")
    while not pilha.vazia():
        elemento = pilha.desempilhar()
        print(elemento)


vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
TPilha(vetor)
