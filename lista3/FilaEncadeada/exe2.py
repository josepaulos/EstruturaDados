#2. Crie uma função de busca em que o usuário insere um valor (inteiro) e o programa retorna a sua posição na fila.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def pop(self):
        if self.is_empty():
            print("A fila está vazia. Não é possível fazer pop.")
            return None
        else:
            data = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return data

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" <- ")
            current = current.next
        print("Fim da fila")

    def search(self, value):
        current = self.front
        position = 1

        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1

        return None

# Exemplo de uso:
fila = Queue()

fila.push(1)
fila.push(2)
fila.push(3)

fila.display()  # Deve imprimir: 1 <- 2 <- 3 <- Fim da fila

valor_procurado = 2
posicao = fila.search(valor_procurado)

if posicao is not None:
    print(f"O valor {valor_procurado} está na posição {posicao} na fila.")
else:
    print(f"O valor {valor_procurado} não foi encontrado na fila.")

