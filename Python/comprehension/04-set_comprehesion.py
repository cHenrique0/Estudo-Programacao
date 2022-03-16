#
# Set Comprehension
    #
    # Usa a mesma sintaxe que o list comprehension
    #
#
# Exemplos:
"""
numeros = {num for num in range(1, 7)}
print(numeros)

numeros = {x ** 2 for x in range(10)}
print(numeros)
"""

letras = {letra for letra in "Some String"}
print(letras)