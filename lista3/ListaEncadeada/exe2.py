#Remova duplicatas de uma lista ordenada. 
#Suponha que lhe seja fornecida uma lista encadeada armazenando números inteiros em ordem crescente. 
#Sua tarefa é remover todos os elementos duplicados da lista. 
#Por exemplo, dada a lista [0 → 1 → 1 → 5 → 7 → 10 → 10 → None], 
#seu programa deve retornar a lista [0 → 1 → 5 → 7 → 10 → None]


class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None  # Inicialize a cabeça como None

    def adicionar(self, dado):
        novo_no = No(dado)
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    def remover_duplicatas(self):
        atual = self.cabeca
        while atual:
            proximo_no = atual.proximo
            while proximo_no and atual.dado == proximo_no.dado:
                proximo_no = proximo_no.proximo
            atual.proximo = proximo_no
            atual = proximo_no

    def exibir(self):
        atual = self.cabeca
        while atual:
            print(atual.dado, end=" -> ")
            atual = atual.proximo
        print("Nenhum")

# Exemplo de uso
lista = ListaEncadeada()
lista.adicionar(0)
lista.adicionar(1)
lista.adicionar(1)
lista.adicionar(3)
lista.adicionar(3)
lista.adicionar(10)
lista.adicionar(10)

print("Lista Original:")
lista.exibir()

lista.remover_duplicatas()

print("Lista sem as duplicatas:")
lista.exibir()
