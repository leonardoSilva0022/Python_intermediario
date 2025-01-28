# Exercícios 
# crie funções que duplicam, triplicam e quadriplicam
# o numero recebido como parâmetro.

def duplica_numero(numero):
    return numero * 2

def triplica_numero(numero):
    return numero *3

def quadriplica_numero(numero):
    return numero * 4

# Exemplo de uso:
numero_original = 5

duplicado = duplica_numero(numero_original)
triplicado = triplica_numero(numero_original)
quadriplicado = quadriplica_numero(numero_original)

print(f'O dobro de {numero_original} é {duplicado}')
print(f'O triplo de {numero_original} é {triplicado}')
print(f'O quádruplo de {numero_original} é {quadriplicado}')