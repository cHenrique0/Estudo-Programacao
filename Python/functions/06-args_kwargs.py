#
# Parametros args e kwargs
#
#
# 1. *args:
    #
    # Permite que a função receba uma quantidade de parâmetros arbitrária.
    # Pode receber qualque nome, mas é vital que tenha o * na frente.
    # O nome args é uma convenção da comunidade Python.
    # *args coloca os parâmetros informados dentro de uma tupla.

# Usando apenas *args:

"""
def soma_numeros(*numeros):
    return sum(numeros)

print(soma_numeros())
print(soma_numeros(0))
print(soma_numeros(0, 1))
print(soma_numeros(0, 1, 2))
print(soma_numeros(0, 1, 2, 3))
print(soma_numeros(0, 1, 2, 3, 4))
print(soma_numeros(0, 1, 2, 3, 4, 5))
"""

# Usando *args junto de outros parâmetros:
    # Se quisermos utilizar outros parêmtros, eles devem ser declarados antes do *args
"""
def do_something(name, email, *args):
    # name e email são obrigatórios
    
    # retorno para efeito de aprendizagem
    return name, email, sum(args)

print(do_something('Marcelo', 'marcelo@gmail.com', 1, 2, 3, 4, 5))
"""

# Passando uma coleção(list, tuple e set) como argumento
    # usando * na passagem de argumento na chamada da função
    # o * realiza o desempacotamento implicito da coleção
        # desempacotamento explicito:
            # list = [item_1, item_2, item_3, ..., item_n]
            # var_1, var_2, var_3, ..., var_n = list
            # cada item na lista será atribuido a uma variavel
        
"""
def soma_numeros(*args):
    return sum(args)

numeros = [1, 2, 3, 4, 5]
print(soma_numeros(*numeros))
"""

#
# 2. **kwargs
    #
    # Assim como o args, nomear o parâmetro como kwargs é uma convenção da comunidade 
    # Python, assim, pode-se dar qualquer nome a ele.
    # O **kwargs exige a utilização de parâmetros nomeados e os tranforma em um
    # dicionário python.

# Usando **kwargs

def favorite_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person.title()}'s favorite color is {color}")

favorite_colors(marcos='green', julia='yellow', fernanda='blue', vanessa='white')
