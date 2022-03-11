# Seção 7 - Colections
#
# O python possui alguns tipos de coleções:
# i.    Listas
# ii.   Tuplas
# iii.  Dicionarios
# iv.   Mapas
# v.    CONJUNTOS
#
# 3. Conjuntos(Sets):
#
# Os conjuntos são referenciados por {}. Porém são diferentes dos dicionarios.
#
# Obs: Quando se fala de conjuntos, em qualquer linguagem de programação, estamos fazendo referencia
# a Teoria dos Conjuntos da Matemática.
#
# No Python, os conjuntos são chamados de Sets.
# Os sets(conjuntos) não possuem valores duplicados;
# Os sets não possuem valores ordenados;
# Os elementos de um set não são acessados via indices, ou seja, os conjuntos não são indexados.
#
# Usa-se conjuntos para armazenar elementos não levando em consideração a ordem deles.


# Diferenças entre sets e dicionarios (python):
    #
    # Dicionarios possuem chave/valor, conjuntos possuem apenas valor
    # 

# Definindo um conjunto(set):
    #
    # FORMA 1:
"""
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # O conjunto possui dados repetidos
print(s)                                # Mas as repetições não são adicionadas ao set
print(type(s))                          # Tipo de dado retornado: <class set>
"""
    # FORMA 2 (mais comum):
"""
s = {1, 2, 3, 4, 5, 5} # Lembrando que os elementos repetidos são ignorados
print(s)
print(type(s))
"""

# Convertendo sets:
"""
s = set("Geek University")  # String > Set
print(s)

l = set([1, 2, 3, 4, 5, 6, 7, 4, 3, 2]) # Lista > Set
print(l)

t = set((1, 3, 4, 3, 6, 7)) # Tupla > Set
print(t)
"""

# Diferenças entre as coleções:
"""
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]    # As listas aceitam valores duplicados
print(f"Lista: {lista}")

tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)    # As tuplas aceitam valores duplicados
print(f"Tupla: {tupla}")

dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')  # Os dicionarios não aceitam chaves duplicadas
print(f"Dicionario: {dicionario}")

conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34} # Os conjuntos NÃO aceitam valores duplicados
print(f"Conjunto: {conjunto}")
"""

# Iterando sobre sets:
"""
s = {1, 'b', True, 34.22, 44}
for valor in s:
    print(valor)
"""

# Adicionando elementos ao conjunto:
    #
    # conjunto.add(elemento) > adiciona o elemento ao conjunto
"""
s = {1, 2, 3}
print(f"Antes de add: {s}")
s.add(4)
print(f"Depois de add: {s}")
"""

# Removendo elementos do conjunto:
    #
    # FORMA 1 - remove():
        # conjunto.remove(elemento) > remove o elemento do conjunto.
        # OBS: não confundir 'elemento' com o indice, pois os conjuntos
        #      não são indexados.
"""
s = {1, 2, 3}
print(f"Antes de remover: {s}")
s.remove(3)
print(f"Depois de remover: {s}")
"""
    # FORMA 2 - discard():
        #conjunto.discard(elemento) > remove o elemento do conjunto.
"""
s = {1, 2, 3}
print(f"Antes de remover: {s}")
s.discard(2)
print(f"Depois de remover: {s}")
"""

# Copiando um conjunto:
    #
    # FORMA 1 - Deep Copy:
        # novo = conjunto.copy() > Copia o conjunto para uma nova variavel
        # OBS: os conjuntos são independentes. Então, uma alteração no 'novo'
        # não altera o 'conjunto'.
"""
s = {1, 2, 3}
novo = s.copy()
novo.add(4) # Alteração NÃO afeta o conjunto 's'.
print(f"S = {s}")
print(f"Novo = {novo}")
"""
    # FORMA 2 - Shallow Copy:
        # novo = conjunto > copia o conjunto para uma nova variavel
        # OBS: os conjuntos são exatamente os mesmos conjuntos. Então, uma alteração
        # no 'novo' ALTERA o 'conjunto'.
"""
s = {1, 2, 3}
novo = s
novo.add(4) # Alteração afeta o conjunto 's'
print(f"S = {s}")
print(f"Novo = {novo}")
"""

# Removendo todos os elementos do conjunto:
    #
    # conjunto.clear() > limpa o conjunto, deixando-o vazio
"""
s = {1, 2, 3}
print(f"Antes de limpar: {s}")
s.clear()
print(f"Depois de limpar: {s}")
"""

# Métodos matemáticos dos conjuntos:
    #
    # 1. UNIÃO:
        # FORMA 1 - union():
            # novo = conjunto1.union(conjunto2) > Une dois conjuntos num só set

"""
conjunto_1 = {"Marcos", "Patricia", "Ellen", "Pedro", "Julia", "Guilherme"}
conjunto_2 = {"Fernando", "Gustavo", "Julia", "Ana", "Patricia"}
print(f"Set_1 = {conjunto_1}")
print(f"Set_2 = {conjunto_2}")
uniao = conjunto_1.union(conjunto_2)
print(f"União = {uniao}")
"""
        # FORMA 2 - utilizando | (pipe):
"""
conjunto_1 = {"Marcos", "Patricia", "Ellen", "Pedro", "Julia", "Guilherme"}
conjunto_2 = {"Fernando", "Gustavo", "Julia", "Ana", "Patricia"}
print(f"Set_1 = {conjunto_1}")
print(f"Set_2 = {conjunto_2}")
uniao = conjunto_1 | conjunto_2
print(f"União = {uniao}")
"""
    #
    # 2. INTERSEÇÃO:
        # FORMA 1 - intersection():
"""
conjunto_1 = {"Marcos", "Patricia", "Ellen", "Pedro", "Julia", "Guilherme"}
conjunto_2 = {"Fernando", "Gustavo", "Julia", "Ana", "Patricia"}
print(f"Set_1 = {conjunto_1}")
print(f"Set_2 = {conjunto_2}")
intersecao = conjunto_1.intersection(conjunto_2)
print(f"Interseção = {intersecao}")
"""
        # FORMA 2 - utilizando o &:
"""
conjunto_1 = {"Marcos", "Patricia", "Ellen", "Pedro", "Julia", "Guilherme"}
conjunto_2 = {"Fernando", "Gustavo", "Julia", "Ana", "Patricia"}
print(f"Set_1 = {conjunto_1}")
print(f"Set_2 = {conjunto_2}")
intersecao = conjunto_1 & conjunto_2
print(f"Interseção = {intersecao}")
"""
    #
    # 3. DIFERENÇA - difference():
"""
conjunto_1 = {"Marcos", "Patricia", "Ellen", "Pedro", "Julia", "Guilherme"}
conjunto_2 = {"Fernando", "Gustavo", "Julia", "Ana", "Patricia"}
print(f"Set_1 = {conjunto_1}")
print(f"Set_2 = {conjunto_2}")
only_conj1 = conjunto_1.difference(conjunto_2)
only_conj2 = conjunto_2.difference(conjunto_1)
print(f"Só no conjunto 1 = {only_conj1}")
print(f"Só no conjunto 2 = {only_conj2}")
"""

# Soma*, Valor máximo*, valor minimo*, tamanho:
    # * > Se os valores forem inteiros ou reais
"""
s = {1, 2, 3, 4, 5}
print(f"Soma: {sum(s)}")
print(f"Maior valor: {max(s)}")
print(f"Menor valor: {min(s)}")
print(f"Tamanho: {len(s)}")
"""
