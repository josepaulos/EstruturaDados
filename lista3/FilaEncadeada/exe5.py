#Seu programa deverá permitir:
#–Incluir novos processos na fila de processo;           
#–Matar o processo com o maior tempo de espera;
#–Executar um processo (remover da fila)           
#–Imprimir o conteúdo da lista de processos.   

class Process:
    def __init__(self, process_id, arrival_time, execution_time, priority):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.execution_time = execution_time
        self.priority = priority
        self.waiting_time = 0  # Tempo de espera inicializado como 0

class Queue:
    def __init__(self):
        self.queue = []

    def add_process(self, process):
        self.queue.append(process)

    def kill_process(self):
        if not self.is_empty():
            self.queue.remove(max(self.queue, key=lambda x: x.waiting_time))

    def execute_process(self):
        if not self.is_empty():
            self.queue[0].execution_time -= 1
            self.queue[0].waiting_time += 1
            if self.queue[0].execution_time == 0:
                self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def display_processes(self):
        for process in self.queue:
            print(f"ID: {process.process_id}, Arrival Time: {process.arrival_time}, Execution Time: {process.execution_time}, Priority: {process.priority}, Waiting Time: {process.waiting_time}")

# Exemplo de uso:
process_queue = Queue()

# Incluir novos processos na fila
process_queue.add_process(Process(1, 0, 4, 2))
process_queue.add_process(Process(2, 1, 3, 1))
process_queue.add_process(Process(3, 2, 5, 3))

# Executar processos
while not process_queue.is_empty():
    process_queue.execute_process()

# Matar o processo com o maior tempo de espera
process_queue.kill_process()

# Exibir lista de processos
print("Lista de Processos:")
process_queue.display_processes()
