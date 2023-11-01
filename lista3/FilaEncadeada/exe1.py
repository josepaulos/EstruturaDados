# 1. Implemente uma fila dinâmica contendo todas as funcionalidades de uma fila padrão. Para isso, resolvar:
# –Crie um nó padrão da fila.
# –Crie uma função de inicialização da fila vazia
# –Crie uma função push que cria e insere um novo nó para o final da fila.
# –Crie uma função pop que remove o primeiro elemento da fila.


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


fila = Queue()

fila.push(1)
fila.push(2)
fila.push(3)

fila.display() 

elemento_removido = fila.pop()
print("Elemento removido:", elemento_removido)

fila.display()  