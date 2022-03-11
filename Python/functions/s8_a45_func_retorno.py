#
# Funções com retorno:
    #
    # Para retornar valores em funções python usa-se a palavra reservada 'return'
    # A palavra 'return' finaliza a execução da função.
    # Pode-se ter, em uma unica função, diferentes retornos.
    # Uma função pode retornar diferentes tipos de dados e multiplos valores.
#

"""
def quadrado_de_7():
    return 7 * 7    # Retorno da função

quad = quadrado_de_7()  # Guardando o retorno da função numa variavel
print(quad)
"""

# Multiplos returns e valores de diferentes tipos de dados
"""
def nova_funcao():
    var = True
    if var:
        return 4
    elif var is None:
        return 3.2
    return 'b'

print(nova_funcao())
"""

# Retornando multiplos valores
"""
def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)
"""

# Cara ou coroa:
"""
from random import random

def joga_moeda():
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())
"""