# Ordem dos decoradores
def paramentros_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)

        def sua_nova_funcao(*args, **kwargs):
            res =  func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador


@paramentros_decorador(nome='5')
@paramentros_decorador(nome='4')
@paramentros_decorador(nome='3')
@paramentros_decorador(nome='2')
@paramentros_decorador(nome='1')
def soma(x, y):
    return x + y


dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)

