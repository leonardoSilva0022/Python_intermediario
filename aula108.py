"""
Considerando dua lista de interios ou floats (lista A e lista B)
Some os valores nas lista retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vao considerar o tamanho da menor.

Exemplo:
lista_a     =[1, 2, 3, 4, 5, 6, 7]
lista_b     =[1, 2, 3, 4]

================== resultado 
lista_soma =[2, 4, 6, 8]
"""

lista_a = [10, 2, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)


lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_soma = [1 + 1,2 + 2,3 + 3,4 + 4]
print(lista_soma)