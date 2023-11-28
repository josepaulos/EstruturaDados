#Determine se uma árvore é simétrica.
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

def e_simetrica(raiz):
    def e_simetrica_aux(raiz1, raiz2):
        if raiz1 is None and raiz2 is None:
            return True
        if raiz1 is None or raiz2 is None:
            return False

        return (raiz1.chave == raiz2.chave) and \
               e_simetrica_aux(raiz1.esquerda, raiz2.direita) and \
               e_simetrica_aux(raiz1.direita, raiz2.esquerda)

    if raiz is None:
        return True

    return e_simetrica_aux(raiz.esquerda, raiz.direita)


    # Cria a arvore 1
raiz = NodoArvore(40)
raiz.esquerda = NodoArvore(20)
raiz.direita = NodoArvore(20)
raiz.direita.esquerda = NodoArvore(30)
raiz.direita.direita = NodoArvore(10)
raiz.esquerda.esquerda = NodoArvore(10)
raiz.esquerda.direita = NodoArvore(30)

em_ordem(raiz)

# Verifica se a árvore é simétrica
if e_simetrica(raiz):
    print("A árvore é simétrica.")
else:
    print("A árvore não é simétrica.")