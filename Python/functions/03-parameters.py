#
# Funções com parametro:
    #
    # Funções que recebem dados para serem processados dentro da função
    # As funções podem ter n parametros de entrada, ou seja, pode-se receber
    # quantos paremetros forem necessarios.
    # Os parametros são separados por virgula.
    # Parametros são informações de que uma função precisa para executar sua tarefa.
    #
#
# Exemplos:
    #
    # Função com 1 parametro
"""
def quadrado(numero):   # numero é o parametro da função
    return numero ** 2

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

def canta_parabens(aniversariante):
    print("Parabens pra você")
    print("Nesta data querida")
    print("Muitas felicidades")
    print("Muitos anos de vida!!!")
    print(f"Viva o {aniversariante}")

canta_parabens("Marcos")
"""
    #
    # Função com n parametros:
"""
def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 5))
print(multiplica(4, 5))
print(outra(3, 2, "Geek "))
"""


# Nomeando parametros:
    #
    # Sempre nomeie os parametros de acordo com o que a função pede/executa/retorna
    #
"""
def nome_completo(nome, sobrenome):
    return f"Seu nome completo é {string1} {string2}"

print(nome_completo("Angelina", "Jolie"))
"""

# Diferença entre parametros e argumentos:
#
# Parametro -> São as variaveis declaradas na DEFINIÇÃO da função
# Argumentos -> Dados passados na chamada de execução da função
"""
def funcao(par1, par2): # par1 e par2 são os parametros
    return par1

funcao("Sim", "Nao")    # "Sim" e "Não" são os argumentos
"""

