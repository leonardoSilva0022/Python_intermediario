# reduce - faz a reduação de um iterável em um valor
from functools import reduce

produtos = [ 
    {'nome': 'Produtos 5', 'preco': 10.00},
    {'nome': 'Produtos 1', 'preco': 22.32},
    {'nome': 'Produtos 3', 'preco': 10.11},
    {'nome': 'Produtos 2', 'preco': 105.87},
    {'nome': 'Produtos 4', 'preco': 69.90},
]


# def funcao_do_reduce(acumulador, produto):
#     print('acumulador', acumulador)
#     print('produto', produto)
#     print()
#     return acumulador + produto['preco']

total = reduce(
    lambda ac, p: ac + p['preco'],
    produtos,
    0
)


print('Total é', total)

# total = 0
# for p in produtos:
#     total +=p['preco']

# print(total)