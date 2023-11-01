# 6. Escreva uma função chamada TPilha2 que recebe como parâmetro 2 pilhas (N e P) e um vetor de inteiros. Para cada um: 

# se positivo, inserir na pilha P; 
# se negativo, inserir na pilha N; 
# se zero, retirar um elemento de cada pilha.


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

def TPilha2(pilha_P, pilha_N, vetor):
    for numero in vetor:
        if numero > 0:
            pilha_P.empilhar(numero)
        elif numero < 0:
            pilha_N.empilhar(numero)
        elif numero == 0:
            elemento_P = pilha_P.desempilhar()
            elemento_N = pilha_N.desempilhar()
            if elemento_P is not None and elemento_N is not None:
                pass


pilha_P = Pilha()
pilha_N = Pilha()
vetor = [3, -2, 0, 4, -5, 0]

TPilha2(pilha_P, pilha_N, vetor)

print("Elementos na pilha P:")
while not pilha_P.vazia():
    elemento = pilha_P.desempilhar()
    print(elemento)

print("Elementos na pilha N:")
while not pilha_N.vazia():
    elemento = pilha_N.desempilhar()
    print(elemento)
