# Collections
#
# O python possui alguns tipos de coleções:
# i.    Listas
# ii.   TUPLAS
# iii.  Dicionarios
# iv.   Mapas
# v.    Conjuntos
#
# 2. Tuplas (tuple):
    #
    # Tuplas são parecidas com lista.
    # Existem duas diferenças básicas:
        # As tuplas são representadas por parenteses ()
        # As tuplas são imutáveis, isso significa que não podemos fazer alterações na tupla.
    # Toda operação em uma tupla gera uma nova tupla.
    # As tuplas são DEFINIDAS pela virgula e não pelo uso do parenteses.
    # As tuplas possuem os mesmo metodos das lista, com exceção dos métodos que causam alterações,
    # pois elas são imutaveis.
    # Quando usar tuplas?
        #
        # Deve-se utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção.
        # ex: meses do ano,
#
# Exemplos:
"""
tupla1 = (1, 2, 3, 4, 5, 6)     # Criando uma tupla usando parenteses
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6       # Criando uma tuplas sem uso do parenteses
print(tupla2)
print(type(tupla2))

tupla3 = (4)    # Isso NÃO é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,)    # Isso é uma tupla
print(tupla4)
print(type(tupla4))

tupla5 = 4,
print(tupla5)
print(type(tupla5))
"""

# Gerando uma tupla com range()
"""
tupla = tuple(range(11))
print(tupla)
print(type(tupla))
"""

# Desempacotamento de tupla
    # O desempacotamento de tupla acontence da mesma forma que na lista.
"""
tupla = (2, 3)
num_1, num_2 = tupla
print(num_1)
print(num_2)
"""

# Concatenando tuplas
"""
tupla1 = 1, 2, 3
tupla2 = (4, 5, 6)
tupla3 = tupla1 + tupla2
print(tupla1)
print(tupla2)
print(tupla3)

tupla1 = tupla1 + tupla2    # As tuplas são imutaveis, mas podemos sobrescrever os valores da variavel
print(tupla1)
"""

# Verificando se um valor está na tupla
"""
tupla = (1, 2, 3)
print(3 in tupla)
print(4 in tupla)
"""

# Quantidade de ocorrencia de um elemnto na tupla
    #
    # tupla.count(elemento) > retorna a quantidade de ocorrencia do elemento na tupla.
"""
tupla = ('a', 'b', 'c', 'd', 'a', 'e')
print(tupla.count('a'))
print(tupla.count('c'))
"""
