#
# Exercicios Seção 8 - Funções
#
# 1.
"""
def dobro(num):
    return num * 2

print(dobro(2))
print(dobro(3))
"""

# 2.
"""
def data_por_extenso(dia, mes, ano):
    meses = ["janeiro", "fevereiro", "março", "abril",
            "maio", "junho", "julho", "agosto",
            "setembro", "outubro", "novembro", "dezembro"]
    
    mes = meses[mes-1]

    print(f"{dia} de {mes} de {ano}")


data_por_extenso(14, 8, 1995)
data_por_extenso(1, 12, 2019)
"""

# 3.
"""
def positivo_ou_negativo(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    
    return 0

print(positivo_ou_negativo(2))
print(positivo_ou_negativo(-2))
print(positivo_ou_negativo(0))
"""

# 4.
"""
def quadrado_perfeito(num):
    sqrt = int(num ** 0.5)
    if (sqrt ** 2) == num:
        return f"{num} é quadrado perfeito!"
    return f"{num} não é quadrado perfeito!"


print(quadrado_perfeito(2))
print(quadrado_perfeito(4))
print(quadrado_perfeito(9))
"""

# 5.
"""
from math import pi

def volume_esfera(raio):
    return (4/3) * pi * (raio ** 3)

print(f"Volume = {volume_esfera(3)}")
"""

# 6.
"""
def converter(hora, min, seg):
    segs = (hora * 3600) + (min * 60) + seg
    return segs

print(converter(1, 30, 25))
"""

# 7.
"""
def celsius_fahrenheit(C):
    F = (C * (9 / 5)) + 32
    return F

print(celsius_fahrenheit(0))
"""

# 8.
"""
def pitagoras(a, b):
    h = ((a ** 2) + (b ** 2)) ** (1 / 2)
    return h

print(pitagoras(3, 4))
"""

# 9.
"""
from math import pi

def volume_cilindro(raio, altura):
    vol = pi * (raio ** 2) * altura
    return vol

print(volume_cilindro(2, 10))
"""

# 10.
"""
def maior(a, b):
    if a > b:
        return a
    return b

print(maior(1, 2))
print(maior(2, 1))
"""

# 11.
"""
def calcula_nota(nota_1, nota_2, nota_3, opcao):
    media = 0
    if opcao == 'A':
        media = (nota_1 + nota_2 + nota_3) / 3
        return media
    elif opcao == 'P':
        media = ((nota_1 * 5) + (nota_2 * 3) + (nota_3 * 2)) / 10
        return media
    return 0

print(calcula_nota(5, 10, 2, 'A'))
print(calcula_nota(5, 4, 2, 'P'))
"""

# 12.
"""
def soma_algarismos(numero):
    soma = 0
    num = str(numero)
    for al in num:
        soma += int(al)
    return soma

print(soma_algarismos(251))
"""

# 13.
"""
def calcula(num_1, num_2, operacao):
    if operacao == '+':
        return num_1 + num_2
    elif operacao == '-':
        return num_1 - num_2
    elif operacao == '*':
        return num_1 * num_2
    elif operacao == '/':
        return num_1 / num_2
    return 0
        

print(calcula(2, 2, '+'))
print(calcula(2, 2, '-'))
print(calcula(2, 2, '*'))
print(calcula(2, 2, '/'))
"""

# 14.
"""
def consumo_combustivel(km, litros):
    consumo = km / litros
    if consumo < 8:
        print("Venda o carro!")
    elif 8 <= consumo <= 14:
        print("Econômico!")
    elif consumo > 14:
        print("Super econômico!")

consumo_combustivel(24, 4)
consumo_combustivel(30, 3)
consumo_combustivel(15, 1)
"""

