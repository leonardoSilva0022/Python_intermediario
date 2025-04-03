import random 

######## VALIDADOR DE CPF #######
def validador():

    ''' Função responsável por receber os numeros e verificar se é apenas numeros'''
    cpf = input("Cpf: ").replace(".","").replace("-","")
    print("="*30)
    while cpf.isdigit() == False or len(cpf) != 11:
        print("Cpf Invalido!")

    
    cpf_falso(cpf)

    if calculo_digitos(cpf,9) == False:
        print("Cpf Invalido")
    
    if calculo_digitos(cpf,9) == True:
        print("Cpf Invalido")

    else:
        print("Cpf Invalido")

def calculo_digitos(n, digito):
    ''' Função responsavel por calcular os digitos 10 e 1 do cpf- o Paramentro
    N = CPF || digito = digito a calcular'''
    contador = 0
    z = (digito+1)
    for x in n[0:digito]:
        x = int(x)
        mult = z * x
        contador+=mult
        z-=1
    resto = (contador%11)
    if resto < 2:
        resto=0
    else:
        resto = 11 - resto
    if resto != int(n[digito]):
        return False
    else:
        return True

def cpf_falso(n):
    if n == "11111111111" or n == "22222222222" or n == "33333333333":
        print("Cpf invalido")

    if n == "44444444444" or n == "55555555555" or n == "66666666666":
        print("Cpf invalido")

    if n == "77777777777" or n == "88888888888" or n == "99999999999":
        print("Cpf invalido")

############ GERADOR DE CPF ############
def gera_cpf():
    '''Função gera 9 digitos aleatorios entra 0 e 9'''
    n=""
    for x in range(9):
        n+= "".join(str(random.randint(0,9)))
    gera_digitos(n,9)
    n+="".join(str(num))
    gera_digitos(n,10)
    n+="".join(str(num))
    print("="*30)
    print('{0}{1}{2}.{3}{4}{5}.{6}{7}{8}-{9}{10}'.format(*n))


def gera_digitos(n,dig):
    '''Função responsavel por gerar os digitos 10 e 11 validos para o cpf
    O Paramentro n = os 9 digitos do gera _cpf ||| dig = digito a calcular '''
    global num
    contador = 0
    num=0
    dig = dig +1
    for x in n[0:dig]:
        x = int(x)
        mult = dig * x
        contador+=mult
        dig-=1
        resto = (contador%11)
        if resto < 2:
            num=0
        else:
            num = 11 - resto


def main():
    '''função principal'''
    while True:
        print("="*30)
        print("Validador | Gerador de cpf".center(30))
        print("="*30)
        print("[G] - Gerar Cpf Válido")
        print("[V] - Validar Cpf")
        print("[S] - Para Sair")

        op = input("Opção: ").lower()
        if op == "g":
            gera_cpf()

        elif op == "v":
            validador()

        elif op == "s":
            exit()
        else:
            print("Opção invalida")
            op = input("Opção: ").lower()

main()