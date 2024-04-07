# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
def divide(n, d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    
    return n / d

print(divide(8, 0))
