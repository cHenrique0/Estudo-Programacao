# Collections
#
# O python possui alguns tipos de coleções:
# i.    LISTAS
# ii.   Tuplas
# iii.  Dicionarios
# iv.   Mapas
# v.    Conjuntos
#
# 1. Listas (list):
    # 
    # As Listas em python são representadas por [].
    # Tudo que estiver dentro dos colchetes são os elementos da lista.
    # As listas funcionam como vetores/matrizes (arrays em C e outras linguagens).
    # As lista são mutaveis, ou seja, podem sofre alterações.
    # Listas são coleções ordenadas, portanto podemos acessar qualquer elemento informando a posição(índice).
    # As listas no python são DINAMICAS e podem conter QUALQUER tipo de dados.
        # -> Dinamica: 
            # por que não possuem tamanho fixo. Ou seja, podemos criar a lista
            # e simplismente ir adicionando elementos enquanto houver memória disponivel.
        # -> Qualquer tipo de dado: 
            # as listas não possuem tipo de dados fixo.
    # Os colchetes mesmo sem nada, representam uma lista vazia.
    # Podemos confirmar isso com a função type([]).
#
# Exemplos:

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
lista3 = []
lista4 = list(range(11))
lista5 = list("abcdefgh")
lista6 = [1, 2.34, True, "Text", 'd', [1, 2, 3]]

# Encontrando um valor contido na lista:
""" 
num = 10
if num in lista4:
    print(f"O numero {num} está na lista")
else:
    print(f"O numero {num} não está na lista")
"""

# Ordenando uma lista
    #
    # a. SORT
    # list.sort()
"""
print(lista1)
lista1.sort()
print(f"Ordenando a lista 1: {lista1}")
lista1.sort(reverse=True)   # ordena a lista de forma inversa(no caso, do maior pro menor)
print(f"Ordem inversa: {lista1}")
"""

    # b. SORTED
    # sorted(list) -> ordena a lista temporariamente
""" 
print(f"Original: {lista1}")
print(f"Temporaria: {sorted(lista1)}")
print(f"Temp de ordem inversa: {sorted(lista1, reverse=True)}")
print(f"De volta ao original: {lista1}")
"""

# Contando o número de ocorrências de um elemento na lista
"""
n = 1
c = 'e'
print(f"'{n}' aparece {lista1.count(n)} vezes na lista")
print(f"'{c}' aparece {lista2.count(c)} vezes na lista")
"""

# Adicionando elementos na lista
    #
    # a. APPEND
    # lista.append(elemento) -> Insere o elemento no fim da lista
"""
print(lista1)
lista1.append(42)
print(lista1)
lista1.append([8, 3, 1])
print(lista1)
"""

    # b. EXTEND
    # lista.extend(list) -> Insere os elementos de list na lista
    # obs: 'list' pode ser qualquer elemento iteravel: lista, tupla, strings, etc
"""
print(lista1)
lista1.extend([123, 44, 67])
print(lista1)
"""
    # Obs: lista.append(list) -> insere 'list' como elemento
    #      lista.extend(list) -> insere os elementos de 'list' como valor adicional à lista

    # c. INSERT
    # lista.insert(indice, elemento) -> insere o elemento no indice informado
    # OBS: essa função NÃO SUBSTITUI o valor do indice.
"""
print(lista1)
lista1.insert(2, 'Novo valor')
print(lista1)
"""

# Concatenando listas:
    # 
    # a. Usando o operador '+'
"""
lista1 = lista1 + lista2
print(lista1)
"""

    # b. Usando a função 'extend()'
"""
lista1.extend(lista2)
print(lista1)
"""

# Invertendo a ordem da lista:
    #
    # a. REVERSE
    # list.reverse() -> reorganiza a lista de ordem inversa(de trás pra frente)
"""
print(lista1)
print(lista2)
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)
"""

    # b. SLICING
"""
print(lista1)
print(lista2)
print(lista1[::-1])
print(lista2[::-1])
"""

# Copiando uma lista:
"""
print(lista2)
copia = lista2.copy()
print(copia)
"""

# Tamanho de uma lista:
"""
print(f"Tamanho da {lista1}: {len(lista1)}")
print(f"Tamanho da {lista2}: {len(lista2)}")
print(f"Tamanho da {lista3}: {len(lista3)}")
print(f"Tamanho da {lista4}: {len(lista4)}")
print(f"Tamanho da {lista5}: {len(lista5)}")
"""

# Removendo elementos da lista:
    #
    # a. POP
    # lista.pop() -> retorna e remove o ultimo elemento da lista
"""
print(lista5)
elemento = lista5.pop()
print(lista5)
print(elemento)
"""

    # b. POP
    # lista.pop(indice) -> retorna e remove o elemento do indice informado
"""
print(lista5)
elemento = lista5.pop(2)
print(lista5)
print(elemento)
"""

    # c. DEL
    # del list[index] -> remove o elemento de acordo com o indice informado
