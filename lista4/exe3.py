#Verifique se duas árvores binárias são idênticas.

class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave, self.chave, self.direita and self.direita.chave)


def em_ordem(raiz):
    if not raiz:
        return

    # Visita filho da esquerda.
    em_ordem(raiz.esquerda)

    # Visita nodo corrente.
    print(raiz.chave),

    # Visita filho da direita.
    em_ordem(raiz.direita)

def sao_identicas(raiz1, raiz2):
    # Se ambas as árvores são vazias, elas são idênticas
    if raiz1 is None and raiz2 is None:
        return True

    # Se uma árvore é vazia e a outra não, elas não são idênticas
    if raiz1 is None or raiz2 is None:
        return False

    # Verifica se os valores dos nós são iguais
    if raiz1.chave != raiz2.chave:
        return False

    # Verifica recursivamente as subárvores esquerda e direita
    return sao_identicas(raiz1.esquerda, raiz2.esquerda) and sao_identicas(raiz1.direita, raiz2.direita)

# Cria a arvore 1
raiz = NodoArvore(40)
raiz.esquerda = NodoArvore(20)
raiz.direita = NodoArvore(60)
raiz.direita.esquerda = NodoArvore(50)
raiz.direita.direita = NodoArvore(70)
raiz.esquerda.esquerda = NodoArvore(10)
raiz.esquerda.direita = NodoArvore(30)

# Cria a arvore 2 (identica)
raiz2 = NodoArvore(40)
raiz2.esquerda = NodoArvore(20)
raiz2.direita = NodoArvore(60)
raiz2.direita.esquerda = NodoArvore(50)
raiz2.direita.direita = NodoArvore(70)
raiz2.esquerda.esquerda = NodoArvore(10)
raiz2.esquerda.direita = NodoArvore(30)


if sao_identicas(raiz, raiz2):
    print("As árvores são idênticas.")
else:
    print("As árvores não são idênticas.")