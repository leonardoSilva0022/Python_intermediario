class ListaTarefas:
    def __init__(self):
        self.todo = []  
        self.desfazer = []
        self.refazer = []  

    def adicionar_tarefa(self, tarefa):
        self.todo.append(tarefa)
        self.desfazer.append(self.todo.copy())  

    def desfazer_acao(self):
        if self.desfazer:
            self.refazer.append(self.todo.copy())  
            self.todo = self.desfazer.pop()

    def refazer_acao(self):
        if self.refazer:
            self.desfazer.append(self.todo.copy())  

# Exemplo de uso
lista = ListaTarefas()
lista.adicionar_tarefa('fazer café')
lista.adicionar_tarefa('caminhar')

print("Lista de tarefas:", lista.todo)
lista.desfazer_acao()
print("Após desfazer:", lista.todo)
lista.refazer_acao()
print("Após refazer:", lista.todo)
