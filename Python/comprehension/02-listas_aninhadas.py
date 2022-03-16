#
# Listas Aninhadas:
    #
    # Algumas linhagens de programação (C/C++, java, php) possuem uma estrutura de dados
    # chamadas de arrays:
        # Unidimensionais   > Arrays/Vetores
        # Multidimensionais > Matrizes
    #
    # Em python temos as listas.
#
# Exemplos:
"""
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3
print(listas)
"""

# Acessando os dados:
"""
print(listas[0])
print(listas[0][1])
print(listas[2][1])
"""

# Iterando sobre listas aninhadas:

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # FORMA 1:
"""
for lista in listas:
    for num in lista:
        print(num)
"""
    # FORMA 2:
"""
for i in range(len(listas)):
    for j in range(len(listas[0])):
        print(listas[i][j])
"""

    # FORMA 3 - List Comprehension:
"""
[[print(valor) for valor in lista] for lista in listas]
"""

# Outros exemplos:
    #
    # Tabuleiro(Matriz 3x3)
"""
tabuleiro = [[num for num in range(1, 4)] for lista in range(1, 4)]
print(tabuleiro)
"""
    #
    # Gerando jogadas para um jogo da velha
"""
velha = [['X' if num % 2 == 0 else 'O' for num in range(1, 4)] for lista in range(1, 4)]
print(velha)
"""
    #
    # Gerando valores iniciais
"""
velha = [['-' for i in range(1, 4)] for j in range(1, 4)]
[print(lista) for lista in velha]
"""