# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes
# classes.
# string = 'Leonardo' # str
# print(string.upper())
# print(isinstance(string, str))
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Leonardo', 'Soares')
# p1.nome = 'Leonardo'
# p1.sobrenome = 'Silva'

p2 = Pessoa('Mary', 'Soares')
# p2.nome = 'Mary'
# p2.sobrenome = 'Soares'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)
