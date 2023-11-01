#4. Escreva uma função que inverta a ordem dos elementos da fila.  Por exemplo:

#[1] [4] [5] [2] → [2] [5] [4] [1]



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

    def reverse(self):
        if self.is_empty():
            return

        stack = []
        current = self.front

        while current:
            stack.append(current.data)
            current = current.next

        current = self.front

        while current:
            current.data = stack.pop()
            current = current.next

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" <- ")
            current = current.next
        print("Fim da fila")

# Exemplo de uso:
fila = Queue()

fila.push(1)
fila.push(4)
fila.push(5)
fila.push(2)

print("Fila original:")
fila.display()

fila.reverse()

print("Fila invertida:")
fila.display()
