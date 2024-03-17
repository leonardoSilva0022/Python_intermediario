# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Igor',
    'sobrenome': 'Gomes',
}
(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

for chave, valor in pessoa.items():
    print(chave, valor)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)
    
    