# 15.
"""
def triangulo(lado_1, lado_2, lado_3):
    soma_1 = lado_1 + lado_2
    soma_2 = lado_1 + lado_3
    soma_3 = lado_2 + lado_3
    if lado_1 < soma_3 and lado_2 < soma_2 and lado_3 < soma_1:
        if lado_1 == lado_2 == lado_3:
            print("É um triângulo equilátero!")
        elif (lado_1 == lado_2 and lado_1 != lado_3) or (lado_1 == lado_3 and lado_1 != lado_2) or (lado_2 == lado_3 and lado_2 != lado_1):
            print("É um triângulo isósceles!")
        elif lado_1 != lado_2 != lado_3:
            print("É um triângulo escaleno!")
    else:
        print("Não é um triângulo!")


triangulo(3, 3, 3)
triangulo(3, 3, 4)
triangulo(3, 4, 3)
triangulo(4, 3, 3)
triangulo(4, 5, 3)
triangulo(1, 5, 3)
"""

# 16.
"""
def desenha_linha(num):
    print('=' * num)

desenha_linha(100)
"""

# 17.
"""
def soma_entre_numeros(num_1, num_2):
    numeros = [x for x in range(num_1 + 1, num_2)]
    return sum(numeros)

print(soma_entre_numeros(10, 15))
"""

# 18.
"""
def potencia(x, z):
    c = 1
    pot = x
    while c < z:
        x *= pot
        c += 1
    return x

print(potencia(4, 3))
"""

# 19.
"""
def maior_primo(numero):
    num = str(numero)
    fatores = []
    primos = []
    divisores = 0
    for n in num:
        if int(n) > 1:
            fatores.append(int(n))
    
    for f in fatores:
        for i in range(1, f + 1):
            if f % i == 0:
                divisores += 1
        if divisores <= 2:
            primos.append(f)
        divisores = 0
    
    return max(primos)

print(maior_primo(2))
print(maior_primo(23))
print(maior_primo(235))
print(maior_primo(2357))
print(maior_primo(23579))
"""

# 20.

# 21.

# 22.
"""
def desenha(n):
    for i in range(1, n + 1):
        print('!' * i)

desenha(3)
"""

# 23.
"""
def desenha_triangulo(n):
    for i in range(1, n):
        print('*' * i)
    for j in range(2*n - 1, n - 1, -1):
        print('*' * (j-3))

desenha_triangulo(4)
"""

# 24.
"""
def desenha_piramide(n):
    j = n - 1
    for i in range(1, 2*n):
        if i % 2 != 0:
            print(" " * (j), end="")
            print("*" * i)
            j -= 1

desenha_piramide(6)
"""

# 25.
"""
def calcula_serie(n):
    s = 0
    aux = 1
    while aux <= n:
        r = (aux ** 2) + 1
        d = (aux + 3)
        s += ((aux ** 2) + 1) / (aux + 3)
        aux += 1
    
    return s

print(calcula_serie(3))
"""

# 26.
"""
def somatorio(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    
    return sum

print(somatorio(10))
"""

# 32.
"""
def simplifica(numerador, denominador):
    n_maior = 0
    d_maior = 0
    comum = 0
    for i in range(1, numerador + 1):
        if numerador % i == 0:
            n_maior = i
        for j in range(1, denominador + 1):
            if denominador % j == 0:
                d_maior = j
            if d_maior == n_maior:
                comum = d_maior
    numerador = numerador / comum
    denominador = denominador / comum
    return numerador, denominador

print(simplifica(36, 60))
print(simplifica(5, 10))
print(simplifica(10, 10))
print(simplifica(55, 15))
"""

# 39.
"""
def troca_valor(a, b):
    aux = a
    a = b
    b = aux
    return a, b

print(troca_valor(1, 2))
"""

# 40.
"""
def valores_par(lista):
    quant = 0
    for x in lista:
        if x % 2 == 0:
            quant += 1
    
    return quant

l = [ 2, 3, 4, 5, 6, 7, 8, 9, 10]
quant = valores_par(l)
print(f"O vetor {l} tem {quant} valores par.")
"""