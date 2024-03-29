numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
novo_numeros = [numero for numero in numeros if numero > 5]
impares = [numero for numero in numeros if numero % 2 != 0]
pares = [numero for numero in numeros if numero % 2 == 0]
outro_if = [
    numero  
    if numero != 6 else 600
    for numero in pares
]

print(numeros)
print(novo_numeros)
print(impares)
print(pares)
print(outro_if)
