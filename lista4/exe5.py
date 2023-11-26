class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave, self.chave, self.direita and self.direita.chave)


def altura(raiz):
    if not raiz:
        return 0

    altura_esquerda = altura(raiz.esquerda)
    altura_direita = altura(raiz.direita)

    return 1 + max(altura_esquerda, altura_direita)


def balanceada(raiz):
    if not raiz:
        return True, 0

    esquerda_balanceada, altura_esquerda = balanceada(raiz.esquerda)
    direita_balanceada, altura_direita = balanceada(raiz.direita)

    if not esquerda_balanceada or not direita_balanceada or abs(altura_esquerda - altura_direita) > 1:
        return False, 0

    altura_atual = 1 + max(altura_esquerda, altura_direita)

    return True, altura_atual


# Cria a árvore 1
raiz = NodoArvore(40)
raiz.esquerda = NodoArvore(20)
raiz.direita = NodoArvore(60)
raiz.direita.esquerda = NodoArvore(50)
raiz.direita.direita = NodoArvore(70)
raiz.esquerda.esquerda = NodoArvore(10)
raiz.esquerda.direita = NodoArvore(30)

# Verifica se a árvore é balanceada
balanceada, altura_arvore = balanceada(raiz)
if balanceada:
    print("A árvore é balanceada.")
else:
    print("A árvore não é balanceada.")
