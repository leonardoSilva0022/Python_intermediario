tentativa_max = 3 
login_correto = "admin"
senha_correta = "1234"

tentativas = 0 

while tentativas < tentativa_max:
    login = input("Nome de usuário: ")
    senha = input("Senha: ")
    
    if login == login_correto and senha == senha_correta:
        print("Acesso concedido")
        break
    else:
        tentativas += 1
        print("Usuário ou senha incorretos. Tentativas restantes:", tentativa_max - tentativas)
        
        if tentativas == tentativa_max:
            print("Conta bloqueada")
