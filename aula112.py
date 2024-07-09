# filter é um filtro funcional 
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produtos 5', 'preco': 10.00},
    {'nome': 'Produtos 1', 'preco': 22.32},
    {'nome': 'Produtos 3', 'preco': 10.11},
    {'nome': 'Produtos 2', 'preco': 105.87},
    {'nome': 'Produtos 4', 'preco': 69.90},
]

def filtrar_preco(produto):
    return produto['preco'] > 100

# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 100
# ]
novos_produtos = filter( 
    # lambda produto: produto['preco'] > 100,
    filtrar_preco,
    produtos
)



print_iter(produtos)
print_iter(novos_produtos)