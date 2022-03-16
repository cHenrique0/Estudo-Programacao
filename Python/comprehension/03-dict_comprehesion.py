#
# Dictionary Comprehesion:
    #
    # Usamos o mesmo principio do list comprehension.
    #
#
# Exemplos:

"""
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(f"Números: {numeros}")
print(f"Quadrado: {quadrado}")

numeros = [1, 2, 3, 4, 5]
quadrado = {valor: valor ** 2 for valor in numeros}
print(f"Números: {numeros}")
print(f"Quadrado: {quadrado}")

chave = 'abcde'
valor = [1, 2, 3, 4, 5]
mistura = {chave[i]: valor[i] for i in range(len(chave))}
print(mistura)

d = {chave:valor**2 for chave, valor in enumerate(range(10))}
print(d)
"""