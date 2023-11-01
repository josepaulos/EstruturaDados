#3. Escreva uma função que receba como parâmetro duas pilhas e verifique de elas são iguais. Duas pilhas são iguais se possuem os mesmos elementos, na mesma ordem.


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
        
def pilhas_sao_iguais(pilha1, pilha2):
    if len(pilha1.itens) != len(pilha2.itens):
        return False  

    for elemento1, elemento2 in zip(pilha1.itens, pilha2.itens):
        if elemento1 != elemento2:
            return False  

    return True  


pilha1 = Pilha()
pilha2 = Pilha()


elementos1 = [1, 2, 3, 4, 5]
elementos2 = [1, 2, 3, 4, 5]

for elemento in elementos1:
    pilha1.empilhar(elemento)

for elemento in elementos2:
    pilha2.empilhar(elemento)

if pilhas_sao_iguais(pilha1, pilha2):
    print("As pilhas são iguais.")
else:
    print("As pilhas não são iguais.")
