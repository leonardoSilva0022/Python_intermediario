def divisãoFn(x, y):
    return x / y


def multiplicaçãoFn(x, y):
    return x * y


def potenciaçãoFn(x, y):
    return x ** y

numeros = [1, 2, 3, 4, 5]
divisão = [divisãoFn(numero , 2) for numero in numeros]
multiplicação = [numero * 2 for numero in numeros]
quadrado = [numero ** 2 for numero in numeros]

print(numeros)
print(divisão)
print(multiplicação)
print(quadrado)