"""
print(lista5)
del lista5[1]
print(lista5)
"""

    # d. REMOVE
    # list.remove(value) -> remove o elemento de acordo com o valor
    # OBS: o método remove() apaga apenas a PRIMEIRA ocorrência do valor.
""" 
print(lista5)
lista5.remove('a')
print(lista5)
"""

    # e. CLEAR
    # lista.clear() -> remove todos os elementos da lista
"""
print(lista5)
lista5.clear()
print(lista5)
"""

# Convertendo string em lista
    #
    # SPLIT
    # a. lista.split() -> converte uma string em lista
    # OBS: Por padrão, o split() separa os elementos da lista pelo espaço entre elas na string.
"""
curso = "Programação em Python: Essencial"
print(f"String: {curso}")
curso = curso.split()
print(f"Lista: {curso}")
"""

    # b. lista.split(separador) -> separa os elementos da lista pelo 'separador' informado
"""
curso = "Programação,em,Python:,Essencial"
print(f"String: {curso}")
curso = curso.split(',')    # Informando o separador: virgula
print(f"Lista: {curso}")
"""

# Convertendo lista em string
    #
    # separador.join(lista) -> pega cada elemento da lista e tranforma em uma string com o separador indicado
"""
lista = ["Programação", "em", "Python:", "Essencial"]
print(f"Lista: {lista}")
curso = " ".join(lista)
print(f"String: {curso}")
"""

# Iterando sobre listas:
    #
    # FOR
"""
for x in lista1:    # Printando cada elemento da lista
    print(x)
"""

    # WHILE
"""
c = 0
while c < len(lista1):
    print(lista1[c])
    c += 1
"""

# Acessando elementos pelo indice
#          0         1        2        3
cores =["verde", "amarelo", "azul", "branco"]
"""
for i in range(len(cores)):
    print(cores[i])
"""

# Gerar indices com FOR
"""
for indice, cor in enumerate(cores):
    print(f"{indice}: {cor}")
"""

# Encontrando o indice de um elemento na lista
    #
    # INDEX
    # a. lista.index(elemento) -> retorna o indice do primeiro elemento encontrado na lista
numeros = [5, 6, 7, 5, 8, 9, 10]
"""
print(numeros.index(6)) # Retorna o indice do valor 6
print(numeros.index(9)) # Retorna o indice do valor 9
print(numeros.index(5))
"""

    # b. lista.index(elemento, indice) -> retorna o indice do primeiro elemento encontrado na lista
    #                                    a partir do indice informado no parametro
"""
print(numeros.index(5, 1)) # Começa a procurar a partir do indice 1
"""

    # c. lista.index(elemento, inicio, fim) -> retorna o indice do elemento encontrado na lista
    #                                         entre os indidices inicio e fim

"""
print(numeros.index(8, 3, 6))
"""

# SLICING
#
# lista[inicio:fim:passo]
    #
    # lista[inicio:] -> começa do indice 'inicio' e vai até o fim da lista
lista = [1, 2, 3, 4]
"""
print(lista[1:])
"""
    # lista[:fim] -> começa do indice 0 e vai até o indice (fim - 1)
    # OBS: o indice fim não entra na lista.

"""
print(lista[:2]) # Começa em 0 e vai até o 2-1
print(lista[:4]) # Começa em 0 e vai até o 4-1
"""
    # lista[::passo] -> começa em 'inicio' e vai até o 'fim' a cada 'passo'
"""
print(lista[1::2]) # Começa no indice 1 e vai até o fim, de 2 em 2
print(lista[::2]) # Começa no indice 0 e vai até o fim, de 2 em 2
"""

# Tranformando lista em tupla
    #
    # tuple(lista) -> tranforma a lista em uma tupla
"""
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))
tupla = tuple(lista)
print(tupla)
print(type(tupla))
"""

# Desempacotamento de listas
    #
    # Coloca cada elemento da lista numa váriavel
    # O numero de variaveis deve ser compativel com o tamanho da lista.
"""
lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)
"""

# Copiando uma lista
    #
    # DEEP COPY
    # Se dá ao utilizar o metodo copy(), que copia o conteudo de uma lista para outra variavel
    # deixando as duas independente uma da outra.
"""
lista = [1, 2, 3]
nova = lista.copy()
print(f"lista: {lista}")
print(f"nova: {nova}")
nova.append(4) # Alteração na lista
print(f"nova: {nova}")      # Já a lista copia teve alteração
print(f"lista: {lista}")    # A lista original NÃO foi alterada
"""
    # SHALLOW COPY
    # Se dá ao utilizar a copia via atribuição.
    # Essa atribuição não torna as lista independente uma da outra.
    # Ao alterar o conteudo da copia tambem altera-se o conteudo da lista original.
"""
lista = [1, 2, 3]
nova = lista
print(f"lista: {lista}")
print(f"nova: {nova}")
nova.append(4)  # Alteranção na lista
print(f"nova: {nova}")      # A lista copia recebe a alteração
print(f"lista: {lista}")    # A lista original TAMBEM recebe a alteração
"""