#
# Exercicios
#
# 1.

"""
A = [1, 0, 5, -2, -5, 7]
soma = A[0] + A[1] + A[5]
print(f"Soma: {A[0]} + {A[1]} + {A[5]} = {soma}")
A[4] = 100
[print(x) for x in A]
"""

# 2.
"""
inteiros = []
while len(inteiros) < 6:
    x = int(input("Digite um valor inteiro: "))
    inteiros.append(x)
print(f"Você digitou os seguintes valores: {inteiros}")
"""

# 3. 
"""
reais = [float(input("Digite um numero real: ")) for x in range(10)]
quadrado = [x ** 2 for x in reais]
print(f"Reais digitados: {reais}")
print(f"Reais ao quadrado: {quadrado}")
"""

# 4.
"""
vetor = [float(input("Digite um numero: ")) for _ in range(8)]
print("Digite dois número entre 0 e 7:")
x = int(input("1° numero: "))
y = int(input("2° numero: "))
soma = 0
for indice, elemento in enumerate(vetor):
    if indice == x or indice == y:
        soma += elemento
print(f"Vetor digitado: {vetor}")
print(f"A soma dos elementos nas posições {x} e {y} é: {soma}")
"""

# 5.
"""
vetor = [int(input("Digite números inteiros: ")) for x in range(10)]
par = 0
for x in vetor:
    if x % 2 == 0:
        par += 1
print(f"O tamanho do vetor é: {len(vetor)}")
print(f"O vetor possui {par} valores pares.")
"""

# 6.
"""
v = input("Digite 10 numeros separados por virgula: ")
vetor = v.split(",")
for i in range(len(vetor)):
    vetor[i] = int(vetor[i])
print(f"O maior valor é: {max(vetor)}")
print(f"O menor valor é: {min(vetor)}")
"""

# 7.
"""
vetor = [int(input("Digite um numero inteiro: ")) for x in range(10)]
maior = max(vetor)
print(f"Vetor: {vetor}")
print(f"Maior valor: {maior}")
print(f"Indice do maior valor: {vetor.index(maior)}")	
"""

# 8.
"""
vetor = [int(input("Digite um numero inteiro: ")) for x in range(6)]
vetor.reverse()
print(vetor)
"""

# 9.
"""
vetor = [int(input("Digite um numero inteiro par: ")) for x in range(6)]
vetor.reverse()
print(vetor)
"""

# 10.
"""
vetor = [float(input("Digite um numero inteiro: ")) for x in range(15)]
media = sum(vetor)/len(vetor)
print(f"A média geral é: {media}")
"""

# 11.
"""
vetor = [float(input("Digite um numero inteiro: ")) for x in range(10)]
qtd_negativos = 0
soma_positivos = 0
for x in vetor:
    if x < 0:
        qtd_negativos += 1
    if x % 2 == 0 and x > 0:
        soma_positivos += x
print(f"O vetor tem {qtd_negativos} números negativos")
print(f"A soma dos números positivos é: {soma_positivos}")
"""

# 12.
"""
vetor = [float(input("Digite um numero: ")) for x in range(5)]
print(f"Vetor: {vetor}")
print(f"Maior valor: {max(vetor)}")
print(f"Menor valor: {min(vetor)}")
print(f"Média dos valores: {sum(vetor)/len(vetor)}")
"""

# 13.
"""
vetor = [float(input("Digite um numero: ")) for x in range(5)]
maior = max(vetor)
menor = min(vetor)
print(f"O menor valor({menor}) está na posição {vetor.index(menor)}")
print(f"O maior valor({maior}) está na posição {vetor.index(maior)}")
"""

# 14.
"""
vetor = [float(input("Digite um numero: ")) for x in range(10)]
repetidos = []
for i in range(len(vetor)):
    if vetor.count(vetor[i]) > 1:
        if vetor[i] not in repetidos:
            repetidos.append(vetor[i])
print(f"O números repetidos são: {repetidos}")
"""

# 15.
"""
#vetor = [float(input("Digite um numero: ")) for x in range(20)]
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 11, 44, 5, 3, 2, 7, 10, 90]
n_rep = []
for x in vetor:
    if x not in n_rep:
        n_rep.append(x)
vetor = vetor.clear()
vetor = n_rep

print(vetor)
"""

# 16.
"""
vetor = [float(input("Digite um numero real: ")) for x in range(5)]
op = -1
while op != 0:
    print("\nDigite um código:\n\t0 -> Finalizar\n\t1 -> Mostrar o vetor digitado\n\t2 -> Mostrar o vetor na ordem inversa")
    cod = int(input("\n\t > "))
    if cod == 0:
        op = 0
    elif cod == 1:
        print(f"Vetor digitado: {vetor}")
    elif cod == 2:
        vetor.reverse()
        print(f"Vetor na ordem inversa: {vetor}")
    else:
        print("Digite um código válido")
print("Programa finalizado!")
"""

# 17.
"""
vetor = [float(input("Digite um numero: ")) for x in range(10)]
print(f"Vetor digitado: {vetor}")
for i in range(len(vetor)):
    if vetor[i] < 0:
        vetor[i] = 0
print(f"Vetor com 0's: {vetor}")
"""

# 18.
"""
vetor = [float(input("Digite um numero: ")) for x in range(10)]
x = int(input("Digite um numero inteiro: "))
for y in vetor:
    if y % x == 0:
        print(f"{y} é multiplo de {x}")
"""

# 19.
"""
vetor = [(i+5*i)%(i+1) for i in range(50)]
print(f"Vetor: {vetor}")
"""

# 20.
"""
vetor = [int(input("Digite um numero inteiro entre 0 e 50: ")) for x in range(10)]
impar = []
for x in vetor:
    if x % 2 != 0:
        impar.append(x)
print(f"Vetor digitado: {vetor}")
print(f"Numeros impares do vetor: {impar}")
"""

# 21.
"""
A = [float(input("Digite um numero pro vetor A: ")) for x in range(10)]
B = [float(input("Digite um numero pro vetor B: ")) for x in range(10)]
C = []
for i in range(len(A)):
    for j in range(len(B)):
        if i == j:
            c = A[i] - B[j]
            C.append(c)
print(A)
print(B)
print(C)
"""

# 22.
"""
print("Preenchendo o 1º vetor")
vetor_1 = [int(input("Digite um número inteiro: ")) for _ in range(10)]
print("Preenchendo o 2º vetor")
vetor_2 = [int(input("Digite um número inteiro: ")) for _ in range(10)]
vetor_3 = []
for item in range(10):
    vetor_3.append(vetor_1[item])
    vetor_3.append(vetor_2[item])

print(f"1º vetor: {vetor_1}")
print(f"2º vetor: {vetor_2}")
print(f"vetor resultante: {vetor_3}")
"""

# 23.
"""
print("1º vetor")
vetor_1 = [float(input("Digite um número real: ")) for _ in range(5)]
print("2º vetor")
vetor_2 = [float(input("Digite um número real: ")) for _ in range(5)]
prod = sum([v1*v2 for v1, v2 in zip(vetor_1, vetor_2)])
print(f"1º vetor: {vetor_1}")
print(f"2º vetor: {vetor_2}")
print(f"Produto escalar: {prod}")
"""
