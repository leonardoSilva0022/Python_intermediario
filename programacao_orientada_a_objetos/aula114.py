# Funções recursivas e recursividade
# - funções que podem se chamar de volta 
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problrma que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema 
# - Um caso base que para a recursão
# fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120
#https://brasilescola.uol.com.br/matematica/fatorial.htm
# import sys

# sys.setrecursionlimit(1004)


# def recursiva(inicio=0, fim=4):
#     print(inicio, fim)

#     # Caso base
#     if inicio >= fim:
#         return fim
    

#     # Caso recursivo 
#     # conta até chegar ap final 
#     inicio += 1
#     return recursiva(inicio, fim)


# print(recursiva(0, 1000))

def fatctorial(n):
    if n == 1 or n == 0:
        return 1 
    
    return n * fatctorial(n - 1)


print(fatctorial(5))
print(fatctorial(10))
print(fatctorial(100))