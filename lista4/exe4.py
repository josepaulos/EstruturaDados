#. Calcule a altura de uma BST.
def altura(raiz):
    countEsquerda, countDireita, count = 0,0,0
    if raiz == None:
        return 0
    elif(raiz.esquerda != None or raiz.direita != None):
        countEsquerda += 1
        countEsquerda += altura(raiz.esquerda)
        countDireita += altura(raiz.direita)
        count = max(countDireita, countEsquerda)
    return count

# Exemplo de uso:
# Criando uma árvore simples
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        
raiz = Node(1)
raiz.esquerda = Node(2)
raiz.direita = Node(3)
raiz.esquerda.esquerda = Node(4)
raiz.esquerda.direita = Node(5)

# Chamando a função altura
print(altura(raiz))  # Saída esperada: 3
