#
# Funções com parametro padrão (default parameters)
    #
    # Neste tipo de função a passagem de parametros é opcional
    # Os parâmetros com valores default(padrão) devem sempre estar ao final da declaração da função.
#
#
"""
def potencia(num, pot=2):   # pot se torna opcional pois tem o valor padrão
    return num ** pot

print(potencia(5))      # Passando 1 argumento
print(potencia(4, 3))   # Passando 2 argumentos
"""

# Exemplos:
"""
def show_info(nome="Geek", instrutor=False):
    if nome == "Geek" and instrutor:
        return "Bem vindo instrutor Geek!"
    elif nome == "Geek":
        return "Eu pensei que você era o instrutor!"
    return f"Olá, {nome}!"


print(show_info())
print(show_info(instrutor=True))
print(show_info("Ozzy"))
"""

# Recebendo uma função como parametro:
"""
def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, func=soma):
    return func(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))
"""

