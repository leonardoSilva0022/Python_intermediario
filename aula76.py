# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'nome'

pessoa['nome'] = 'Leonardo Soares'
pessoa['sobrenome'] = 'Silva'


print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome', None))
if pessoa.get('sobrenome') is None:
    print(' NÃO EXISTE')
else:
    print(pessoa['sobrenome'])
# print('ISSO não vai')