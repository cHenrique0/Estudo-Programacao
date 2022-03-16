#
# List Comprehension
	#
	# Gera uma nova lista com dados processados a partir de outro iteravel.
	# Podemos criar listas apartir de ranges
#
#
# Exemplos:

"""
numeros = [1, 2, 3, 4, 5]
lista_1 = [num * 10 for num in numeros]
print(lista_1)

lista_2 = [num / 2 for num in numeros]
print(lista_2)


def funcao(valor):
    return valor * valor

lista_3 = [funcao(num) for num in numeros]
"""

# List Comprehension x Loops

    # LOOP
"""
numeros = [1, 2, 3, 4, 5]
dobros = []
for num in numeros:
    dobros.append(num * 2)

print(dobros)


   # List Comprehension

print([num * 2 for num in numeros])
"""

# Outros Exemplos
"""
nome = "Geek University"
print([letra.upper() for letra in nome])

amigos = ["maria", "julia", "pedro", "guilherme" , "vanessa"]
print([nome.title() for nome in amigos])


print([x * 3 for x in range(1, 10)])
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])
"""

# Adicionando estruturas condicionais às lists comprehesion

numeros = [1, 2, 3, 4, 5, 6]
"""
par = [num for num in numeros if num % 2 == 0]
impar = [num for num in numeros if num % 2 != 0]
print(f"Pares: {par}")
print(f"Impares: {impar}")
"""

res = [num * 2 if num % 2 == 0 else num / 2 for num in numeros]
print(res)
