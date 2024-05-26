# Entendendo os seus próprios módulos Python
# O primeiro módulo executado chamse __main_
# Você pode importar outro modulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulo acima do __main__ por 
# padrão 
# O python conhece todos os módulos e pacotes presentes 
# nos caminho de sys.path

import aula97_m

print('Este módulo se chama', __name__)
